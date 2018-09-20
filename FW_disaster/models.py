from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random



class Constants(BaseConstants):
    name_in_url = 'FW_disaster'
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

    DisasterExp_1 = models.CharField(initial=None,
                                choices=['経験し，大規模な被害を受けた','経験し，被害を受けた','経験し，小規模な被害を受けた','経験したが，被害は全く受けなかった','経験したことはない'],
                                verbose_name='地震',
                                widget=widgets.Select())
    DisasterExp_2 = models.CharField(initial=None,
                                choices=['経験し，大規模な被害を受けた','経験し，被害を受けた','経験し，小規模な被害を受けた','経験したが，被害は全く受けなかった','経験したことはない'],
                                verbose_name='津波',
                                widget=widgets.Select())
    DisasterExp_3 = models.CharField(initial=None,
                                choices=['経験し，大規模な被害を受けた','経験し，被害を受けた','経験し，小規模な被害を受けた','経験したが，被害は全く受けなかった','経験したことはない'],
                                verbose_name='噴火',
                                widget=widgets.Select())
    DisasterExp_4 = models.CharField(initial=None,
                                choices=['経験し，大規模な被害を受けた','経験し，被害を受けた','経験し，小規模な被害を受けた','経験したが，被害は全く受けなかった','経験したことはない'],
                                verbose_name='土砂災害（崖崩れ・土石流・地滑り）',
                                widget=widgets.Select())
    DisasterExp_5 = models.CharField(initial=None,
                                choices=['経験し，大規模な被害を受けた','経験し，被害を受けた','経験し，小規模な被害を受けた','経験したが，被害は全く受けなかった','経験したことはない'],
                                verbose_name='豪雨',
                                widget=widgets.Select())
    DisasterExp_6 = models.CharField(initial=None,
                                choices=['経験し，大規模な被害を受けた','経験し，被害を受けた','経験し，小規模な被害を受けた','経験したが，被害は全く受けなかった','経験したことはない'],
                                verbose_name='洪水',
                                widget=widgets.Select())
    DisasterExp_7 = models.CharField(initial=None,
                                choices=['経験し，大規模な被害を受けた','経験し，被害を受けた','経験し，小規模な被害を受けた','経験したが，被害は全く受けなかった','経験したことはない'],
                                verbose_name='暴風・竜巻',
                                widget=widgets.Select())
    DisasterExp_8 = models.CharField(initial=None,
                                choices=['経験し，大規模な被害を受けた','経験し，被害を受けた','経験し，小規模な被害を受けた','経験したが，被害は全く受けなかった','経験したことはない'],
                                verbose_name='豪雪',
                                widget=widgets.Select())
    DisasterExp_9 = models.CharField(initial=None,
                                choices=['経験し，大規模な被害を受けた','経験し，被害を受けた','経験し，小規模な被害を受けた','経験したが，被害は全く受けなかった','経験したことはない'],
                                verbose_name='その他の異常な自然災害',
                                widget=widgets.Select())





    crt_HAP = models.CharField(initial=None,
                                choices=['0','1','2','3','4','5','6','7','8','9','10'],
                                verbose_name='あなたは現在，どの程度幸せですか？0-10満点で評価してください．',
                                widget=widgets.Select())

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
    FW1 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='未来はいつも運命によって決められていると信じている',
                                widget=widgets.Select())
    FW2 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人の性格や才能は，（脳のつくりなどの）生物学的な構造によって決まっている',
                                widget=widgets.Select())
    FW3 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人の歴史の大部分は偶然の出来事の積み重ねである',
                                widget=widgets.Select())
    FW4 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人は自分の意志で決定を下すことができる',
                                widget=widgets.Select())
    FW5 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='どんなに努力しても，自分の運命は変えられない',
                                widget=widgets.Select())
    FW6 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='心理学者や精神科医はやがて人のふるまいの全てを解明するだろう',
                                widget=widgets.Select())
    FW7 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='誰もこれから起こることを予測できない',
                                widget=widgets.Select())
    FW8 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人は自分が下した誤った選択に対しては，一切の責任を負わなくてはならない',
                                widget=widgets.Select())
    FW9 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='全ての人の人生は，最初から運命によって決められている',
                                widget=widgets.Select())
    FW10 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='自分の将来は，遺伝子によって決められている',
                                widget=widgets.Select())
    FW11 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='サイコロの目やコイントスのように，人生は予測できない',
                                widget=widgets.Select())
    FW12 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人は心から望めば，どんな障害でも乗り越えられる',
                                widget=widgets.Select())
    FW13 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='物事はなるようにしかならず，自分にできることは少ない',
                                widget=widgets.Select())
    FW14 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='過去の経験がどのように現在の自分の知性や性格を形作ってきたかを，科学は示してくれる',
                                widget=widgets.Select())
    FW15 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人は誰しも予測できないようなふるまいをする',
                                widget=widgets.Select())
    FW16 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='犯罪者には自分の行った悪事に対する，全面的な責任がある',
                                widget=widgets.Select())
    FW17 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='その考え方が好きかどうかは別として，人生は説明できない力に動かされているように思う',
                                widget=widgets.Select())
    FW18 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人間の行動は他の動物たちと同じように，いつも自然の摂理に従っている',
                                widget=widgets.Select())
    FW19 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='日々の出来事は全くもって一貫性を持たないため，先を予測することは難しい',
                                widget=widgets.Select())
    FW20 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人生は運に負うところが大きい',
                                widget=widgets.Select())
    FW21 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人は自らの自由な意志や思考で行動している',
                                widget=widgets.Select())
    FW22 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='親の持つ性質は，子どもの性質を決めている',
                                widget=widgets.Select())
    FW23 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人は，自分のあやまちにいつも責任を負っている',
                                widget=widgets.Select())
    FW24 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='大人になってから成功するかは子どもの頃の環境で決まる',
                                widget=widgets.Select())
    FW25 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人に起こる出来事は，偶然の産物である',
                                widget=widgets.Select())
    FW26 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='精神力が強ければ，自分に生じた欲望をいつも抑えることができる',
                                widget=widgets.Select())
    FW27 = models.CharField(initial=None,
                                choices=['1.そう思わない','2.どちらかといえばそう思わない','3.どちらでもない','4.どちらかといえばそう思う','5.そう思う'],
                                verbose_name='人の将来は予測することができない',
                                widget=widgets.Select())
