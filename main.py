from os import listdir
from os.path import isdir, join

class Reader:
    totalLines = 0
    skip_pop_up = False
    files_to_ignore = []

    def start_reading(self, path):
        if not isdir(path):
            # no need to list files
            self.read_lines(path, path)
            return

        # print("\nListing all the files and subdirs under current directory...")
        list_ = listdir(path)
        print("\nFound "+str(len(list_))+" file(s) under present directory!")

        count = 1
        for f in list_:
            print(str(count)+". "+f)
            count = count + 1

        # ask for the filenames to ignore
        if not self.skip_pop_up:
            files_to_ignore_ = input("Mention which files to ignore(you can write SKIP to remove this popup forever): ")
            if files_to_ignore_:
                if files_to_ignore_ != "SKIP":
                    file_nums = files_to_ignore_.split(" ")
                    for idx in file_nums:
                        self.files_to_ignore.append(list_[int(idx)-1])
                else:
                    self.skip_pop_up =  True
                    
        for c in list_:
            if c in self.files_to_ignore:
                print("Ignoring  "+c)
                continue

            if isdir(join(path, c)):
                current_path = join(path, c)
                print("\n"+ c + " is a directory!")
                print("Accessing it...")
                self.start_reading(current_path)
                continue

            # if it is a file, read the total lines of code
            print("\n"+c + " is a file...reading the total lines...")
            filepath = join(path, c)
            self.read_lines(filepath, c)

    def read_lines(self, filepath, filename):

        with open(filepath, encoding="utf-8") as f:
            content = f.read()
            splits = content.split("\n")
            lines = len(splits) - 1
            print("No. of lines in "+filename+" is: "+str(lines))
            self.totalLines = self.totalLines + lines


class Main:
    def __init__(self):
        reader = Reader()
        init_path = input("Enter the absolute path of the project: ")
        reader.start_reading(init_path)
        print("\nTOTAL LINES OF CODE IN THE CURRENT PROJECT IS: "  + str(reader.totalLines) )

Main()
