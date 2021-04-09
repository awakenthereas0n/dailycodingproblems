# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.


# Precaution: It is advisable not to unpickle data received from an untrusted source as they may pose security threat. However, the pickle module has no way of knowing or raise alarm while pickling malicious data.

import pickle

# Dictonary of values
dcc_dict = {1:"6",2:"2",3:"f"}

# Pickle data out
pickle_out = open("dict.pickle","wb")
pickle.dump(dcc_dict, pickle_out)
pickle_out.close()

# Read pickle data from new object
pickle_in = open("dict.pickle","rb")
dcc_dict_out = pickle.load(pickle_in)

print(dcc_dict_out)