import os, subprocess
from platform import system
files_cpp, file, cls = [], "", 0 #set to 1 for clear screen
command = ["g++", "-S"]
if system() == "Windows":
    cls_cmd = "cls"
else:
    cls_cmd = "clear"  #  for Linux/MacOS

def get_files():
    global files_cpp
    cwd = os.getcwd()
    files = os.listdir(cwd)
    files_cpp = [i for i in files if i.lower().endswith('.cpp')]

def show_files():
    print("Identified following .cpp file(s):")
    for i in range(len(files_cpp)):
        print(i, files_cpp[i])

def clear_screen():
    os.system(cls_cmd)
    
def compile():
    if cls:
        clear_screen()
    try:
        subprocess.run([*command, file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
    except subprocess.CalledProcessError as suberror:
        print(suberror.stdout.decode("utf-8"))
    else:
        print(f"Successfully compiled!")
        #Running {file[:-2]}.exe...\n")
        #exit_code = subprocess.run(file[:-2]).returncode
        #print(f"\n-----------------------------------\nProcess terminated with exit code {exit_code}") 

while True:
    get_files()
    if files_cpp:
        show_files()
        if len(files_cpp) == 1:
        	file = files_cpp[0]
        while True:
            if file:
                cmd = input(f"\nENTER to compile {file} or input index of .cpp file: ")
            else:
                cmd = input("\nEnter index of .cpp file: ")
            if not cmd:
            	compile()
            elif cmd.isnumeric() and int(cmd) in range(len(files_cpp)):
                file = files_cpp[int(cmd)]
                compile()
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
        input("No .cpp files found. Press ENTER to try again...")
