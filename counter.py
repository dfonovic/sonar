import os, subprocess
from platform import system
files_s, file, cls = [], "", 0 #set to 1 for clear screen
command = ["wc", "-l","./counter.csv"]

if system() == "Windows":
    cls_cmd = "cls"
else:
    cls_cmd = "clear"  #  for Linux/MacOS

def get_files():
    global files_s
    cwd = os.getcwd()
    files = os.listdir(cwd)
    files_s = [i for i in files if i.lower().endswith('.s')]

def show_files():
    print("Identified following .s assembler file(s):")
    for i in range(len(files_s)):
        print(i, files_s[i])

def clear_screen():
    os.system(cls_cmd)

def simplecount():
    lines = 0
    for line in open(file):
        lines += 1
    print(f"Number of lines: {lines}")
    try:
        subprocess.run([*command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    except subprocess.CalledProcessError as suberror:
        print(suberror.stdout.decode("utf-8"))
    else:
        print(f"Successfully appended to csv file!")

    

    

while True:
    get_files()
    if files_s:
        show_files()
        if len(files_s) == 1:
        	file = files_s[0]
        while True:
            if file:
                cmd = input(f"\nENTER to compile {file} or input index of .s file: ")
            else:
                cmd = input("\nEnter index of .s file: ")
            if not cmd:
            	simplecount()
            elif cmd.isnumeric() and int(cmd) in range(len(files_s)):
                file = files_s[int(cmd)]
                simplecount()
            elif cmd == "f": #refresh list of files
            	get_files()
            	show_files()
            elif cmd == "c":
                clear_screen()
            elif cmd == "q":
            	exit()
            else:
                print("Invalid input")	
    else:
        input("No .s files found. Press ENTER to try again...")

