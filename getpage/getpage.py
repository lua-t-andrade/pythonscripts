#! usr/bin/python3
# This will download a page

import requests, sys
import time

startTime = time.time()

try:
    page_to_download = sys.argv[1]
except IndexError:
    print("Error: you need to input a web page.")
    exit()

try:
    requested_page = requests.get(page_to_download)
    requested_page.raise_for_status()
except Exception as error2:
    print("Uh-oh! %s" %(error2))

file_to_save = open("requestedpage.html", "wb")
for chunk in requested_page.iter_content(100000):
    file_to_save.write(chunk)

file_to_save.close()

endTime = time.time()

print("Program ran successfully, took only %s seconds" %(endTime - startTime))

