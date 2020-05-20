path = "/insert/here/path/to/directory/where/files/saved"
files = os.listdir(path)
pdb_ = [path + file for file in files if file[-4:] == '.pdb'][0]
xtc_ = [path + file for file in files if file[-4:] == '.xtc'][0]
print(pdb_)
print(xtc_)
