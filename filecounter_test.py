import counter
import unittest
import os
import tempfile
import shutil

PATHSTEM = "v:\\workspace\\FileHandling_Homework\\src\\"


class TestCounter(unittest.TestCase):
    """Test case to verify functionality of a function that counts the number
    of files that have each extension.
    """
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        self.file_names = [
                           'file.txt','file.py','file.doc','file.bin',
                           'file2.txt','file2.bin','file3.txt','file.file.py'
                           ]
        
    def base_test(self,lst,expected):
        for fn in lst:
            f = open(fn, 'w')
            f.close()
        self.assertEqual(counter.counter(),expected, 
                         'Did not match expected file count.')
            
    def test_single_file(self):
        "Verify the ability to count files by way of  their extensions."
        TestCounter.base_test(self,self.file_names[0:1],{'txt':1})
    
    def test_multiple_files1(self):
        "Verify the ability to count multiple extensions."
        TestCounter.base_test(self,self.file_names[0:4],
                              {'txt':1, 'py':1, 'doc':1, 'bin':1,}
                              )
    
    def test_multiple_files2(self):
        "Verify the ability to count multiple files with multiple extensions"
        TestCounter.base_test(self,self.file_names[0:7],
                              {'txt':3, 'py':1, 'doc':1, 'bin':2,}
                              )
        
    def test_handling_extension_format(self):
        """Verify the ability to handle file names that include 
        additional '.' characters.
        """
        TestCounter.base_test(self,self.file_names[7:8],{'py':1}
                              )
    
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)


if __name__ == '__main__':
    unittest.main()
