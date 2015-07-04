import unittest
import mysql.connector
from database import login_info
from classfactory import build_row

class DBTest(unittest.TestCase):

    def test_retrieve_data_row_objects(self):
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        table = 'animal'
        cols = 'id name family weight'
        D = build_row(table, cols)
        sql = 'SELECT * FROM animal;'
        cursor.execute(sql)
        expected_rows = set()
        for row in cursor.fetchall():
            expected_rows.add(repr(D(row)))

        d = D([100, "Joe", "Python", 10])
        observed_rows = set()
        for row in d.retrieve(cursor):
            observed_rows.add(repr(row))

        self.assertEqual(observed_rows, expected_rows)

    def test_retrieve_data_row_objects_with_conditions(self):
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        table = 'animal'
        cols = 'id name family weight'
        D = build_row(table, cols)
        sql = 'SELECT * FROM animal WHERE weight>40 AND weight<600;'
        cursor.execute(sql)
        expected_rows = set()
        for row in cursor.fetchall():
            expected_rows.add(repr(D(row)))

        d = D([100, "Joe", "Python", 10])  
        observed_rows = set()
        for row in d.retrieve(cursor, ["weight>40","weight<600"]):
            observed_rows.add(repr(row))

        self.assertEqual(observed_rows, expected_rows)
    
        
if __name__ == '__main__':
    unittest.main()
