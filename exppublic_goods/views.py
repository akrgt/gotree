from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    timeout_seconds = 180

    def is_displayed(self):
        return self.round_number == 1
    pass


class Contribute(Page):
    """Player: Choose how much to contribute"""
    timeout_seconds = 30

    form_model = models.Player
    form_fields = ['contribution']

    timeout_submission = {'contribution': c(Constants.endowment / 2)}


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "他のプレイヤーが意思決定をしています．しばらくお待ちください．"


class Results(Page):
    """Players payoff: How much each has earned"""
    timeout_seconds = 30

    def vars_for_template(self):
        return {
            'total_earnings': self.group.total_contribution * Constants.efficiency_factor,
        }
    form_model = models.Player
    form_fields = ['HAPPINESS']

page_sequence = [
    Introduction,
    Contribute,
    ResultsWaitPage,
    Results
]
