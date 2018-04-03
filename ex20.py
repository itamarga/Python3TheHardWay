from sys import argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_one_line(line_count, f):
    print(line_count, f.readline(), end='')

script, file_to_read = argv
f = open(file_to_read)
print("First, let's print the whole file:")
print_all(f)

print("Now let's rewind, kinda like a tape.")
rewind(f)
print("Let's print three lines:")
line = 1
print_one_line(line, f)
line += 1
print_one_line(line, f)
line += 1
print_one_line(line, f)