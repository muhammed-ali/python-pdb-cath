This is a python script to extract relevant information from pdb and cath files for each pdb entry and store the individual files in a .parquet file format.

To run this data extraction script on a sample input files, I have provided the relevant input files in the "./python-pdb-cath-master/data/input/" directory. You will first need to create a "output" directory inside the "./python-pdb-cath-master/data/" directory and then execute the script by "python main.py" from the home directory of the project ("./python-pdb-cath-master/").

If you want to apply the script on the original files downloaded from the ftp servers of pdb (http://ftp.ebi.ac.uk/pub/databases/fastafiles/pdb/pdbaa.gz) and cath (ftp://orengoftp.biochem.ucl.ac.uk/cath/releases/latest- release/cath-classification-data/cath-domain-description-file.txt), please (un)comment out the relevant commands on line 7, 21, and 27 of the 'functions.py' script inside the main of the project.
