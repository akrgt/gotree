from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield (views.Introduction)
        yield (views.Decision, {"decision": '協力'})
        assert 'Both of you chose to cooperate' in self.html
        assert self.player.payoff == Constants.both_cooperate_payoff
        yield (views.Results)
