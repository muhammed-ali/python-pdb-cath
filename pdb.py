class Pdb:
    def __init__(self, datasource = '', description='', sequence_id='', sequence=[]):
        self._datasource = datasource
        self._description = description
        self._sequence_id = sequence_id
        self._sequence = sequence

    def get_datasource(self):
        return self._datasource

    def set_datasource(self, datasource):
        self._datasource = datasource

    def get_description(self):
        return self._description.strip() + "\r"

    def set_decription(self, line):
        strip_0 = line[1:]
        self._description = "description: " + strip_0 + "\r"

    def set_sequence_id(self, line):
        strip_0 = line[1:].split()
        self._sequence_id = "sequence_id: " + strip_0[0] + "\r"

    def get_sequence_id(self):
        return self._sequence_id.strip() + "\r"

    def set_sequence(self, sequence):
        self._sequence = sequence

    def get_sequence(self):
        return " ".join(self._sequence)
