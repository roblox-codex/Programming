
def res_image (filename):

              with open (filename, ‘rb’) as file_image:

                             file_image.seek (163)

                             a = file_image.read (2)

                             height = (a [0] << 8) + a [1]

                             a = file_image.read (2)

                             width = (a [0] << 8) + a [1]

              print (“The resolution of the given image is:”, width, “x”, height)

res_image (“image1.jpeg”)
