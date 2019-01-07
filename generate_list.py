import os

arr = os.listdir('C:\\Users\\Martin\\Documents\\Github\\robotickytabor.cz\\img\\2018')

f = open('C:\\Users\\Martin\\Documents\\Github\\robotickytabor.cz\\generated_list.txt', "w+")

for i in range (72):
  f.write("<li><a href=\"img/2018/%s\" data-imagelightbox=\"g\"><img src=\"thumb/2018/%s\" alt=\" \"/></a></li>\n" % (arr [i], arr [i]))

f.close()
