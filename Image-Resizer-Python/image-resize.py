from PIL import Image
img=Image.open('logo.png')#input file name
w=42 #custom width here
h=42 #custom height here
img=img.resize((w,h),Image.ANTIALIAS)
img.save('output.png') #output file name
print 'OK'
