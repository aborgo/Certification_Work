"""
Counts the number of files with an arbitrary exstension.
"""

import glob

def counter():
    d = {}
    lst = glob.glob('*.*')
    for i in lst:
        file_parts = i.split('.')
        extension = file_parts[len(file_parts)-1]
        if not d.get(extension):
            d[extension] = 1
        else:
            d[extension] += 1
    return d
    
