import time
from datetime import datetime

if __name__ == '__main__':
    print("The application is running...")
    while True:
        print(f"{datetime.now()}: hello there!")
        time.sleep(1)
