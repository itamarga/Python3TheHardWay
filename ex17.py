from sys import argv; open(argv[2],'w').write(open(argv[1]).read())
# from os.path import exists

# script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")

# indata = open(from_file).read()

# print(f"The input file is {len(indata)} byes long")

# print(f"Does the output file exist? {exists(to_file)}")
# print("Press RETURN to continue, or CTRL-C to cancel")
# input()

# open(to_file, 'w').write(indata)
