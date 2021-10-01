import os
import shutil
from variables import *

# Make function to rewrite txt without blank space at the bottom
def rewrite(src, dest): # Returns: None
    with open(src, 'r') as f1:
        lines = f1.readlines()
        lines[-1] = lines[-1].replace('\n','')
    with open(dest, 'w') as f2:
        f2.writelines(lines)

# Exit/cancel the program once all files have been compiled
while True:
    for (root,dirs,fil) in os.walk(trans_dir, topdown=True):
        fil_list = fil
        for files in fil_list:
            # Check if the title has been found
            title_found = False
            # Get a file and find its pair, put their paths in a list
            file_id = files[0:14]  
            for files2 in fil_list:
                # Find the file's partner
                id2 = files2[0:14]
                if file_id == id2:
                    new_tup = [files,files2]
                    # Create a new folder with the temp as the name  
                    dir = os.path.join(path,trans_dir,'temp')
                    if not os.path.exists(dir):
                        os.mkdir(dir)
                    # Rename the files to 'eng' and 'jap'
                    for item in new_tup:
                        # Add the files to the new folder
                        if 'en' in item:
                            try:
                                # Look for the english translation out of the pair, get the title
                                # as the first line on the txt file
                                with open(trans_dir+"/"+item,'r',encoding='utf-8-sig') as f:
                                    lines = f.read() ##Read sample file
                                    title = lines.split('\n', 1)[0]
                                    # Replace the new folders name with the title
                                    try:
                                        os.rename(path+trans_dir+'/temp',path+trans_dir+'/'+title)
                                    except OSError:
                                        # Move the file in the new folder without the blank space
                                        rewrite(path+trans_dir+'/'+item,path+trans_dir+'/'+title+'/eng')
                                rewrite(path+trans_dir+'/'+item,path+trans_dir+'/temp/eng')
                            except FileNotFoundError:
                                continue
                        # Rename the japanese translation to jap and put it into the folder with its partner
                        elif 'ja' in item:
                            if title_found:
                                try:
                                    rewrite(path+trans_dir+'/'+item,path+trans_dir+'/'+title+'/jap')
                                except FileNotFoundError:
                                    continue
                            else:
                                try:
                                    rewrite(path+trans_dir+'/'+item,path+trans_dir+'/temp/jap')
                                except FileNotFoundError:
                                    continue

# If one folder is missing a pair, simply look for the file name that shares
# the same first 14 characters with it

