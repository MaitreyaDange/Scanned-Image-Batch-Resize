import os
from PIL import Image

# Paste the path of the directory containing files
IN_PATH = 'C:\\Users\\Maitreya Dange\\Documents\\Coding\\Python Projects\\Scanned Image Batch Resize\\input\\'
OUT_PATH = 'C:\\Users\\Maitreya Dange\\Documents\\Coding\\Python Projects\\Scanned Image Batch Resize\\output\\'

files = os.listdir(IN_PATH)

def main():
    resize_image()

def rename_file() :
    for file in files :
        os.rename(os.path.join(OUT_PATH, file), os.path.join(OUT_PATH, file[:len(file)-4] +  ' renamed.png'))

def resize_image():
    for file in files :
        if os.path.isfile(IN_PATH+file) :
            im = Image.open(IN_PATH+file)
            im = im.resize((int(im.size[0]/10),int(im.size[1]/10)), Image.LANCZOS)
            im.save( OUT_PATH+file[:len(file)-4] + ' resized.jpg', 'JPEG')
  
# Driver Code 
if __name__ == '__main__': 
    main() 