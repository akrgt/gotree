from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """

一人のプレイヤーが，自分自身と，他のプレイヤーで何ポイント分けるか決定します．ただし，ここではプレイヤーAとBに5ポイントずつ渡して，取り上げることができるようにします，

One player decides how to divide a certain amount between himself and the other
player.
See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

まだしばらく改定中．もう少しよく考えないと，ちょっと使えないかも．

"""


class Constants(BaseConstants):
    name_in_url = 'dictator_steal'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'dictator_steal/Instructions.html'

    # Initial amount allocated to the dictator
    endowment = c(10)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    kept = models.CurrencyField(
        doc="""自身の利益を決めてください．""",
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        verbose_name='私は( 0 から %i )ポイントを自分の利益とします．' % Constants.endowment,

    )

#I will keep (from 0 to %i)
    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = self.kept
        p2.payoff = Constants.endowment - self.kept


class Player(BasePlayer):
    pass
