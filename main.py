import os
# Classes for Image Procession
from PIL import Image
from PIL import ImageEnhance
# Progress Bar in cmd
from tqdm import tqdm
# Windows 10 Toast Notification
from win10toast import ToastNotifier
#choose file or directory
import tkinter as tk
from tkinter.filedialog import askdirectory

# Paste the path of the directory containing files
# IN_PATH = 'C:/Users/Maitreya Dange/Documents/Coding/Python Projects/Scanned Image Batch Resize/input/'
try :
    IN_PATH = askdirectory(title = 'Select Folder')
except :
    IN_PATH = 'C:/Users/Maitreya Dange/Pictures/Scans'
    
# DecompressionBombing Error Suppression :
Image.MAX_IMAGE_PIXELS = 180000000
# Set Parameters
# Resize Factor < 1 
RESIZE_FACTOR = 1/2
# Contrast
CONTRAST = 1.5

files = os.listdir(IN_PATH)
toaster = ToastNotifier()

if not os.path.exists(IN_PATH + '/Processed') :
    os.mkdir(IN_PATH + '/Processed')
    os.mkdir(IN_PATH + '/Processed/JPG')
    os.mkdir(IN_PATH + '/Processed/PDF')


def main():
    resize_image()

def resize_image():
    with tqdm(total = len(files), unit='Image') as pbar :
        for file in files :
            if os.path.isfile(IN_PATH+'/'+file) :
                im = Image.open(IN_PATH+'/'+file)
                enh_im = ImageEnhance.Contrast(im)
                im = enh_im.enhance(CONTRAST)
                im = im.resize((int(im.size[0]*RESIZE_FACTOR),int(im.size[1]*RESIZE_FACTOR)), Image.LANCZOS)
                im = im.convert("RGB")
                im.save( IN_PATH+'/Processed/JPG/'+file[:len(file)-4] + ' [ processed ].pdf', 'PDF', resolution = 300)
                im.save( IN_PATH+'/Processed/PDF/'+file[:len(file)-4] + ' [ processed ].jpg', 'JPEG')
                pbar.set_postfix(Image = file)
            
            pbar.update(1)
        pbar.close()
        toaster.show_toast("Scanned Image Batch Resize", "Queue Processed", duration=20)   
  
# Driver Code 
if __name__ == '__main__': 
    main() 