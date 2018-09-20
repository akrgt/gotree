from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        yield (views.Introduction)

        if self.player.id_in_group == 1:
            yield (views.Offer, {"kept": c(9)})
            assert self.player.payoff == c(9)
        else:
            assert self.player.payoff == c(1)
        yield (views.Results)
