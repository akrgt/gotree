from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
二種類の最終提案ゲーム：直接応答法とストラテジーメソッド
Ultimatum game with two treatments: direct response and strategy method.
前者はあるプレイヤーが提案者として提案をして，応答者が受諾するか拒否するかを決定します．
In the former, one player makes an offer and the other either accepts or rejects.
応答者の反応に
It comes in two flavors, with and without hypothetical questions
 about the second player's response to offers other than the one that is made.
後者では，応答者があり得る全ての提案額のリストを提示します．そして，応答者はどの金額を受け入れるのか，もしくはどの金額を拒否するのかを尋ねられます．
In the latter treatment, the second player is given a list of all possible offers, and is asked which ones to accept or reject.
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum10'
    players_per_group = 2
    num_rounds = 10

    instructions_template = 'ultimatum/Instructions.html'

    endowment = c(10)
    payoff_if_rejected = c(0)
    offer_increment = c(1)

    offer_choices = currency_range(0, endowment, offer_increment)
    offer_choices_count = len(offer_choices)

    keep_give_amounts = []
    for offer in offer_choices:
        keep_give_amounts.append((offer, endowment - offer))


class Subsession(BaseSubsession):
    def before_session_starts(self):
        # randomize to treatments
        for g in self.get_groups():
            if 'treatment' in self.session.config:
                g.strategy = self.session.config['treatment'] == 'strategy'
            else:
                g.strategy = random.choice([True, False])


class Group(BaseGroup):
    strategy = models.BooleanField(
        doc="""Whether this group uses strategy method"""
    )

    amount_offered = models.CurrencyField(choices=Constants.offer_choices)

    offer_accepted = models.BooleanField(
        doc="if offered amount is accepted (direct response method)"
    )

    response_0 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_1 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_2 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_3 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_4 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_5 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_6 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_7 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_8 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_9 = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    response_10 = models.BooleanField(widget=widgets.RadioSelectHorizontal())

    def set_payoffs(self):
        p1, p2 = self.get_players()

        if self.strategy:
            self.offer_accepted = getattr(self, 'response_{}'.format(
                int(self.amount_offered)))

        if self.offer_accepted:
            p1.payoff = Constants.endowment - self.amount_offered
            p2.payoff = self.amount_offered
        else:
            p1.payoff = Constants.payoff_if_rejected
            p2.payoff = Constants.payoff_if_rejected


class Player(BasePlayer):
    pass
