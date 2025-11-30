#To find different parts of the URL and display them
import urllib.parse
#Take any URL
url='https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar'

#get a tuple with parts of the URL
tpl=urllib.parse.urlparse(url)

#Display the contents   of the tuple
print(tpl)

#Display different parts of the URL

print("Scheme:",tpl.scheme)
print("Netloc:",tpl.netloc)
print("Path:",tpl.path)
print("Params:",tpl.params)
print('Port number:',tpl.port)
print('Total URL:',tpl.geturl())
