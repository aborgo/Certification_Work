"""
Formats and returns a multipart e-mail.
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import mimetypes

def formatter(adress,body,attach=[]):
    """
    Creates a MIME object and attaches MIMtypes to it.
    """
    msg = MIMEMultipart()
    txt = MIMEText(body,'plain')
    txt['To'] = adress
    msg.attach(txt)
    for fn in attach:
        _type = mimetypes.guess_type(fn)
        if _type[0][0:5] == 'image':
            with open(fn,'rb') as fp:
                img = MIMEImage(fp.read())
                fp.close()
                msg.attach(img)
        if _type[0][0:4] == "text":
            with open(fn,'r') as fp:
                txt = MIMEText(fp.read())
                fp.close()
                msg.attach(txt)
                
    return msg
    
    
if __name__ == '__main__':
    msg = formatter('test@thing.org',"The body of the message",
                    ['v:/workspace/HandlingEmail_Homework/src/python-logo.png',
                     'v:/workspace/HandlingEmail_Homework/src/test1.txt'])
    print(msg)
