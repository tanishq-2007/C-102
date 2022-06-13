from os import access
import cv2
import dropbox
import time
import random

from numpy import number

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name='img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    return img_name
    print('snapshot taken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token='sl.BJecKBhLidswRJV-dF6N-bZ4vuW0X128sktDpaJB5FE3rhIt4SaxkI8OHGlo_GoDKBryIkdcydbA3uYSyyiO7yP_r1qJ-G0T6FHhDkW9CI4Wde7ahpOrfK55n1VER3XnRUxm5gw'
    file=img_name
    file_from=file
    file_to='/newFolder1'+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('File Uploaded')

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)

main()

