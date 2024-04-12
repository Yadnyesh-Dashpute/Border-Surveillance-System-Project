import numpy as np
import cv2
import time
import os
import tkinter as tk
from tkinter import messagebox

def exit_application():
    msg_box = tk.messagebox.askquestion('Exit Application', 'Are You Sure You Want To Send Alert!',
                                        icon='warning')
    if msg_box == 'yes':
        root.destroy()
        cap.release()
        cv2.destroyAllWindows()
        os.system("start wmplayer c:\\project\\siren.wav")          
        os.system("C:\Windows\System32\cmd.exe /c C:\\project\\sendemail.bat")               
        exit(0)
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')
        root.destroy()
        cap.release()
        cv2.destroyAllWindows()
        os.system("C:\Windows\System32\cmd.exe /c python C:\\project\\main.py")               
        exit(0)

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

Sec = 0
Min = 0
Check = 1
Counter = 1

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #if ret is True:
     #           gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #else:
    #    continue
    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    faces = eye_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)     

    if len(faces) > 0:  

        Sec += 1
        print(str(Min) + " Mins " + str(Sec) + " Sec ")

        cv2.putText(img, "Time: " + str(Min) + " Mins " + str(Sec) + " Sec ", (0,img.shape[0] -30), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,255), 1)
        #cv2.putText(img, "Number of Intruder Detected: " + str(faces.shape[0]), (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,255), 1)    

        time.sleep(1)
        if Sec == 3 and len(faces) >= 1:
            Sec = 0
            Min += 1
            print(str(Min) + " Minute")
            cv2.putText(img, "Time: " + str(Min) + " Mins " + str(Sec) + " Sec ", (0,img.shape[0] -30), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,255), 1)
            cv2.imwrite("snap.png",img);
            button1 = tk.Button(root, text='Alert Received. Press Button to Start/Stop Buzzer', command=exit_application, bg='brown', fg='white')
            canvas1.create_window(100, 100, window=button1)
            root.mainloop()
            Counter += 1

        if Min == 2:
            print("Alert")
            if Check == 1:
#                import http.client
#                conn = http.client.HTTPConnection("api.msg91.com")
#                payload = "{ \"sender\": \"ATMAUT\", \"route\": \"4\", \"country\": \"91\", \"sms\": [ { \"message\": \"Suspicious activity detected inside ATM.\", \"to\": [ \"9677104366\"] } ] }"
#                headers = {'authkey': "209349Aqh8iTXUN1Of5accca05",'content-type': "application/json"}
#                conn.request("POST", "/api/v2/sendsms", payload, headers)
#                res = conn.getresponse()
#                data = res.read()
#                print(data.decode("utf-8"))
                 #cv2.imwrite("snap.png",img);
                 #os.system("C:\Windows\System32\cmd.exe /c C:\\project\\sendemail.bat")
                 #p = Popen("sendemail.bat", cwd=r"C:\\project\\")                 
                 Check += 1   



                   
    if len(faces) == 0:

        print('No Intruder Detected')
        cv2.putText(img, "No face detected ", (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,255), 1)        
        Sec = 0
        Min = 0

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break    

cap.release()
cv2.destroyAllWindows()
