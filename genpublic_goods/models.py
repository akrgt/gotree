from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
4人一回限りの公共財ゲームです．This is a one-period public goods game with 4 players.
"""


class Constants(BaseConstants):
    name_in_url = 'genpublic_goods'
    players_per_group = 3
    num_rounds = 3

    instructions_template = 'genpublic_goods/Instructions.html'

    # """Amount allocated to each player"""
    endowment = c(10)
    efficiency_factor = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        for p in self.get_players():
            p.payoff = (Constants.endowment - p.contribution) + self.individual_share


class Player(BasePlayer):
    contribution = models.CurrencyField(
        initial=None,
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
#    contribution = models.CharField(
#        initial=None,
#         choices=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#    )


#    contribution = models.CurrencyField(
#        min=0, max=Constants.endowment,
#        doc="""The amount contributed by the player""",
#    )




    HAPPINESS = models.CharField(initial=None,
                                choices=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                                verbose_name='あなたは今，どの程度幸せですか？10点満点でお答えください．'
                           )