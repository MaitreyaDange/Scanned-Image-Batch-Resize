import os

# Paste the path of the directory containing files
PATH = 'C:\\Users\\Maitreya Dange\\Documents\\Coding\\Python Projects\\Batch Rename\\input'

files = os.listdir(PATH)

def main():
    rename_file()


def rename_file() :
    for file in files :
        os.rename(os.path.join(PATH, file), os.path.join(PATH, file[:len(file)-4] +  ' renamed.png'))
  
# Driver Code 
if __name__ == '__main__': 
    
    main() 