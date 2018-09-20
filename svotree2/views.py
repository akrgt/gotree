from . import models
from ._builtin import Page, WaitPage
from .functions import slider, tdm9
from otree.api import Currency as c, currency_range
from .models import Constants

class ViewSliderPrimaryDiscreteInstructions(Page):
    def before_next_page(self):
        self.player.set_payoff()

class SliderPrimaryDiscrete(Page):
    def before_next_page(self):
        self.player.set_payoff()

    form_model = models.Player
    form_fields = ['slider1',
                   'slider2',
                   'slider3',
                   'slider4',
                   'slider5',
                   'slider6',
                   'slider7',
                   'slider8',
                   'slider9',
                   'slider10',
                   'slider11',
                   'slider12',
                   'slider13',
                   'slider14',
                   'slider15',
                ]

    def vars_for_template(self):
        return {'slider_items': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]}

    def before_next_page(self):
        chosen_values = {
            'item1': self.player.slider1,
            'item2': self.player.slider2,
            'item3': self.player.slider3,
            'item4': self.player.slider4,
            'item5': self.player.slider5,
            'item6': self.player.slider6,
            'item7': self.player.slider7,
            'item8': self.player.slider8,
            'item9': self.player.slider9,
            'item10': self.player.slider10,
            'item11': self.player.slider11,
            'item12': self.player.slider12,
            'item13': self.player.slider13,
            'item14': self.player.slider14,
            'item15': self.player.slider15
        }
        mean_allocations = slider.mean_allocations_discrete(chosen_values)
        svo_slider_angle = slider.svo_angle(mean_allocations['self'], mean_allocations['other'])
        self.player.slider_angle = svo_slider_angle
        self.player.slider_classification = slider.svo_classification(svo_slider_angle)

class ViewSliderPrimaryContinuous(Page):
    def before_next_page(self):
        self.player.set_payoff()

class SliderPrimaryContinuous(Page):

    form_model = models.Player
    form_fields = ['slider1',
                   'slider2',
                   'slider3',
                   'slider4',
                   'slider5',
                   'slider6',
                   'slider7',
                   'slider8',
                   'slider9',
                   'slider10',
                   'slider11',
                   'slider12',
                   'slider13',
                   'slider14',
                   'slider15',
                ]

    def vars_for_template(self):
        return {'slider_items': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]}

    def before_next_page(self):
        chosen_values = {
            'item1': self.player.slider1,
            'item2': self.player.slider2,
            'item3': self.player.slider3,
            'item4': self.player.slider4,
            'item5': self.player.slider5,
            'item6': self.player.slider6,
            'item7': self.player.slider7,
            'item8': self.player.slider8,
            'item9': self.player.slider9,
            'item10': self.player.slider10,
            'item11': self.player.slider11,
            'item12': self.player.slider12,
            'item13': self.player.slider13,
            'item14': self.player.slider14,
            'item15': self.player.slider15
        }
        mean_allocations = slider.mean_allocations_continuous(chosen_values)
        svo_slider_angle = slider.svo_angle(mean_allocations['self'], mean_allocations['other'])
        self.player.slider_angle = svo_slider_angle
        self.player.slider_classification = slider.svo_classification(svo_slider_angle)


class ViewNineItemTDMInstructions(Page):
    def before_next_page(self):
        self.player.set_payoff()

class ViewSliderPrimaryContinuousInstructions(Page):
    def before_next_page(self):
        self.player.set_payoff()


class NineItemTDM(Page):

    form_model = models.Player
    form_fields = [
        "nine_item_tdm_1",
        "nine_item_tdm_2",
        "nine_item_tdm_3",
        "nine_item_tdm_4",
        "nine_item_tdm_5",
        "nine_item_tdm_6",
        "nine_item_tdm_7",
        "nine_item_tdm_8",
        "nine_item_tdm_9",
    ]

    def vars_for_template(self):

        return {'nine_item_tdm_decisions': tdm9.decisions}

    def before_next_page(self):
        chosen_values = {
            1: self.player.nine_item_tdm_1,
            2: self.player.nine_item_tdm_2,
            3: self.player.nine_item_tdm_3,
            4: self.player.nine_item_tdm_4,
            5: self.player.nine_item_tdm_5,
            6: self.player.nine_item_tdm_6,
            7: self.player.nine_item_tdm_7,
            8: self.player.nine_item_tdm_8,
            9: self.player.nine_item_tdm_9
        }

        self.player.nine_item_tdm_prosocial = tdm9.count_decisions_of_type("Prosocial", chosen_values)
        self.player.nine_item_tdm_individualistic = tdm9.count_decisions_of_type("Individualistic", chosen_values)
        self.player.nine_item_tdm_competitive = tdm9.count_decisions_of_type("Competitive", chosen_values)

        self.player.nine_item_tdm_classification = tdm9.svo_type(chosen_values)




class RingMeasure(Page):

    form_model = models.Player
    form_fields = [
        "ring_measure_1",
        "ring_measure_2",
        "ring_measure_3",
        "ring_measure_4",
        "ring_measure_5",
        "ring_measure_6",
        "ring_measure_7",
        "ring_measure_8",
        "ring_measure_9",
        "ring_measure_10",
        "ring_measure_11",
        "ring_measure_12",
        "ring_measure_13",
        "ring_measure_14",
        "ring_measure_15",
        "ring_measure_16",
        "ring_measure_17",
        "ring_measure_18",
        "ring_measure_19",
        "ring_measure_20",
        "ring_measure_21",
        "ring_measure_22",
        "ring_measure_23",
        "ring_measure_24"
    ]



class DebugDisplayPage(Page):

    def vars_for_template(self):
        return {'angle': self.player.slider_angle, 'classification_slider': self.player.slider_classification, 'tdm_prosocial': self.player.nine_item_tdm_prosocial, 'tdm_individualistic': self.player.nine_item_tdm_individualistic, 'tdm_competitive': self.player.nine_item_tdm_competitive, 'classification_tdm': self.player.nine_item_tdm_classification}

page_sequence = [
    ViewNineItemTDMInstructions,
    NineItemTDM,
    ViewSliderPrimaryDiscreteInstructions,
    SliderPrimaryDiscrete,
]

'''
page_sequence = [
    NineItemTDM,
    DebugDisplayPage,
    RingMeasure,
    SliderPrimaryDiscrete,
    DebugDisplayPage,
    SliderPrimaryContinuous,
    DebugDisplayPage,
]
'''