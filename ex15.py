from sys import argv

script, filename = argv
txt = open(filename)
prompt = "> "

print(f"here's your file {filename}:")

print(txt.read())

txt = open(filename)

txt.close()

txt = open(filename)

print(txt.read())
