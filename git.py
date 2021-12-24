import argparse
import os
import git
import sys

#print(os.listdir())
#print(os.path.basename())

parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
#print(args.file)
cwd = os.getcwd()
#os.chdir('new')


with open(args.file, 'r') as f:
    buf = f.readlines()
print(f"{os.path.basename(args.file)}  --> {buf}") 

#git.Repo.clone_from(buf,cwd)


for i in buf:
    clone = "git clone " + i
    print(clone)
    os.system(clone) # Cloning
#print(clone)  

#os.chdir(path) 
# #os.system(clone) # Cloning
