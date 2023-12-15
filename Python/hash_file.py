
import hashlib 

def hashing (name_of_file):

              h = hashlib.sha1 ()

              with open (name_of_file, ‘rb’) as file:

                             piece = 0

                             while chunk != b ‘ ‘:

                                            piece = file.read (1024)

                                            h.update (piece)

              return h.hexdigest ()

output1 = hashing (“image1.jpg”)

print (output1)
