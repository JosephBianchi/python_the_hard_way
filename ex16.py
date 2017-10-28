from sys import argv

script, filename = argv

# print files name from argv
print(f"we're going to erase {filename}.")

print("if you dont want that hit the ctrl-c")

print("if you do want that hit return")
# enter to move onto next command
input("?")

print("opening the file...")
# open file create file object
target = open(filename, "w+")

print("truncating the file..")
# delete file
target.truncate()


print("now im going to ask you for three lines")

line1 = input("1")
line2 = input("2")
line3 = input("3")

print("im going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()
target = open(filename, "r")

print(target.read())

print("and finally we clost it")
target.close()
