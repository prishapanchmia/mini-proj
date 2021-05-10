
# import module
from pdf2image import convert_from_path
import pytesseract
from PIL import Image 
import os
poppler_path = r'C:\Users\parab\Desktop\python\Firstdjan\MPR\mpr\src\mini-proj\poppler-0.68.0\bin'
# Store Pdf with convert_from_path function

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def check(filename1):
	filename1 = os.path.join(r'C:\Users\parab\Desktop\python\Firstdjan\MPR\mpr\src\mini-proj\media_root\uploads',filename1)
	images = convert_from_path(filename1,poppler_path = poppler_path) 
	for i in range(len(images)):
	    detect = 0
	      # Save pages as images in the pdf
	    filename = "page0.jpg"
	    images[i].save(filename, 'JPEG')
	    
	    text = pytesseract.image_to_string(Image.open(filename))
	    if text.find('DETECTED') != -1:
	    	detect = 1
	    	print('yes')
	    else:
	    	print("no")

	    os.remove(filename)
	    if detect == 1:
	    	break
	if detect == 1:
		return True
	else:
		return False