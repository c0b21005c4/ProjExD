# 第6回
## こうかとんシューティング（ex06/shooting_koukaton.py）
### ゲーム概要
- ex06/shooting_koukaton.pyを実行すると，1600x900のスクリーンに草原が描画され，現れる敵を倒していくゲーム
- こうかとんのライフは3つ
- こうかとんのライフが０になるとゲームオーバー(画面が現れる)
- こうかとんは前方に卵を発射することができる
- 卵と敵が接触した時、敵が消える
- 一定間隔で薬とハートが流れてくる
- 薬を取ると一定時間攻撃の制限がなくなる
- ハートを取るとライフが１ふえる
### 操作方法
#### ゲーム中画面
- 矢印キーでこうかとんを上下左右に移動する
- スペースキーで卵の発射（攻撃）ができる
#### ゲーム外画面
- 左右キーで選択
- エンターキーで決定
### 機能項目
#### 天野
- ゲームの基盤の作成
- 敵の追加
- 敵の攻撃の追加
- こうかとんの攻撃の追加
- 薬（パワーアップアイテム）の追加
#### 湯口
- ラスボスの追加(攻撃、出現等)
- スタート、ゲームオーバー、クリア画面の作成
- 画像を使っているクラスの親クラスを作成してコード量を削減した
#### 鈴木
- こうかとんのライフを作成(敵に当たったりなど機能的な面も担当)
- ゲームオーバー時にケンタッキーおじさんがくるくる回っているように作成
#### 長田
- BGMの追加
- 効果音の追加
#### 大橋
- スコアの表示(小さい敵は1,ボス敵は100追加される)
