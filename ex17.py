from sys import argv
from os.path import exists

script, from_file, to_file = argv


# we should do these two on one line, how?
in_file = open(from_file, "r")
# indata = in_file.read()

# print(f"the input file is {len(indata)} bytes long")

# print(f"does the output file exist? {exists(to_file)}")

# print("ready, hit return to continue, ctrl-c to abort.")
# input("?")

out_file = open(to_file, "w")
out_file.write(in_file.read())
# print("alrihgt, all done")

out_file.close()
in_file.close()
