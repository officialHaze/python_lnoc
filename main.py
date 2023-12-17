from os import listdir
from os.path import isdir, join

class Reader:
    totalLines = 0

    def start_reading(self, path):
        if not isdir(path):
            # no need to list files
            self.read_lines(path)
            return

        print("\n Listing all the files and subdirs under current directory...")
        list_ = listdir(path)
        print(list_)

        for c in list_:
            if isdir(join(path, c)):
                current_path = join(path, c)
                print("\n"+ c + " is a directory!")
                print("Accessing it...")
                self.start_reading(current_path)
                continue

            # if it is a file, read the total lines of code
            print(c + " is a file...reading the total lines...")
            filepath = join(path, c)
            self.read_lines(filepath)

    def read_lines(self, filepath):
        with open(filepath, encoding="utf-8") as f:
            content = f.read()
            splits = content.split("\n")
            lines = len(splits) - 1
            print("No. of lines in the current file is: "+str(lines))
            self.totalLines = self.totalLines + lines


class Main:
    def __init__(self):
        reader = Reader()
        init_path = input("Enter the absolute path of the project: ")
        reader.start_reading(init_path)
        print("\nTOTAL LINES OF CODE IN THE CURRENT PROJECT IS: "  + str(reader.totalLines) )

Main()
