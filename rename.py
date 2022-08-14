import re
import os
import shutil

#script também vai ler as sub-pastas
main_folder = r'C:\Users\lucas\Pictures\icons'


def file_loop(root, dirs, files):
    for file in files:
        print(file)

def main_loop():
    for root, dirs, files in os.walk(main_folder):
        file_loop(root, dirs, files)

if __name__ == '__main__':
    main_loop()