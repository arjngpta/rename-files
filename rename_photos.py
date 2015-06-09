# this program will rename photos to the following file-name format
# example: IMG_2015015_233016.jpg

import os
import pyexiv2
import datetime
i = 0

# remove spaces from file names
old_list = os.listdir(os.getcwd())
for old_name in old_list:
        file_name = old_name.replace(' ', '_')
        file_name = old_name.replace('-', '_')
        os.rename(old_name, file_name)

# identify file names to change
file_list = os.listdir(os.getcwd())
change_list = []
for file_name in file_list:
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
        elif not (file_ext == ".jpg" or file_ext == ".png" or file_ext == ".JPG" or file_ext == ".jpeg"):
                print ("ignored - not image: "+ file_name)
        # already renamed files should not be renamed
        elif "IMG_" in file_name:
                print ("ignored - already changed: "+ file_name)
        # add qualifying files to change_list
        else:
                change_list.append(file_name)

# define the new file name
for file_name in change_list:
        print ("defining: "+ file_name)
        meta_name = os.path.splitext(file_name)[0]
        file_ext = os.path.splitext(file_name)[1]
        metadata = pyexiv2.ImageMetadata(file_name)
        metadata.read()
        if "Exif.Photo.DateTimeOriginal" in metadata.exif_keys:
                tag = metadata['Exif.Photo.DateTimeOriginal']
                meta_name = tag.value.strftime('%Y%m%d_%H%M%S')
        elif "Exif.Image.DateTime" in metadata.exif_keys:
                tag = metadata['Exif.Image.DateTime']
                meta_name = tag.value.strftime('%Y%m%d_%H%M%S')
        else:
                print ("no meta-data: "+ file_name)
        new_name = "IMG_" + meta_name + file_ext
        # check for duplicates
        while new_name in file_list:
                i = i + 1
                print ("found - duplicate file: "+ new_name)
                new_name = "IMG_" + meta_name + "-" + str(i) + file_ext
        # rename the file
        os.rename(file_name, new_name)
        file_list = os.listdir(os.getcwd())
        print ("changed "+ file_name +" to "+ new_name)
        i = 0

print "DONE!"





