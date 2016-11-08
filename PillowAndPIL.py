from PIL import Image

img = Image.open("mecnun.jpg")

print(img.size) #Width & Height
print(img.format) #Extension JPEG

area = (100, 100, 250, 250) #Area to Crop X1,Y1,X2,Y2
cropped = img.crop(area) #Crop and Store in variable

cropped.show() #Opens Image as File with Default Program


