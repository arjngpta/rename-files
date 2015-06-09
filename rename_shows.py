# this program will rename TV Shows from the mkv to the mp4 file-name extension
# example: House_of_Cards_S01E01.mp4

import os

# remove spaces from file names
old_list = os.listdir(os.getcwd())
for old_name in old_list:
        file_name = old_name.replace(' ', '_')
        file_name = old_name.replace('-', '_')
        os.rename(old_name, file_name)

# identify file names to change
file_list = os.listdir(os.getcwd())
for file_name in file_list:
        file_title = os.path.splitext(file_name)[0]
        file_ext = os.path.splitext(file_name)[1]
        # thumbnail files should not be renamed
        if "Thumbs" in file_name:
                print ("ignored - thumbnail: "+ file_name)
        # double underscored files should not be renamed
        elif "__" in file_name:
                print ("ignored - underscored: "+ file_name)
        # dotted files should not be renamed
        elif file_name.startswith("."):
                print ("ignored - dotted: "+ file_name)
        # non-image files should not be renamed
        elif not (file_ext == ".mkv" or file_ext == ".MP4" or file_ext == ".MKV"):
                print ("ignored - not targeted: "+ file_name)
        # already renamed files should not be renamed
        elif ".mp4" in file_ext:
                print ("ignored - already changed: "+ file_name)
        # change qualifying files
        else:
                new_name = file_title + ".mp4"
                os.rename(file_name, new_name)
                print ("changed: "+ file_name +" to "+ new_name)

print "DONE!"





