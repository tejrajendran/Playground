# Program to rename files to reveal secret message

import os
def rename_files():
    # 1 - get files from folder
    file_list = os.listdir(r"/Users/212571508/Documents/Prank") # r -> raw path
    print(file_list)
    print("current working directory: " + os.getcwd());
    os.chdir(r"/Users/212571508/Documents/Prank");
    # 2 - for each file in folder - rename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None, "0123456789"))


rename_files()