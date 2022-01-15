import pyautogui, time

def howl():
    pyautogui.write('6')
    time.sleep(0.005)
    pyautogui.write('s')
    time.sleep(0.005)

def main():
    time.sleep(2)
    while True:
        howl()
if __name__ == "__main__":
    main()
#6s6s6s6s6s66s6s