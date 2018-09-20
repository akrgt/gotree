""""
Ring Measure Computation function
"""

decisions = [
    {'number': 1, 'A': {'self': 390, 'other': -1450}, 'B': {'self': 0, 'other': -1500}},
    {'number': 2, 'A': {'self': -1450, 'other': 390}, 'B': {'self': -1500, 'other': 0}},
    {'number': 3, 'A': {'self': -1500, 'other': 0}, 'B': {'self': -1450, 'other': -390}},
    {'number': 4, 'A': {'self': -1450, 'other': 390}, 'B': {'self': -1300, 'other': 750}},
    {'number': 5, 'A': {'self': -390, 'other': -1450}, 'B': {'self': -750, 'other': -1300}},
    {'number': 6, 'A': {'self': -750, 'other': 1300}, 'B': {'self': 1060, 'other': 1060}},
    {'number': 7, 'A': {'self': 750, 'other': -1300}, 'B': {'self': 1060, 'other': -1060}},
    {'number': 8, 'A': {'self': -1300, 'other': 750}, 'B': {'self': -1060, 'other': 1060}},
    {'number': 9, 'A': {'self': 1300, 'other': 750}, 'B': {'self': 1060, 'other': 1060}},
    {'number': 10, 'A': {'self': -1060, 'other': -1060}, 'B': {'self': -750, 'other': -1300}},
    {'number': 11, 'A': {'self': -1300, 'other': -750}, 'B': {'self': -1450, 'other': -390}},
    {'number': 12, 'A': {'self': -1060, 'other': 1060}, 'B': {'self': -750, 'other': 1300}},
    {'number': 13, 'A': {'self': 1450, 'other': -390}, 'B': {'self': 1500, 'other': 0}},
    {'number': 14, 'A': {'self': -390, 'other': 1450}, 'B': {'self': -750, 'other': 1300}},
    {'number': 15, 'A': {'self': 1300, 'other': -750}, 'B': {'self': 1060, 'other': -1060}},
    {'number': 16, 'A': {'self': -390, 'other': 1450}, 'B': {'self': 0, 'other': 1500}},
    {'number': 17, 'A': {'self': 1450, 'other': -390}, 'B': {'self': 1300, 'other': -750}},
    {'number': 18, 'A': {'self': 1450, 'other': 390}, 'B': {'self': 1300, 'other': 750}},
    {'number': 19, 'A': {'self': 390, 'other': -1450}, 'B': {'self': 750, 'other': 1300}},
    {'number': 20, 'A': {'self': 1450, 'other': 390}, 'B': {'self': 1500, 'other': 0}},
    {'number': 21, 'A': {'self': 390, 'other': 1450}, 'B': {'self': 750, 'other': 1300}},
    {'number': 22, 'A': {'self': -390, 'other': -1450}, 'B': {'self': 0, 'other': -1500}},
    {'number': 23, 'A': {'self': -1300, 'other': -750}, 'B': {'self': -1060, 'other': -1060}},
    {'number': 24, 'A': {'self': 390, 'other': 1450}, 'B': {'self': 0, 'other': 1500}}
]


