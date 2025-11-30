#Reading the source code of a webpage
import urllib.request

#store the url of the webpage in to an object
file = urllib.request.urlopen("https://www.python.org/")

#read data from file and display
print(file.read())
