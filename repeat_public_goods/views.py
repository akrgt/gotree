from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    def is_displayed(self):
        return self.round_number == 1


class Contribute(Page):
    """Player: Choose how much to contribute"""

    form_model = models.Player
    form_fields = ['contribution']

    timeout_submission = {'contribution': c(Constants.endowment / 2)}


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs(),

    body_text = "他の参加者が意思決定中です．しばらくお待ち下さい．"


class Results(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(self):
#        self.player.sum_all_rounds()
        return {
            'total_earnings': self.group.total_contribution * Constants.efficiency_factor,
#            'cumulative_payoffs': sum([p.payoff for p in self.player.in_all_rounds()]),
            'total_payoffs': sum([p.payoff for p in self.player.in_all_rounds()]),
        }

    def before_next_page(self):
        self.player.set_final()



page_sequence = [
    Introduction,
    Contribute,
    ResultsWaitPage,
    Results
]
