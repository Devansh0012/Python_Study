file = open('youtube.txt','w')

try:
    file.write('Hello World')
    
finally:
    file.close()
    
# The above code is a simple example of error handling in Python. The code opens a file in write mode, writes a string to it, and then closes the file. If an error occurs while writing to the file, the file will still be closed properly. The finally block ensures that the file is closed even if an error occurs. This is important because failing to close a file can lead to data loss or corruption.

with open('youtube.txt','w') as file:
    file.write('Hello World !')
    
# The above code is a more concise way to open a file in Python. The with statement automatically closes the file when the block of code is finished, so there is no need for a separate finally block. This is a common pattern in Python for working with files, as it ensures that files are always closed properly, even if an error occurs.