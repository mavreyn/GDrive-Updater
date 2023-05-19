'''
This script will find the google drive exe shortcut from windows start menu and run it
Will work even if the folder housing the original exe changes names
Then I use task scheduler on this file

Maverick Reynolds
04.08.2023

'''

import os
import re

# This is probably the simplest solution, path to this file never changes
os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google Drive')


'''
ALTERNATE SOLUTION POSSIBLY

# Can get to here just fine
path = 'C:/Program Files/Google/Drive File Stream/'

files = os.listdir(path)
# Need to find the folder XX.A.BB.C
for file in files:
    # If file/dir name consists of only numbers and periods, it is found
    if re.match('^[\d.]+$', file):
        path += file + '/'
        break

path += 'GoogleDriveFS.exe'

os.startfile(path)
'''
