import serial
import time
import tkinter as tk

# シリアルポートの設定
ser = serial.Serial('/dev/serial0', 115200, timeout=1)

def send_integer(value):
    # 整数値を文字列に変換して送信
    ser.write(f"{value}\n".encode('utf-8'))
    print(f"Sent: {value}")

def forward_drive():
    m = 1
    send_integer(m)

def back_drive():
    m = 2
    send_integer(m)

def left_drive():
    m = 3
    send_integer(m)

def right_drive():
    m = 4
    send_integer(m)

def stop():
    m = 0
    send_integer(m)

def quick_turn_l():
    m = 5
    send_integer(m)
    
def quick_turn_r():
    m = 6
    send_integer(m)
    
def move_max_f():
    m = 7
    send_integer(m)

def brake():
    m = 0
    send_integer(m)

# キーボード入力を検出してモーター制御関数を呼び出すためのクラス
class RCController:
    def __init__(self, master):
        self.master = master
        self.master.title("RC Controller")
        self.master.geometry("300x200")

        self.master.bind("<KeyPress-w>", self.move_forward)
        self.master.bind("<KeyPress-s>", self.move_backward)
        self.master.bind("<KeyPress-a>", self.turn_left)
        self.master.bind("<KeyPress-d>", self.turn_right)
        self.master.bind("<KeyPress-q>", self.quick_turn_l)
        self.master.bind("<KeyPress-e>", self.quick_turn_r)
        self.master.bind("<KeyPress-z>", self.move_max_f)
        self.master.bind("<KeyPress-x>", self.brake)
        #self.master.bind("<KeyRelease>", self.brake)

    def move_forward(self, event):
        forward_drive()

    def move_backward(self, event):
        back_drive()

    def turn_left(self, event):
        left_drive()

    def turn_right(self, event):
        right_drive()
        
    def quick_turn_l(self, event):
        quick_turn_l()
    
    def quick_turn_r(self, event):
        quick_turn_r()
        
    def move_max_f(self, event):
        move_max_f()
    
    def brake(self, event):
        brake()

#    def stop(self, event):
 #       stop()

if __name__ == "__main__":
    root = tk.Tk()
    controller = RCController(root)
    root.mainloop()

r=0
while True:
    # モーター制御用のループ
    pass
