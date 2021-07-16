import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "j8rgpm",
        "typeId": "First_Device",
        "deviceId":"123"
    },
    "auth": {
        "token": "First_Device_123"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    print("Data Received :")
    print(m,"\n")

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:    
    client.commandCallback = myCommandCallback
    time.sleep(2)
    
client.disconnect()
