import os
import sys
import csv
import shutil

def rename_files(csv_filename):
    with open('rename_csv.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        files_mapping = {}
        new_filenames = set()

        for row in csvreader:
            name = row[0] + '.wav'
            new = row[1] + '.wav'

            if new in new_filenames:
                raise Exception(
                    'Found duplicate filename {} for file {}'.format(new, name)
                )

            new_filenames.add(new)
            files_mapping[name] = new

        for name, new in files_mapping.items():
            if os.path.exists(name):
                print('\n' + 'renaming ' + name)
                shutil.copyfile(name, new)
                
            else:
                print('\n' + name + " does not exist")


if __name__ == "__main__":
    rename_files(sys.argv[1])
