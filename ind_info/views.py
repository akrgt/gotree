from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class CognitiveReflectionTest(Page):

    form_model = models.Player
    form_fields = ['crt_bat',
                  'crt_widget',
                  'crt_lake',
                  'crt_1st',
                  'crt_2nd',
                  'crt_3rd',
                  'crt_sup']

    def before_next_page(self):
        self.player.set_payoff()


class ratemo(Page):

    form_model = models.Player
    form_fields = ['ratemo_1',
                   'ratemo_2',
                   'ratemo_3',
                   'ratemo_4',
                   'ratemo_5',
                   'ratemo_6',
                   'ratemo_7',
                   'ratemo_8',
                   'ratemo_9',
                   'ratemo_10',
                   'ratemo_11',
                   'ratemo_12',
                   'ratemo_13',
                   'ratemo_14',
                   'ratemo_15',
                   'ratemo_16',
                   'ratemo_17',
                   'ratemo_18',
                   'ratemo_19',
                   'ratemo_20',
                   'ratemo_21',
                   'ratemo_22',
                   'ratemo_23',
                   'ratemo_24'

]

    def before_next_page(self):
        self.player.set_payoff()


class big5(Page):

    form_model = models.Player
    form_fields = ['big5_1',
                   'big5_2',
                   'big5_3',
                   'big5_4',
                   'big5_5',
                   'big5_6',
                   'big5_7',
                   'big5_8',
                   'big5_9',
                   'big5_10'

]

    def before_next_page(self):
        self.player.set_payoff()




class Demographics(Page):

    form_model = models.Player
    form_fields = [
                  'q_gender',
                  'q_age',
                  'q_country',
                  'q_aca',
                  'q_INK',
                  'q_INS',
                  'q_MAR',
                  'q_CHI']



    def before_next_page(self):
        self.player.set_payoff()

page_sequence = [
    CognitiveReflectionTest,
    ratemo,
    big5,
    Demographics,

]
