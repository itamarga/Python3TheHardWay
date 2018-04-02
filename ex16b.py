from sys import argv

script, filename = argv

toread = open(filename)

print(f"Will now read {filename}")
input("Press RETURN to proceed.")

print(toread.read())
toread.close()