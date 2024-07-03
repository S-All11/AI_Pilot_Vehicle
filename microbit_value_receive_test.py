from microbit import *

# UART 初期化 (ピン指定)
uart.init(baudrate=9600, tx=pin0, rx=pin1)

display.scroll("Ready")

while True:
    if uart.any():
        # 受信データの読み込み
        received = uart.readline().strip()
        if received:
            # 受信データを表示
            print(received)
            display.scroll(received)
        else:
            display.show(Image.SAD)
