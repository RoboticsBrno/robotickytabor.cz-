import os

arr = os.listdir('C:\\Users\\Martin\\Documents\\Github\\robotickytabor.cz\\img\\2019')

f = open('C:\\Users\\Martin\\Documents\\Github\\robotickytabor.cz\\generated_list.txt', "w+")

for i in range (105):
  f.write("<li><a href=\"img/2019/%s\" data-imagelightbox=\"h\"><img src=\"thumb/2019/%s\" alt=\" \"/></a></li>\n" % (arr [i], arr [i]))

f.close()
