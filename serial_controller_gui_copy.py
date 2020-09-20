import tkinter as tk
import serial
import numpy as np
import scipy.io as sio

class Controller:
    def __init__(self):
        self.pressed = {}
        self.prevPressed = {}
        self._initPresses()
        self._create_ui()
        self.ser = serial.Serial(
            port='/dev/cu.wchusbserial1410',
            baudrate=115200,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS
        )
        self.ser.isOpen()
        self.list_values = []
        self.mylist = []
        self.mydict = {}
        self.keylist = []

    def _initPresses(self):
        self.pressed["w"] = 0
        self.pressed["a"] = 0
        self.pressed["s"] = 0
        self.pressed["d"] = 0
        self.prevPressed["w"] = 0
        self.prevPressed["a"] = 0
        self.prevPressed["s"] = 0
        self.prevPressed["d"] = 0

    def start(self):
        self._check_key_press()
        self.root.mainloop()
        print(self.mylist)
        datamatrix = np.array(self.mylist)
        print datamatrix
        sio.savemat('Train_Data1.mat', {'datamatrix':datamatrix})

        
    def _check_for_press(self, key, command):
         if self._is_pressed(key):
          self.prevPressed[key] = 1
          self.ser.write(command)
          self.list_values = [v for v in self.pressed.values()]
          self.mylist.append(self.list_values)
          print(key + " pressed")
          print(self.mylist)

        
    def _check_for_release(self, key, command):
        if self._is_released(key):
            self.prevPressed[key] = 0
            self.ser.write(command)
            print(key + " released")

    def _check_key_press(self):
        self._check_for_press("w", b"\x01")
        self._check_for_release("w", b"\x02")
        self._check_for_press("s", b"\x03")
        self._check_for_release("s", b"\x04")
        self._check_for_press("d", b"\x05")
        self._check_for_release("d", b"\x06")
        self._check_for_press("a", b"\x07")
        self._check_for_release("a", b"\x08")

        self.root.after(10, self._check_key_press)

    def _is_pressed(self, key):
        return self.pressed[key] and self.prevPressed[key] == 0

    def _is_released(self, key):
        return self.pressed[key] == 0 and self.prevPressed[key]

    def _create_ui(self):
        self.root = tk.Tk()
        self.root.geometry('400x300')
        self._set_bindings()

    def _set_bindings(self):
        for char in ["w","s","d", "a"]:
            self.root.bind("<KeyPress-%s>" % char, self._pressed)
            self.root.bind("<KeyRelease-%s>" % char, self._released)
            self.pressed[char] = 0

    def _pressed(self, event):
        self.pressed[event.char] = 1

    def _released(self, event):
        self.pressed[event.char] = 0

if __name__ == "__main__":
    p = Controller()
    p.start()


