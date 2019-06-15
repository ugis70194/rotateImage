﻿# rotateImage

## 使い方
```
Python rotateImage.py 画像のあるディレクトリの相対パス /画像のファイル名 生成したい個数
```
```
ex) Python rotateImage.py ./src /ugis.png 8
```  
で実行するだけです。第2引数の前の```/```を忘れないでください。  
個数と回転する角度についてですが、画像の最小回転角度は生成する画像の個数をnとすると 360/n 度になります。 8個くらいが回転を感じられていいと思います。  

外部ライブラリのPillowを使っています。インストールしていない場合は
```
pip install Pillow
```
でインストールしてください。
