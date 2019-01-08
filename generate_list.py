import os

arr = os.listdir('C:\\Users\\Martin\\Documents\\Github\\robotickytabor.cz\\img\\2017')

f = open('C:\\Users\\Martin\\Documents\\Github\\robotickytabor.cz\\generated_list.txt', "w+")

for i in range (97):
  f.write("<li><a href=\"img/2017/%s\" data-imagelightbox=\"g\"><img src=\"thumb/2017/%s\" alt=\" \"/></a></li>\n" % (arr [i], arr [i]))

f.close()
