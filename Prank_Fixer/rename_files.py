import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"/Users/PriteshJ/Documents/Udacity/ProgrammingFoundationsWithPython/Prank_Fixer/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"/Users/PriteshJ/Documents/Udacity/ProgrammingFoundationsWithPython/Prank_Fixer/prank")    
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        to_remove = "0123456789"
        table = str.maketrans("", "", to_remove)
        os.rename(file_name, file_name.translate(table))
    os.chdir(saved_path)
rename_files()  
