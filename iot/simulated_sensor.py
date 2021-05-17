import random
import time
import csv
from datetime import datetime

from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=final-project-iot.azure-devices.net;DeviceId=PythonSensor1;SharedAccessKey=egKgXyL3wFDD5ZU8v1e7RUtJ3FE6IGG9T+18qr3PDuY="
CSV_FILE_PATH = "../../SB_May20_Nov20.csv"
DEVICE_ID = "PythonSensor1"

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():
    try:
        client = iothub_client_init()
        print("IoT Hub device sending periodic messages, press Ctrl-C to exit")
        while True:
            with open(CSV_FILE_PATH, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    msg_dict = dict(row)
                    msg_dict['DateTime'] = datetime.now().isoformat() # current time
                    msg_dict['DeviceId'] = DEVICE_ID
                    message = Message(str(msg_dict))
                    print(f"Sending message: {message}")
                    client.send_message(message)
                    time.sleep(10)
    except KeyboardInterrupt:
        print("Sensor simulator stopped")

if __name__ == '__main__':
    iothub_client_telemetry_sample_run()


