import serial
import time

# シリアルポートの設定
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

def send_integer(value):
    # 整数値を文字列に変換して送信
    ser.write(f"{value}\n".encode('utf-8'))
    print(f"Sent: {value}")

# 例として1から10までの整数を送信
for i in range(1, 11):
    send_integer(i)
    time.sleep(1)  # 1秒待機
