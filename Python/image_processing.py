from PIL import Image, ImageFilter

# Load image
image = Image.open('image.jpg') 

# Apply sharpen filter
sharp = image.filter(ImageFilter.SHARPEN)
sharp.save('image_sharpen.jpg')

# Make image grayscale
gray = image.convert('L')
gray.save('image_gray.jpg')

# Rotate image 45 degrees
rotate = image.rotate(45)
rotate.save('image_rotate.jpg') 

# Resize image to 128x128
resize = image.resize((128,128))
resize.save('image_resize.jpg')

# Crop image 
box = (100, 100, 400, 400)
crop = image.crop(box)
crop.save('image_crop.jpg')
