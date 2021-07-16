import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "j8rgpm",
        "typeId": "Assignment2",
        "deviceId":"123456"
    },
    "auth": {
        "token": "123456789"
    }
}

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    level=random.randint(0,125) 
    intensity=random.randint(0,100)
    myData={'Water_Level':level, 'Light_Intensity':intensity}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)    
    time.sleep(5)
    
client.disconnect()
