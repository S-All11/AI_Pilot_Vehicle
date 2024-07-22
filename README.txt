このプロジェクトはカメラやセンサーなどを用いた自動運転を
実装するAI制御のマイコンカーを製作することを目的とし製作後の
拡張性と既存の製品を使ってある程度簡単化する事を
考えた電子工作のためのリポジトリーとなります

基本的な考えかた

AIカメラを接続し画像検知を行う処理装置として
Raspberry PI4Bをメインボードとしそこに
モーター制御用のドライバー回路にdfr0548を用意
メインボードとモータードライバーの仲介役として
Micro: bitを双方に相互接続した回路構成となります
またRaspberry Piのスペックにはある程度の余裕が
欲しいため製作する際はraspi 4か5以降を推奨します

自動運転とはいえ最初は学習かけるにあたってある程度
自分でも手動運転による走行を行いたいため
ラジコンとしても機能するように市販のゲームパッドを
操作用のプロポとして接続する機能も実装していきます

このリポジトリの見方
Raspberry Pi側の値を送信するコード　: raspi_value_send.pyを参照
Micro:bitで受信した値でモータ回転数制御するコード : makecode_project記載のURLを参照
Micro:bitで受信した値をローカルの実行環境で確認するだけのコード : microbit_value_receive_test.pyを参照
Raspberry Pi側でラジコンのプロポとしての一連の機能が実装済みのコード : UART_Controller.pyを参照
Micro:bit側でラジコンとして一連のモータ動作が実装されたプロジェクトは次のリンク: https://makecode.microbit.org/_C5UUk5bLjf9W

https://makecode.microbit.org/_5AT4puKLC47H
https://makecode.microbit.org/_32KKU2i3LD2q
