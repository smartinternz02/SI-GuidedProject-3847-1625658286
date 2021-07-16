import wiotp.sdk.device
import time
import random
from ibmcloudant.cloudant_v1 import CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

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


authenticator = BasicAuthenticator('apikey-v2-10xypw9nevga82oqb993uwcfdqgl748fcoiznj3jfrzn', '3fb54d29a2d64e40f7a0657467d33a27')
service = CloudantV1(authenticator=authenticator)
service.set_service_url('https://apikey-v2-10xypw9nevga82oqb993uwcfdqgl748fcoiznj3jfrzn:3fb54d29a2d64e40f7a0657467d33a27@c6a728a6-a633-4d59-a8e9-c06a612f8176-bluemix.cloudantnosqldb.appdomain.cloud')
def myCommandCallback(cmd):
    print("DATE received from IBM IoT Platform: %s" % cmd.data['DATE'])
    print("TIME received from IBM IoT Platform: %s" % cmd.data['TIME'])
    date=cmd.data['DATE']
    time=cmd.data['TIME']
    products_doc = {
        "DATE" : date,
        "TIME" : time
    }

    response = service.post_document(db='sample', document=products_doc).get_result()
    print(response)


client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:    
    client.commandCallback = myCommandCallback
    time.sleep(2)
    
client.disconnect()

