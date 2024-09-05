import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime 
import tkinter as tk
import time
import pywhatkit

phn={ 
    "ROMIL":"+919930192991",
}
nname=[]
def activate():
    a=entry1.get()
    print("Roll NO:",a)
    call1(a)
def sendmsg(a):
    for x in a:
        for z,y in phn.items():  
            if z==x:         
                now=datetime.now()
                pywhatkit.sendwhatmsg(y,"{} Was Present".format(x),now.hour,now.minute+2)
                # pywhatkit.sendwhatmsg_to_group_instantly("Aandh Bhaat","ss")

win=tk.Tk()
win.geometry("800x500")
win.title("Attendance System")
label1=tk.Label(win,text="Attendance System")
label1.pack()
entry1=tk.Entry(win)
entry1.pack()
button1=tk.Button(win,text="Click For Attendance",command=activate)
button1.pack()
textt=tk.Text(win)
textt.pack()



path = 'imageattendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
 
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        # encode = face_recognition.face_encodings(img)[1]
        encodeList.append(encode)
    return encodeList
 
def markAttendance(a,name):
    with open('attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'{a} : {name} : {dtString}')
            textt.insert(tk.END,f'{a} : {name} : {dtString}'+"\n")
        
        nname.append(name)
    return True

encodeListKnown = findEncodings(images)

 


def call1(a):
    cap = cv2.VideoCapture(0)
    while True:
        s=False
        success, img = cap.read()
        #img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
        me = face_recognition.face_encodings(imgS,facesCurFrame)
    
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)
    
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                s=markAttendance(a,name)

        cv2.imshow('Webcam',img)
        if cv2.waitKey(1) and 0xFF==ord('A'):
            break
        if s:
            print(f"{a} is present")
            cap.release()
            time.sleep(5)
            cv2.destroyAllWindows()
            
            break
        cv2.waitKey(1)
      
win.mainloop()
print(nname)
sendmsg(nname) 
