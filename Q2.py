from PIL import Image
# replace "Image.jpg" with the place where you have downloaded the image
photo = Image.open(r"Image.jpg") # reading the photo

photo = photo.save("photo.jpg") # saving the photo
