import os
from PIL import Image
from PIL import ImageEnhance
from tqdm import tqdm

# Paste the path of the directory containing files
IN_PATH = 'C:\\Users\\Maitreya Dange\\Documents\\Coding\\Python Projects\\Scanned Image Batch Resize\\input\\'
OUT_PATH = 'C:\\Users\\Maitreya Dange\\Documents\\Coding\\Python Projects\\Scanned Image Batch Resize\\output\\'
# DecompressionBombing Error Suppression :
Image.MAX_IMAGE_PIXELS = 180000000

# Set Parameters
# Resize Factor < 1
RESIZE_FACTOR = 1/6

# Contrast
CONTRAST = 1.5

files = os.listdir(IN_PATH)

def main():
    resize_image()

def rename_file() :
    for file in files :
        os.rename(os.path.join(OUT_PATH, file), os.path.join(OUT_PATH, file[:len(file)-4] +  ' renamed.png'))

def resize_image():
    with tqdm(total = len(files)) as pbar :
        for file in files :
            if os.path.isfile(IN_PATH+file) :
                im = Image.open(IN_PATH+file)
                enh_im = ImageEnhance.Contrast(im)
                im = enh_im.enhance(CONTRAST)
                im = im.resize((int(im.size[0]*RESIZE_FACTOR),int(im.size[1]*RESIZE_FACTOR)), Image.LANCZOS)
                im = im.convert("RGB")
                im.save( OUT_PATH+file[:len(file)-4] + ' resized.jpg', 'JPEG')
            pbar.update(1)
        pbar.close()   
  
# Driver Code 
if __name__ == '__main__': 
    main() 