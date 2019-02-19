import pickle

some_dict = {"a":"b","c":"d"}

file_name  = "some_dict.pkl"

pickle_file = open(file_name,"wb")

pickle.dump(some_dict, pickle_file)



pickle_file.close()

with open(file_name,  "rb") as p_file:
    pickle_text = pickle.load(p_file)
    print(pickle_text)
