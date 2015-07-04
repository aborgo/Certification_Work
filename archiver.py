"""
Created by Adam Borgo
"""
import os
import glob
import zipfile

def archiver(directory):
    """Archives the files in a given directory into an .zip file named
    [directory]_archive where the directory is located."""
    origdir = os.getcwd()
    _dir, _base = os.path.split(directory)
    os.chdir(_dir)
    file_list = glob.glob(os.path.join(directory,"*"))
    zf = zipfile.ZipFile("{0}_archive".format(_base),"w")
    for fn in file_list:
        filepath = os.path.join(directory, fn)
        if os.path.isfile(filepath):
            relpath = os.path.join(_base,os.path.basename(fn))
            zf.write(relpath)
    zf.close()
    os.chdir(origdir)
