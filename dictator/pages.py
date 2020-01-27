from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    timeout_seconds = 100
    pass


class Offer(Page):
    timeout_seconds = 30
    form_model = models.Group
    form_fields = ['kept']

    def is_displayed(self):
        return self.player.id_in_group == 1


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def vars_for_template(self):
        if self.player.id_in_group == 2:
            body_text = "あなたはプレイヤー2です．プレイヤー1の決定をお待ち下さい．"
        else:
            body_text = 'しばらくお待ち下さい．'
        return {'body_text': body_text}


class Results(Page):
    def vars_for_template(self):
        return {
            'offer': Constants.endowment - self.group.kept,
        }


page_sequence = [
    Introduction,
    Offer,
    ResultsWaitPage,
    Results
]
