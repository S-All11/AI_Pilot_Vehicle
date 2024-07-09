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

'''next update
def quick_turn_L():
    m = 5
    send_integer(m)
    
def quick_turn_R():
    m = 6
    send_integer(m)
'''

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
        self.master.bind("<KeyRelease>", self.stop)

    def move_forward(self, event):
        forward_drive()

    def move_backward(self, event):
        back_drive()

    def turn_left(self, event):
        left_drive()

    def turn_right(self, event):
        right_drive()

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

