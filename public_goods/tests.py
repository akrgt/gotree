from otree.api import (
    Currency as c, currency_range, SubmissionMustFail, Submission
)
from . import views
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    cases = ['basic', 'min', 'max']

    def play_round(self):
        case = self.case
        yield (views.Introduction)

        if case == 'basic':
            assert self.player.payoff == None
            if self.player.id_in_group == 1:
                for invalid_contribution in [-1, 21]:
                    yield SubmissionMustFail(views.Contribute, {
                        'contribution': invalid_contribution})

        contribution = {
            'min': 0,
            'max': 20,
            'basic': 10,
        }[case]

        yield (views.Contribute, {"contribution": contribution})

        yield (views.Results)

        if self.player.id_in_group == 1:

            if case == 'min':
                expected_payoff = 100
            elif case == 'max':
                expected_payoff = 200
            else:
                expected_payoff = 150
            assert self.player.payoff == expected_payoff
