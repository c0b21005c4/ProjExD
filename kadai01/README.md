#第１回
##消えたアルファベットを探すゲーム
###遊び方
#コマンドラインで"kiemoji.py"を入力して起動する。
#対象文字と表示文字を見比べ、消えたアルファベットを探す。
#まず、消えた文字の個数を回答する。
#次に、消えたアルファベットを入力する（消えた文字数分回答）。
#ユーザの回答がすべてあっていた時、ゲームを終了する。
#不正解だった場合はその時点でやり直す。
#なお、最大やり直し数が決まっている。
#ユーザのやり直し回数が上限を超えた時、その時点でゲームを終了する。
#ゲーム終了時にこの問題にかかった時間を表示する。
###プログラムの内容
#main_quiz関数はユーザの回答の合否と、それに応じたコメント、所要時間の計測と表示をする。
#↳その際にsyutudai関数を呼び出す。
#syutudai関数は対象文字、欠損文字、表示文字の作成をする。