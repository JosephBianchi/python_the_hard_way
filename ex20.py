from sys import argv
# import argv

script, input_file = argv
# use argv

def print_all(f):
    print(f.read())
# func print file

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = '')


current_file = open(input_file)
# open input file

print("first let's print the whole file:\n")
print_all(current_file)

print("now let's print the whole file:\n")

print_all(current_file)

print("now lets rewind, kind of like a tape")
rewind(current_file)

print("lets print three lines")

current_line = 1 #current line
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
