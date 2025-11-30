import urllib.request

try:
    # Store the url of the webpage into an object
    file = urllib.request.urlopen("https://www.python.org/")  
    # Read data from file and store content into a variable
    content = file.read()  

    # Open a file for writing
    f = open('myfile.html', 'wb')

    # Write content into the file
    f.write(content)

    # Close the file
    f.close()

except urllib.error.HTTPError:
    print('The webpage is not found')
    exit()