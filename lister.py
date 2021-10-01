import os
from variables import *

# List the names of all the gathered documents
titles=[]

for (root,dirs,fil) in os.walk(trans_dir, topdown=True):
    dirs_list = dirs
    title=root[len(trans_dir)+1:]
    if len(os.listdir(root)) >= 2:
        titles.append(title)

# Write the list of compiled documents into a txt file
with open('list_of_documents.txt', 'w') as f:
    for t in titles:
        f.write(t)
        f.write('\n')
