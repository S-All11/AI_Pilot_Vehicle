import serial
import time

# シリアルポートの設定
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

def send_integer(value):
    # 整数値を文字列に変換して送信
    ser.write(f"{value}\n".encode('utf-8'))
    print(f"Sent: {value}")

def forward_drive():
    m1,m2 = 150
    m3,m4 = 65
        
def back_drive():
    m1,m2 = -150
    m3,m4 = -65
    
def left_drice():
    m1,m2 = 150
    m3,m4 = 65

def right_drive():
    m1,m2 = 150
    m3,m4 = 65

def quick_turn_L():
    m1,m2 = 150
    m3,m4 = 65
    
def quick_turn_R():
    m1,m2 = 150
    m3,m4 = 65    

r=0
while True:
    for i in range(50, 160,10):
        send_integer(i)
        time.sleep(1)  # 1秒待機
        
    for i in range(150, 40,-10):
        send_integer(i)
        time.sleep(1)  # 1秒待機
    send_integer(0)
    time.sleep(3)
    if(r>=1):
        break
    r+=1
