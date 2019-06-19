# rotateImage Ver. 1.1

## 使い方
```
Python rotateImage.py 画像のあるディレクトリの相対パス  生成したい個数
```
```
ex) Python rotateImage.py ./src  8
```  
で実行するだけです。指定したディレクトリ内の画像がすべて回転されます。回転された画像は指定したディレクトリ内のrotatedディレクトリに保存されます。  
個数と回転する角度についてですが、画像の最小回転角度は生成する画像の個数をnとすると 360/n 度になります。 8個くらいが回転を感じられていいと思います。
外部ライブラリのPillowを使用しています。まだインストールしていない方は
```
pip install pillow
```
でインストールしてください
