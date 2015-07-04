import unittest
from settings import RECIPIENTS, DAYCOUNT
from database import login_info
import mysql.connector as msc
import client
import datetime

conn = msc.Connect(**login_info)
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE if not exists jotd_emails (
     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgMessageID VARCHAR(128),
     msgDate DATETIME,
     msgReceiverAddress VARCHAR(128),
     msgSenderAddress VARCHAR(128),
     msgText LONGTEXT
)"""

class test_client(unittest.TestCase):
    def setUp(self):
        "Provides each test with a freshly populated table"
        curs.execute("DROP TABLE jotd_emails")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()
        client.run()
        
    def test_table(self):
        "Tests that the appropriate number of emails have been created and stored"
        curs.execute("SELECT * FROM jotd_emails")
        observed = len(curs.fetchall())
        expected = DAYCOUNT * len(RECIPIENTS)
        self.assertEqual(observed, expected)
        
    def test_date(self):
        "Tests if each e-mail properly increments the date it will be sent"
        curs.execute("SELECT msgDate FROM jotd_emails")
        date_lst = []
        for i in curs.fetchall():
            time = i[0]
            date_lst.append(time)
        for i in range(len(RECIPIENTS)):
            offset = i * DAYCOUNT
            for v in range(DAYCOUNT-1):
                observed = date_lst[v+1+offset]-date_lst[v+offset]
                self.assertEqual(observed, datetime.timedelta(1))
        
        
        


if __name__ == "__main__":
    unittest.main()
