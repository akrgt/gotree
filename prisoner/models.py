from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
これは一回限りの囚人のジレンマゲームです．2人のプレイヤーが別々に協力をしたいか，裏切りたいかを聞かれます．
彼らの選択は利益に直結します．
This is a one-shot "Prisoner's Dilemma". Two players are asked separately
whether they want to cooperate or defect. Their choices directly determine the
payoffs.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoner'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'prisoner/Instructions.html'

    # payoff if 1 player defects and the other cooperates""",
    betray_payoff = c(300)
    betrayed_payoff = c(0)

    # payoff if both players cooperate or both defect
    both_cooperate_payoff = c(200)
    both_defect_payoff = c(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.CharField(
        choices=['協力', '裏切り'],
        doc="""このプレイヤーの決定""",
        widget=widgets.RadioSelect()
    )

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):
        points_matrix = {'協力': {'協力': Constants.both_cooperate_payoff,
                                       '裏切り': Constants.betrayed_payoff},
                         '裏切り': {
                             '協力': Constants.betray_payoff,
                             '裏切り': Constants.both_defect_payoff}}

        self.payoff = (points_matrix[self.decision]
                       [self.other_player().decision])
