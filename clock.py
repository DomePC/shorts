import time, os, datetime

while True:
    now = datetime.datetime.now()
    print(f'{now.hour}:{now.minute}:{now.second}')
    time.sleep(1)
    os.system('cls')