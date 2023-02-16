from ppadb.client import Client
import time

def adb_connect():
    client = Client(host='127.0.0.1',port=5037)
    find_devices = client.devices()

    if len(find_devices) == 0:
        print("No devices")
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스{device}')

    return device, client

device, client = adb_connect()

def adb_capture():
    result = device.screencap() 
    with open(r'auto\python\mobile BlueStacks\WannaI', 'wb') as fp: #파일 저장
        fp.write(result) 

def adb_Click(x, y):
    device.shell(f'input tap {x, y}')

device, client = adb_connect()
adb_Click(959,453)
time.sleep(1.5)

while True:
    adb_Click(320,1803)
    time.sleep(1)
    adb_Click(570,693)
    time.sleep(13)
    device.shell('input keyevent 3')
    time.sleep(0.5)
    device.shell('input keyevent 3')
    time.sleep(1)