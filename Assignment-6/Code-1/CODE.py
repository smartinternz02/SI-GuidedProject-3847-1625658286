import cv2
import numpy as np
thres = 0.45 # Threshold to detect object
nms_threshold = 0.2
cap = cv2.VideoCapture(0)
cap.set(3,1280)


configPath = cv2.CascadeClassifier("haarcascade_objectdetection.xml")
weightsPath = cv2.CascadeClassifier("haarcascade_allobjects.xml")

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    bbox = list(bbox)
    confs = list(np.array(confs).reshape(1,-1)[0])
    confs = list(map(float,confs))    
    print(confs)
    indices = cv2.dnn.NMSBoxes(bbox,confs,thres,nms_threshold)
    print(indices)

    for i in indices:
        i = i[0]
        box = bbox[i]
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(img, (x,y),(x+w,h+y), color=(0, 255, 0), thickness=2)
        cv2.putText(img, 'Object Detected', (x,y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 4)
        

    cv2.imshow("Output",img)
    Key=cv2.waitKey(1)
    if Key==ord('q'):
        #release the camera
        cap.release()
        #destroy all windows
        cv2.destroyAllWindows()
        break
