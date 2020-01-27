# 明治大学行動経済学研究所
## 概要
oTreeの改修中です.
何らかの改変を行ったプログラムは先頭に「(改)」を、  
改変が不要な場合は「（未改変）」をそれぞれ付け  
リストの上に並べ替えています.

### 疑問点
全ページ表示後の「Finished」と表示される画面（OutOfRangeNotification.html）で  
日本語が「これ以上表示するページはりません」となる件ですが  
otree本体の日本語訳が間違っているのが問題のようです.  
ファイルの場所は仮想環境下で  
\Lib\site-packages\otree\locale\ja\LC_MESSAGES\django.po
にあります.  
ただ、ここを書き換えても表示は直らないんですよね...

ストラテジーメソッドと直接応答法が混ざっている最終提案ゲーム  
動いていますが、意図する実験になっているか不明なので保留します.

social value orientation  
ボタンが押せるようになるまでの時間が長いので、意図しない動作ならば修正対象になるかもしれません.

Principal Agent  
rejectする際もeffortの選択をしないと進行できないバグがあるので、分かり次第修正したいです.

lemon_market  
class Groupとclass Playerでseller_idが2度使われているので,Group側をbought_id(買われたid)と変更して調整中です.

### 改修点
#### pggfg/pggfg5  
起動しない理由として
models.pyのsender receiverのパラメータに"on_delete"が抜けていました.
(Djangoのバージョン違いによるバグかもしれません.)

#### ret_adding  
class Player(BasePlayer)/def score_round内
self.payoff_score を c(0)から 0に型変更.
デバッグ用に実験時間を30秒に変更中.

#### ret_typing  
同上  
時間切れ後の読み込みが400ページ全部読み込んでるような動作っぽいので  
軽量化できるポイントかもです.  

#### survey  
models.py/class Player/def set_payoffに　q_countryを追加.  
文言を'あなたの出身国を教えて下さい'に設定.

#### real_effort
Results.htmlに next_button を追加

#### repeat_prisoner
vies.py/class Introduction にis_displayedを追加.
(1ラウンド目にだけ説明文が表示されるように変更)

#### dictator
templates/dictator/Results.htmlのプレイヤー2の利益を
offer(pages.py/class Resultsの'offer')に変更することでエラーを回避.

#### dictator10
repeat_dictatorを削除.
dictatorフォルダを複製してdictator10を作成.
models.py/class Constants/name_in_url を'dictator10'に
(dictatorのままだと競合してエラーが出ました)
pages.py/class Introductionに is_displayedを追加.

#### ultimatum/ultimatum10
繰り返し用のアプリケーションultimatum10を作成.
treatmentの条件分岐で実験のラウンド数を変更できればアプリケーションが1個で済むのですが、いまのところ方法がみつかりません.

#### trust_simple
instructions_templateの項目が抜けていたので設定しエラーを回避.

#### vickrey_auction
入力フィールドが表示されなかったため、表記を書き換えて簡略化.
必要な入力形式(選択式,スライドバーetc)等ありましたらまた作り直します.

#### svotree2
svotreeのtemplatesフォルダを'svotree2'としてコピー

#### principal_agent
views.py/class Accept下のvars_for_templateにreturn_share,fixed_pay_intを加えてエラーを回避.
