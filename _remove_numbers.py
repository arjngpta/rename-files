# this program is used to rename large numbers of files quickly

import os
def remove_numbers():
    # get file names from folder
    file_list = os.listdir(os.getcwd())
    # print(file_list)
    # rename each file
    for file_name in file_list:
        new_name = file_name.translate(None,"1234567890")
        os.rename(file_name, new_name)
remove_numbers()
print "DONE!"
