from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'svotree2'
    players_per_group = None
    num_rounds = 1

    instructions_slider = 'svotree2/SliderInstructions.html'
    instructions_9tdm = 'svotree2/NineItemTDMInstructions.html'
    instructions_rm = 'svotree2/RingMeasureInstructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_payoff(self):
        """Calculate payoff, to be implemented later """
        self.payoff = 0

    slider1 = models.FloatField()
    slider2 = models.FloatField()
    slider3 = models.FloatField()
    slider4 = models.FloatField()
    slider5 = models.FloatField()
    slider6 = models.FloatField()
    slider_angle = models.DecimalField(decimal_places=2, max_digits=5)
    slider_classification = models.CharField()
    slider7 = models.FloatField()
    slider8 = models.FloatField()
    slider9 = models.FloatField()
    slider10 = models.FloatField()
    slider11 = models.FloatField()
    slider12 = models.FloatField()
    slider13 = models.FloatField()
    slider14 = models.FloatField()
    slider15 = models.FloatField()

    nine_item_tdm_1 = models.CharField()
    nine_item_tdm_2 = models.CharField()
    nine_item_tdm_3 = models.CharField()
    nine_item_tdm_4 = models.CharField()
    nine_item_tdm_5 = models.CharField()
    nine_item_tdm_6 = models.CharField()
    nine_item_tdm_7 = models.CharField()
    nine_item_tdm_8 = models.CharField()
    nine_item_tdm_9 = models.CharField()
    nine_item_tdm_prosocial = models.IntegerField()
    nine_item_tdm_individualistic = models.IntegerField()
    nine_item_tdm_competitive = models.IntegerField()
    nine_item_tdm_classification = models.CharField()

    ring_measure_1 = models.CharField()
    ring_measure_2 = models.CharField()
    ring_measure_3 = models.CharField()
    ring_measure_4 = models.CharField()
    ring_measure_5 = models.CharField()
    ring_measure_6 = models.CharField()
    ring_measure_7 = models.CharField()
    ring_measure_8 = models.CharField()
    ring_measure_9 = models.CharField()
    ring_measure_10 = models.CharField()
    ring_measure_11 = models.CharField()
    ring_measure_12 = models.CharField()
    ring_measure_13 = models.CharField()
    ring_measure_14 = models.CharField()
    ring_measure_15 = models.CharField()
    ring_measure_16 = models.CharField()
    ring_measure_17 = models.CharField()
    ring_measure_18 = models.CharField()
    ring_measure_19 = models.CharField()
    ring_measure_20 = models.CharField()
    ring_measure_21 = models.CharField()
    ring_measure_22 = models.CharField()
    ring_measure_23 = models.CharField()
    ring_measure_24 = models.CharField()

