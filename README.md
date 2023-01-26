# _mypkg

# talker・listenerノード
![test](https://github.com/aoi-daiguji/_mypkg/actions/workflows/test.yml/badge.svg)

## このソフトについて
0から0.5秒間隔で1ずつ数字が増える変数をトピックに送るノードと、トピックの内容を出力するノードが入ったROS2パッケージです。

## 必要なソフトウェア
* Python
  * テスト済み:3.10

## テスト環境
* Ubuntu 22.04

## 使用しているノード
* talker
  * 0から255まで0.5秒間隔で増加する変数をトピック「countup」へ発信。
* listener
  * トピック「countup」を受信、出力する。

## 使い方
* モジュールとスクリプトの登録
  * package.xmlにモジュール「rclpy」、「std_msgs」を登録。
  * setup.pyにスクリプト「talker」、「listener」を登録。

* ビルド
  * colcon buildし、sourceで~/.bashrcを参照する。

* 実行
  * ros2 runでtalkerを実行。
  * 新しく端末を起動し、ros2 runでlistenerを実行。

##参考
* [Ryuichi Ueda](https://github.com/ryuichiueda)  
このパッケージのコードに関して、上田隆一先生の[スライド](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としています。

* [rikuhotakeda](https://github.com/rikuhotakeda)
テストファイル作成時に、助言・ファイルを提供して頂きました。

## 権利表記
* このソフトウェアパッケージは、3条項BSDライセンスの下、再配布及び使用が許可されます。
* © 2022 Daiguji Aoi
