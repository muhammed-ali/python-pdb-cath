from pdb import Pdb

new_data_source = Pdb()


def search_pdb_file():
    file = read_pdb_file('./data/input/sample_pdb.txt', '>') # change it to original pdb file named pdbaa (see below)
    # file = read_pdb_file('/Users/Muhammad_Ali/Downloads/pdbaa', '>')


def read_pdb_file(path, delimiter):
    # pdb = []
    pdb_domain = ''
    with open(path, 'r') as f:
        for line in f:
            if line.startswith(delimiter):
                # sequence = []
                domain = get_domain_from_pdb_file(line)
                data_source = get_data_source(line)
                pdb_domain = domain
                read_cath_file('./data/input/sample_cath.txt', domain) # change it to original cath file named cath-domain-description-file.txt (see below)
                # read_cath_file('/Users/Muhammad_Ali/Downloads/cath-domain-description-file.txt', domain)
                new_data_source.set_datasource(data_source)
                new_data_source.set_decription(line)
                new_data_source.set_sequence_id(line)
            else:
                read_cath_file('./data/input/sample_cath.txt', pdb_domain) # change it to original cath file named cath-domain-description-file.txt (see below)
                # read_cath_file('/Users/Muhammad_Ali/Downloads/cath-domain-description-file.txt', pdb_domain)


def get_domain_from_pdb_file(line):
    pdb = line.split()
    raw_pdb = pdb[0].lower().split(':')[1].split('_')
    domain_chars = raw_pdb[0] + raw_pdb[1].upper() + '00'
    return domain_chars


def get_ver_date(line):
    if line.startswith('VERDATE'):
        ver_date = line.split()
        if ver_date[0] == 'VERDATE':
            return "_processing_date: " + ver_date[1] + "\r"


def get_data_source(line):
    data_source = line[1:].split()[0].split(':')[0]
    return "data_source_id: " + data_source + "\r"


def get_organism_tax_id(line):
    if 'Organism_taxid:' in line:
        position = line.find('Organism_taxid:')
        value = line[position:].split(' ')
        return value[0] + " " + value[1][0: -1] + "\r"


def get_organism_name(line):
    if 'Organism_taxid:' in line:
        position = line.find('Organism_taxid:')
        value = line[0:position].split(' ')
        return "organism_name: " + " ".join(value[4:]) + "\r"


def get_homol(line):
    if line.startswith('HOMOL'):
        homol = line.split()
        if homol[0] == 'HOMOL':
            return homol[0] + ": " + homol[1] + "\r"


def get_topol(line):
    if line.startswith('TOPOL'):
        topol = line.split()
        line_end = len(topol)
        real_length = int(line_end)
        return topol[0] + ": " + ' '.join(topol[1:real_length]) + "\r"


def get_arch(line):
    if line.startswith('ARCH'):
        arch = line.split()
        line_end = len(arch)
        real_length = int(line_end)
        return arch[0] + ": " + ' '.join(arch[1:real_length]) + "\r"


def get_class(line):
    if line.startswith('CLASS'):
        val = line.split()
        line_end = len(val)
        real_length = int(line_end)
        return val[0] + ": " + ' '.join(val[1:real_length]) + "\r"


def get_start(line):
    if line.startswith('SRANGE'):
        val = line.split()
        splitted_val = val[1].split('=')
        return '_start: ' + splitted_val[1] + "\r"


def get_stop(line):
    if line.startswith('SRANGE'):
        val = line.split()
        splitted_val = val[2].split('=')
        return '_stop: ' + splitted_val[1] + "\r"


def read_cath_file(path, pdb_domain):
    file_to_write = ''
    global_domain = ''
    global_data_source = new_data_source.get_datasource()
    global_sequence = 'original_sequence: '
    with open(path, 'r') as f:
        for line in f:
            # ignore comments
            if not line.startswith('#'):
                if line.startswith('DOMAIN'):
                    domain = line.split()
                    global_domain = domain[1]
                    if pdb_domain == domain[1]:
                        file_to_write = domain[1] + '.parquet'
                        pf = open('./data/output/' + domain[1] + '.parquet', "w+")
                        pf.close()
                else:
                    if global_domain == pdb_domain:
                        folder = './data/output/{}'.format(file_to_write)

                        if line.startswith('SSEQS'):
                            global_sequence += line.split()[1]

                        ver_date = get_ver_date(line)
                        if ver_date is not None:
                            pf = open(folder, 'a')
                            pf.write(ver_date)
                            pf.close()

                        start = get_start(line)
                        if start is not None:
                            pf = open(folder, 'a')
                            pf.write(start)
                            pf.close()

                        stop = get_stop(line)
                        if stop is not None:
                            pf = open(folder, 'a')
                            pf.write(stop)
                            pf.close()

                        klass = get_class(line)
                        if klass is not None:
                            pf = open(folder, 'a')
                            pf.write(klass)
                            pf.close()

                        arch = get_arch(line)
                        if arch is not None:
                            pf = open(folder, 'a')
                            pf.write(arch)
                            pf.close()

                        topol = get_topol(line)
                        if topol is not None:
                            pf = open(folder, 'a')
                            pf.write(topol)
                            pf.close()

                        homol = get_homol(line)
                        if homol is not None:
                            pf = open(folder, 'a')
                            pf.write(homol)
                            pf.close()

                        organism_tax_id = get_organism_tax_id(line)
                        if organism_tax_id is not None:
                            pf = open(folder, 'a')
                            pf.write(organism_tax_id)
                            pf.close()

                        organism_name = get_organism_name(line)
                        if organism_name is not None:
                            pf = open(folder, 'a')
                            pf.write(organism_name)
                            pf.close()

    if global_data_source is not None:
        pf = open(folder, 'a')
        pf.write(global_data_source)
        pf.close()

    if new_data_source.get_description() is not None:
        pf = open(folder, 'a')
        pf.write(new_data_source.get_description())
        pf.close()

    if new_data_source.get_sequence_id() is not None:
        pf = open(folder, 'a')
        pf.write(new_data_source.get_sequence_id())
        pf.close()

    if global_sequence is not None:
        pf = open(folder, 'a')
        pf.write(global_sequence)
        pf.close()
