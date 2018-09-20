from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class FreeWill(Page):

    form_model = models.Player
    form_fields = ['crt_HAP',
                  'crt_1st',
                  'crt_2nd',
                  'crt_3rd',
                  'crt_sup',
                  'FW1',
                  'FW2',
                  'FW3',
                  'FW4',
                  'FW5',
                  'FW6',
                  'FW7',
                  'FW8',
                  'FW9',
                  'FW10',
                  'FW11',
                  'FW12',
                  'FW13',
                  'FW14',
                  'FW15',
                  'FW16',
                  'FW17',
                  'FW18',
                  'FW19',
                  'FW20',
                  'FW21',
                  'FW22',
                  'FW23',
                  'FW24',
                  'FW25',
                  'FW26',
                  'FW27'
                   ]

    def before_next_page(self):
        self.player.set_payoff()


class DisasterExp(Page):

    form_model = models.Player
    form_fields = ['DisasterExp_1',
                   'DisasterExp_2',
                   'DisasterExp_3',
                   'DisasterExp_4',
                   'DisasterExp_5',
                   'DisasterExp_6',
                   'DisasterExp_7',
                   'DisasterExp_8',
                   'DisasterExp_9'

]

    def before_next_page(self):
        self.player.set_payoff()


page_sequence = [
    FreeWill,
    DisasterExp,
]
