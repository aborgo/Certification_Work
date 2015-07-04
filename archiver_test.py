import archiver
import unittest
import os
import tempfile
import shutil
import zipfile

class Archiver_test(unittest.TestCase):
    def setUp(self):
        self.dirname = tempfile.mkdtemp("_test_dir")
        self.filenames = ['test1.txt','test2.txt','test3.bin']
        self.subdirname = os.path.join(self.dirname,"_test_sub_dir")
        self.subfilenames = ['test4.txt','test5.py']
        self.archivename = "{0}_archive".format(self.dirname)
        for i in self.filenames:
            _dir = os.path.join(self.dirname,i)
            f = open(_dir,"w")
            f.close()
        os.mkdir(self.subdirname)
        for i in self.subfilenames:
            _dir = os.path.join(self.subdirname,i)
            f = open(_dir,"w")
            f.close()
    
    def test_archiver(self):
        """Tests if files are archived in the correct format
        and subdirectories"""
        archiver.archiver(self.dirname)
        expected = []
        for i in self.filenames:
            item = os.path.join(os.path.basename(self.dirname),i)
            item = item.replace('\\','/')
            expected.append(item)
        zf = zipfile.ZipFile(self.archivename)
        observed = zf.namelist()
        self.assertEqual(observed,expected,'oops!')
        
    
    def tearDown(self):
        shutil.rmtree(self.dirname)
        os.remove(self.archivename)

if __name__ == '__main__':
    unittest.main()
