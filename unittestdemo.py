import unittest
"""
Simple demo of unittest.
"""
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
    
    def test_1(self):
        "Verify creation of files is possible"
        for filename in ("this.txt", "that.txt", "the_other.txt"):
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        self.assertSetEqual(set(os.listdir()),{"this.txt", "that.txt", "the_other.txt"},"The files are different.")
    
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test_3(self):
        "Verify creation of binary file."
        f = open("binaryfile", "wb")
        f.write(b'1'*1000000)
        f.close()
        self.assertTrue(f.closed)
        self.assertEqual(os.stat("binaryfile").st_size,1000000,"File is not the correct size.")

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)

if __name__ == "__main__":
    unittest.main()
