import cv2
import datetime

f_1=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
f_2=cv2.CascadeClassifier("haarcascade_eye.xml")
f_3=cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
f_4=cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
f_5=cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
f_6=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
f_7=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
f_8=cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")
f_9=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
f_10=cv2.CascadeClassifier("haarcascade_fullbody.xml")
f_11=cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
f_12=cv2.CascadeClassifier("haarcascade_licence_plate_rus_16stages.xml")
f_13=cv2.CascadeClassifier("haarcascade_lowerbody.xml")
f_14=cv2.CascadeClassifier("haarcascade_profileface.xml")
f_15=cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")
f_16=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
f_17=cv2.CascadeClassifier("haarcascade_smile.xml")
f_18=cv2.CascadeClassifier("haarcascade_lowerbody.xml")
f_19=cv2.CascadeClassifier("haarcascade_upperbody.xml")

            
                                           

video=cv2.VideoCapture(0)

while True:
    #capture the first frame
    check,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    #detect the faces from the video using detectMultiScale function
    a_1=f_1.detectMultiScale(gray,1.3,5)
    a_2=f_2.detectMultiScale(gray,1.3,5)
    a_3=f_3.detectMultiScale(gray,1.3,5)
    a_3=f_3.detectMultiScale(gray,1.3,5)
    a_4=f_4.detectMultiScale(gray,1.3,5)
    a_5=f_5.detectMultiScale(gray,1.3,5)
    a_6=f_6.detectMultiScale(gray,1.3,5)
    a_7=f_7.detectMultiScale(gray,1.3,5)
    a_8=f_8.detectMultiScale(gray,1.3,5)
    a_9=f_9.detectMultiScale(gray,1.3,5)
    a_10=f_10.detectMultiScale(gray,1.3,5)
    a_11=f_11.detectMultiScale(gray,1.3,5)
    a_12=f_12.detectMultiScale(gray,1.3,5)
    a_13=f_13.detectMultiScale(gray,1.3,5)
    a_14=f_14.detectMultiScale(gray,1.3,5)
    a_15=f_15.detectMultiScale(gray,1.3,5)
    a_16=f_16.detectMultiScale(gray,1.3,5)
    a_17=f_17.detectMultiScale(gray,1.3,5)
    a_18=f_18.detectMultiScale(gray,1.3,5)
    a_19=f_19.detectMultiScale(gray,1.3,5)
    
    
    
    for(x,y,w,h) in a_1:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)        
        cv2.imshow('OBJECT DETECTION', frame)
        
    
    for(x,y,w,h) in a_2:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)
        cv2.imshow('OBJECT DETECTION', frame)

    for(x,y,w,h) in a_3:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)        
        cv2.imshow('OBJECT DETECTION', frame)
        
        
    
    for(x,y,w,h) in a_4:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)
        cv2.imshow('OBJECT DETECTION', frame)

    for(x,y,w,h) in a_5:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)        
        cv2.imshow('OBJECT DETECTION', frame)
        
    
    for(x,y,w,h) in a_6:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)
        cv2.imshow('OBJECT DETECTION', frame)

    for(x,y,w,h) in a_7:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)        
        cv2.imshow('OBJECT DETECTION', frame)
        
    
    for(x,y,w,h) in a_8:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)
        cv2.imshow('OBJECT DETECTION', frame)

    for(x,y,w,h) in a_9:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)        
        cv2.imshow('OBJECT DETECTION', frame)
        
    
    for(x,y,w,h) in a_10:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)
        cv2.imshow('OBJECT DETECTION', frame)

    for(x,y,w,h) in a_11:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)        
        cv2.imshow('OBJECT DETECTION', frame)
        
    
    for(x,y,w,h) in a_12:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)

    for(x,y,w,h) in a_13:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)        
        cv2.imshow('OBJECT DETECTION', frame)
        
    
    for(x,y,w,h) in a_14:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)
        cv2.imshow('OBJECT DETECTION', frame)

    for(x,y,w,h) in a_15:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)        
        cv2.imshow('OBJECT DETECTION', frame)
        
    
    for(x,y,w,h) in a_16:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)
        cv2.imshow('OBJECT DETECTION', frame)

    for(x,y,w,h) in a_17:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)        
        cv2.imshow('OBJECT DETECTION', frame)
        
    
    for(x,y,w,h) in a_18:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)
        cv2.imshow('OBJECT DETECTION', frame)

    for(x,y,w,h) in a_19:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)        
        cv2.imshow('OBJECT DETECTION', frame)

    #waitKey(1)- for every 1 millisecond new frame will be captured
    Key=cv2.waitKey(1)
    if Key==ord('q'):
        #release the camera
        video.release()
        #destroy all windows
        cv2.destroyAllWindows()
        break

