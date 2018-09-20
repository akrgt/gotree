from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random



class Constants(BaseConstants):
    name_in_url = 'ind_info'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0
    ratemo_1 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='たいていの人より，ものごとを論理的に解決するのが上手である．',
                                widget=widgets.Select())
    ratemo_2 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='直観に頼らなければならない状況は好きではない．',
                                widget=widgets.Select())
    ratemo_3 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='自分の予感を信じることにしている．',
                                widget=widgets.Select())
    ratemo_4 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='論理的な考えの持ち主だ．',
                                widget=widgets.Select())
    ratemo_5 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='ものごとを注意深く理論的に解決するのは，得意ではない．',
                                widget=widgets.Select())
    ratemo_6 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常に当てはまる'],
                                verbose_name='簡単な問題より複雑な問題の方が好きだ．',
                                widget=widgets.Select())
    ratemo_7 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='なぜだか理由を説明できないが，その人が正しいか間違っているかを，感じとることができる．',
                                widget=widgets.Select())
    ratemo_8 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常に当てはまる'],
                                verbose_name='分析的に考える方ではない．',
                                widget=widgets.Select())
    ratemo_9 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='私にはすごい直観力はない．',
                                widget=widgets.Select())
    ratemo_10 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='考えることは，楽しいことだと思わない．',
                                widget=widgets.Select())
    ratemo_11 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='直観は問題を解決するのに役立つ方法だろう．',
                                widget=widgets.Select())
    ratemo_12 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='感情に基づいて重要な決定をするのは，愚かなことだと思う．',
                                widget=widgets.Select())
    ratemo_13 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='行動を決める時，直観に頼ることが多い．',
                                widget=widgets.Select())
    ratemo_14 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='私にとって，新しい考え方を学ぶことは，とても魅力的である．',
                                widget=widgets.Select())
    ratemo_15 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='複雑な問題を解決するのは，得意ではない．',
                                widget=widgets.Select())
    ratemo_16 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='知的な挑戦が好きだ．',
                                widget=widgets.Select())
    ratemo_17 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='直観に頼って重要な決定をするのは，いい考えだと思わない．',
                                widget=widgets.Select())
    ratemo_18 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='もし私が直観に頼るならば，間違いをおかすことが多くなるだろう．',
                                widget=widgets.Select())
    ratemo_19 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='直観的な印象に頼るのが好きだ．',
                                widget=widgets.Select())
    ratemo_20 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='一生懸命考えなければならないような問題を解決するのが好きだ．',
                                widget=widgets.Select())
    ratemo_21 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='答えを見つけるために直観に従って，うまくいかなかったことはほとんどない．',
                                widget=widgets.Select())
    ratemo_22 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='人生や生活上のいろんな問題を考えるとき，直観的にやるとうまくいく．',
                                widget=widgets.Select())
    ratemo_23 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='注意深く論理的な分析が必要とされる問題を解決するのは，得意ではない．',
                                widget=widgets.Select())
    ratemo_24 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='いろいろ考えるのは好きではない．',
                                widget=widgets.Select())

    big5_1 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='活発で，外向的だと思う',
                                widget=widgets.Select())

    big5_2 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='他人に不満をもち，もめごとを起こしやすいと思う',
                                widget=widgets.Select())

    big5_3 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='しっかりしていて，自分に厳しいと思う',
                                widget=widgets.Select())

    big5_4 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='心配性で，うろたえやすいと思う',
                                widget=widgets.Select())

    big5_5 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='新しいことが好きで，変わった考えをもつと思う',
                                widget=widgets.Select())

    big5_6 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='ひかえめで，おとなしいと思う',
                                widget=widgets.Select())

    big5_7 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='人に気をつかう，やさしい人間だと思う',
                                widget=widgets.Select())

    big5_8 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='だらしなく，うっかりしていると思う',
                                widget=widgets.Select())

    big5_9 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='冷静で，気分が安定していると思う',
                                widget=widgets.Select())

    big5_10 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='発想力に欠けた，平凡な人間だと思う',
                                widget=widgets.Select())



    q_gender = models.CharField(initial=None,
                                choices=['男性', '女性', 'その他'],
                                verbose_name='あなたの性別を教えてください．',
                                widget=widgets.Select())
    q_age = models.PositiveIntegerField(verbose_name='あなたの年齢を教えてください．',
                                        choices=range(0, 125),
                                        initial=None)
    q_country = models.CharField(initial=None,
                                choices=['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県','茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県','新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県', '三重県','滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県','鳥取県', '島根県', '岡山県', '広島県', '山口県','徳島県', '香川県', '愛媛県', '高知県','福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県'],
                                verbose_name='あなたのおすまいの地域を教えてください．',
                                widget=widgets.Select())



    q_aca = models.CharField(initial=None,
                                choices=['中学校卒業','高校中退','高校卒業','専門学校（短期大学）中退','専門学校（短期大学）卒業','大学中退','大学卒業','大学院修士課程（博士前期課程）中退','大学院修士課程（博士前期課程）修了','大学院博士課程（博士後期課程）中退','大学院博士課程（博士後期課程）修了'],
                                verbose_name='あなたの最終学歴を教えてください．',
                                widget=widgets.Select())

    q_INK = models.CharField(initial=None,
                                choices=['0円','1円〜200万円未満','200万円以上〜400万円未満','400万円以上〜600万円未満','600万円以上〜800万円未満','800万円以上〜1,000万円未満','1,000万円以上〜1,200万円未満','1,200万円以上〜1,500万円未満','1,500万円以上〜2,000万円未満','2,000万円以上','わからない'],
                                verbose_name='あなたの個人収入(額面)を教えてください．',
                                widget=widgets.Select())
    q_INS = models.CharField(initial=None,
                                choices=['0円','1円〜200万円未満','200万円以上〜400万円未満','400万円以上〜600万円未満','600万円以上〜800万円未満','800万円以上〜1,000万円未満','1,000万円以上〜1,200万円未満','1,200万円以上〜1,500万円未満','1,500万円以上〜2,000万円未満','2,000万円以上','わからない'],
                                verbose_name='あなたの世帯収入(額面)を教えてください．',
                                widget=widgets.Select())
    q_MAR = models.CharField(initial=None,
                                choices=['未婚', '既婚'],
                                verbose_name='あなたは結婚されていますか？それとも結婚されていませんか？',
                                widget=widgets.Select())
    q_CHI = models.CharField(initial=None,
                                choices=['子どもなし', '子どもあり'],
                                verbose_name='あなたは子どもがいますか？いませんか？',
                                widget=widgets.Select())



    crt_bat = models.PositiveIntegerField()
    crt_widget = models.PositiveIntegerField()
    crt_lake = models.PositiveIntegerField()
    crt_1st = models.CharField(initial=None,
                                choices=['あてはまらない','どちらかといえばあてはまらない','どちらかといえばあてはまる','あてはまる'],
                                verbose_name='日常生活の中で，自分の行動は「自分自身」に見られていると思うことがある．',
                                widget=widgets.Select())
    crt_2nd = models.CharField(initial=None,
                                choices=['あてはまらない','どちらかといえばあてはまらない','どちらかといえばあてはまる','あてはまる'],
                                verbose_name='日常生活の中で，自分の行動は「直接誰か（人間）」に見られていると思うことがある．',
                                widget=widgets.Select())
    crt_3rd = models.CharField(initial=None,
                                choices=['あてはまらない','どちらかといえばあてはまらない','どちらかといえばあてはまる','あてはまる'],
                                verbose_name='日常生活の中で，自分の行動は「監視カメラ等を通じて誰か（人間）」に間接的に見られていると思うことがある．',
                                widget=widgets.Select())
    crt_sup = models.CharField(initial=None,
                                choices=['あてはまらない','どちらかといえばあてはまらない','どちらかといえばあてはまる','あてはまる'],
                                verbose_name='日常生活の中で，自分の行動は「お天道様や神様，仏様などの超自然的な存在」に見られていると思うことがある．',
                                widget=widgets.Select())
