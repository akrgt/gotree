from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
3人5回繰り返し公共財ゲームです．This is a 10-period public goods game with 4 players.
"""


class Constants(BaseConstants):
    name_in_url = 'repeat_public_goods'
    players_per_group = 3
    num_rounds = 5

    instructions_template = 'repeat_public_goods/Instructions.html'

    # """Amount allocated to each player"""
    endowment = c(20)
    efficiency_factor = 2


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        payoffs = sorted([p.payoff for p in self.get_players()])
        return {'payoffs': payoffs}

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
        min=0, max=Constants.endowment,
        doc="""プレイヤーによる支払""",
    )

    total_payoff = models.CurrencyField()
    total_earnings = models.CurrencyField()

    def set_final(self):
        self.total_payoff = sum([p.payoff for p in self.in_all_rounds()])
 #       for p in self.get_players():
 #           p.total_payoff = sum([self.payoff in self.in_all_rounds()])
 #           p.total_earnings = p.total_contribution * Constants.efficiency_factor



