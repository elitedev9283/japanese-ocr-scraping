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

found = []

# Exit/cancel the program once all files have been compiled
while True:
    for (root,dirs,fil) in os.walk(trans_dir, topdown=True):
        fil_list = fil
        for files in fil_list:
            if files in found:
                continue
            # Check if the title has been found
            title_found = False
            # Get a file and find its pair, put their paths in a list
            file_id = str(files.replace('en','')).replace('ja','')
            for files2 in fil_list:
                if files == files2:
                    continue
                # Find the file's partner
                id2 = str(files2.replace('en','')).replace('ja','')
                if file_id == id2:
                    found.append(files)
                    found.append(files2)
                    print(files, files2)
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
                                    title_found = True
                                # Replace the new folders name with the title
                                os.rename(path+trans_dir+'/temp',path+trans_dir+'/'+title)
                                rewrite(path+trans_dir+'/'+item,path+trans_dir+'/'+title+'/english')
                            except FileNotFoundError:
                                continue
                        # Rename the japanese translation to jap and put it into the folder with its partner
                        elif 'ja' in item:
                            if title_found:
                                try:
                                    rewrite(path+trans_dir+'/'+item,path+trans_dir+'/'+title+'/japanese')
                                except FileNotFoundError:
                                    continue
                            else:
                                try:
                                    rewrite(path+trans_dir+'/'+item,path+trans_dir+'/temp/japanese')
                                except FileNotFoundError:
                                    continue


