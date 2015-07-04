"""
Created by Adam Borgo
Emulates an email client.
"""
from settings import RECIPIENTS, STARTTIME, DAYCOUNT
from email.message import Message
from email.utils import make_msgid
import datetime
from database import login_info
import mysql.connector as msc
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

curs.execute(TBLDEF)
conn.commit()

def store(msg):
    """
    Stores an email message.
    """ 
    date = msg['Date']
    _from = msg['From']
    to = msg['To']
    message_id = msg['Message-Id']
    text = msg.as_string()
    curs.execute("SELECT msgID FROM jotd_emails WHERE msgMessageID=%s", (message_id, ))
    result = curs.fetchone()
    if result:
        return None
    curs.execute("INSERT INTO jotd_emails (msgMessageID, msgDate, msgReceiverAddress, msgSenderAddress, msgText) VALUES (%s, %s, %s, %s, %s)",
             (message_id, date, to, _from, text))
    conn.commit()

def run():
    msg_lst = []
    for name,address in RECIPIENTS:
        date = STARTTIME
        for day in range(DAYCOUNT):
            msg = Message()
            msg['Date'] = str(date)
            msg['From'] = 'Me'
            msg['To'] = address
            msg['Message-Id'] = make_msgid()
            msg.set_payload('message {}'.format(day+1))
            msg_lst.append(msg)
            date = date + datetime.timedelta(1)
    for msg in msg_lst:
        store(msg)
            


if __name__ == "__main__":
    import timeit
    lst = [1,10,50,100,500]
    for i in lst:
        DAYCOUNT = i
        print(timeit.timeit("run()", "from __main__ import run", number = 1))
