import sys
script, read_file, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line[:8] + line[8:]
    # raw_bytes = line.encode(encoding, errors=errors)
    cooked_string = next_lang.decode(encoding, errors=errors)
    # byte_file.write(raw_bytes)

    print(line, "<===>", cooked_string)
    # print(next_lang)

languages = open(read_file, encoding="utf-8")
# languages = open(read_file, "rb")
byte_file = open("raw_bytes.txt", "rb")

main(byte_file, input_encoding, error)