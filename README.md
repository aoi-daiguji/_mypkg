# _mypkg

#talker・listenerノード
![test](https://github.com/aoi-daiguji/_mypkg/actions/workflows/test.yml/badge.svg)

##このソフトについて
大宮司葵生という人間が0.5秒ごとに誕生日を迎え、255歳まで年を取るros2パッケージです。

##必要なソフトウェア
* Python
  * テスト済み:3.10

##テスト環境
* Ubuntu 22.04

##使用しているノード
* talker
  * 人物の名前と年齢（0.5秒ずつに255まで増加）をトピック「person」へ発信。
* listener
  * トピック「person」を受信、出力する。

##使い方
* モジュールとスクリプトの登録
  * package.xmlにモジュール「rclpy」、「std_msgs」を登録。
  * setup.pyにスクリプト「talker」、「listener」を登録。

* ビルド
  * colcon buildし、sourceで~/.bashrcを参照する。

* 実行
  * ros2 runでtalkerを実行。
  * 新しく端末を起動し、ros2 runでlistenerを実行。

## 権利表記
* このソフトウェアパッケージは、3条項BSDライセンスの下、再配布及び使用が許可されます。
* © 2022 Daiguji Aoi
