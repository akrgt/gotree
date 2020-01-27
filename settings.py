from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.00,
    participation_fee=0.00,
    doc="",
)

SESSION_CONFIGS = [
    {
        'name': 'lemon_market',
        'display_name': "(改)Lemon-Market Game",
        'num_demo_participants': 3,
        'app_sequence': [
            'lemon_market2'
        ],
    },
    {
        'name': 'principal_agent',
        'display_name': "(改)Principal Agent",
        'num_demo_participants': 2,
        'app_sequence': ['principal_agent', 'payment_info'],
    },
    {
        'name': 'svotree2',
        'display_name': '(改)社会的価値指向性（SVO）テストDiscrete',
        'num_demo_participants': 1,
        'app_sequence': ['svotree2'],
    },
    {
        'name': 'vickrey_auction',
        'display_name': "(改)Vickrey Auction",
        'num_demo_participants': 3,
        'app_sequence': ['vickrey_auction', 'payment_info'],
    },
    {
        'name': 'dic_ult_tru_pub',
        'display_name': "(未改変)独裁者，最終提案，信頼，公共財ゲーム",
        'num_demo_participants': 6,
        'app_sequence': ['dictator', 'ultimatum', 'trust', 'exppublic_goods'],
    },
    {
        'name': 'svo',
        'display_name': "(未改変)Social Value Orientation",
        'num_demo_participants': 4,
        'app_sequence': ['svo'],
    },
    {
        'name': 'public_goods',
        'display_name': "(未改変)公共財ゲーム",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods'],
    },
    {
        'name': 'repeat_public_goods',
        'display_name': "(未改変)繰り返し公共財ゲーム",
        'num_demo_participants': 3,
        'app_sequence': ['repeat_public_goods'],
    },
    {
        'name': 'ind_info_and_exppublic_goods',
        'display_name': '(未改変)個人情報と公共財ゲーム',
        'num_demo_participants': 3,
        'app_sequence': ['exppublic_goods', 'ind_info'],
    },
    {
        'name': 'guess_two_thirds',
        'display_name': "(未改変)美人コンテスト",
        'num_demo_participants': 3,
        'app_sequence': ['guess_two_thirds'],
    },
    {
        'name': 'volunteer_dilemma',
        'display_name': "(未改変)Volunteer's Dilemma",
        'num_demo_participants': 3,
        'app_sequence': ['volunteer_dilemma', 'payment_info'],
    },
    {
        'name': 'common_value_auction',
        'display_name': "(未改変)共通価値オークション",
        'num_demo_participants': 3,
        'app_sequence': ['common_value_auction'],
    },
    {
        'name': 'public_goods_simple',
        'display_name': "(未改変)練習用の単純な公共財ゲーム",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods_simple', 'survey', 'payment_info'],
    },
    {
        'name': 'three_ultimatum',
        'display_name': '(未改変)三人独裁者ゲーム',
        'num_demo_participants': 3,
        'app_sequence': ['three_ultimatum'],
    },
    {
        'name': 'trust_simple',
        'display_name': "(改)練習用の単純な信頼ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['trust_simple'],
    },
    {
        'name': 'trust',
        'display_name': "(未改変)信頼ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['trust'],
    },
    {
        'name': 'dictator_ultimatum_non_strategy',
        'display_name': "(未改変)独裁者と直接応答法による最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['dictator', 'ultimatum'],
        'treatment': 'direct_response',
    },
    {
        'name': 'ultimatum',
        'display_name': "(未改変)ストラテジーメソッドと直接応答法が混ざっている最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum'],
    },
    {
        'name': 'repeat_ultimatum',
        'display_name': "(改)10期繰り返しストラテジーメソッドと直接応答法が混ざっている最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum10'],
    },
    {
        'name': 'ultimatum_strategy',
        'display_name': "(未改変)ストラテジーメソッドによる最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum'],
        'treatment': 'strategy',
    },
    {
        'name': 'repeat_ultimatum_strategy',
        'display_name': "(改)10期繰り返しストラテジーメソッドによる最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum10'],
        'treatment': 'repeat_strategy',
    },
    {
        'name': 'ultimatum_non_strategy',
        'display_name': "(未改変)直接応答法による最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum'],
        'treatment': 'direct_response',
    },
    {
        'name': 'repeat_ultimatum_non_strategy',
        'display_name': "(改)10期繰り返し直接応答法による最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum10'],
        'treatment': 'repeat_direct_response',
    },
    {
        'name': 'cournot',
        'display_name': "(未改変)Cournot Competition",
        'num_demo_participants': 2,
        'app_sequence': [
            'cournot', 'payment_info'
        ],
    },
    {
        'name': 'repeat_dictator',
        'display_name': "(改)10期繰り返し独裁者ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['dictator10'],
    },
    {
        'name': 'dictator',
        'display_name': "(改)独裁者ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['dictator'],
    },
    {
        'name': 'matching_pennies',
        'display_name': "(未改変)マッチングペニー",
        'num_demo_participants': 2,
        'app_sequence': [
            'matching_pennies',
        ],
    },
    {
        'name': 'traveler_dilemma',
        'display_name': "(未改変)旅人のジレンマ",
        'num_demo_participants': 2,
        'app_sequence': ['traveler_dilemma', 'payment_info'],
    },
    {
        'name': 'bargaining',
        'display_name': "(未改変)Bargaining Game",
        'num_demo_participants': 2,
        'app_sequence': ['bargaining', 'payment_info'],
    },
    {
        'name': 'stackelberg',
        'display_name': "(未改変)Stackelberg Competition",
        'real_world_currency_per_point': 0.01,
        'num_demo_participants': 2,
        'app_sequence': [
            'stackelberg', 'payment_info'
        ],
    },
    {
        'name': 'bertrand',
        'display_name': "(未改変)Bertrand Competition",
        'num_demo_participants': 2,
        'app_sequence': [
            'bertrand', 'payment_info'
        ],
    },
    {
        'name': 'prisoner',
        'display_name': "(未改変)1回限り囚人のジレンマ",
        'num_demo_participants': 2,
        'app_sequence': ['prisoner'],
    },
    {
        'name': 'repeat_prisoner',
        'display_name': "(改)繰り返し囚人のジレンマ(10回)",
        'num_demo_participants': 2,
        'app_sequence': ['repeat_prisoner'],
    },
    {
        'name': 'battle_of_the_sexes',
        'display_name': "(未改変)男女の闘い",
        'num_demo_participants': 2,
        'app_sequence': [
            'battle_of_the_sexes', 'payment_info'
        ],
    },
    {
        'name': 'real_effort',
        'display_name': "(改)Real-effort transcription task",
        'num_demo_participants': 1,
        'app_sequence': ['real_effort'],
    },
    {
        'name': 'survey',
        'display_name': "(改)調査",
        'num_demo_participants': 1,
        'app_sequence': ['survey'],
    },
    {
        'name': 'ret_typing',
        'display_name': "(改)Real Effort Task - タイピング課題",
        'num_demo_participants': 1,
        'app_sequence': [
            'ret_typing',
        ],
        'ret_timer': 180,
        'showupfee': 30,
    },
    {
        'name': 'ret_adding',
        'display_name': "(改)Real Effort Task - 足し算課題",
        'num_demo_participants': 1,
        'app_sequence': [
            'ret_adding',
        ],
        'ret_timer': 180,
        'showupfee': 30,
    },
    {
        'name': 'ind_info',
        'display_name': '(未改変)個人情報',
        'num_demo_participants': 1,
        'app_sequence': ['ind_info'],
    },
    {
        'name': 'svotree',
        'display_name': '(未改変)社会的価値指向性（SVO）テスト',
        'num_demo_participants': 1,
        'app_sequence': ['svotree'],
    },
    {
        'name': 'ind_info_and_svotree',
        'display_name': '(未改変)個人情報と社会的価値指向性（SVO）テスト',
        'num_demo_participants': 1,
        'app_sequence': ['svotree', 'ind_info'],
    },
    {
        'name': 'expsvotree',
        'display_name': '(未改変)社会的価値指向性（SVO）テスト',
        'num_demo_participants': 1,
        'app_sequence': ['svotree'],
    },
    {
        'name': 'pggfg',
        'display_name': '(改)Fehr and Gaechterの20期処罰あり公共財ゲーム',
        # 'display_name': 'Fehr and Gaechterの20期処罰あり公共財ゲーム',
        'num_demo_participants': 3,
        'app_sequence': ['pggfg'],
    },
    {
        'name': 'pggfg5',
        'display_name': '(改)Fehr and Gaechterの5期処罰あり公共財ゲーム',
        # 'display_name': 'Fehr and Gaechterの5期処罰あり公共財ゲーム',
        'num_demo_participants': 3,
        'app_sequence': ['pggfg5'],
    },
    {
        'name': 'FW_disaster',
        'display_name': '(未改変)災害経験',
        'num_demo_participants': 1,
        'app_sequence': ['FW_disaster'],
    },
    {
        'name': 'iat',
        'display_name': 'Implicit Association Test',
        'num_demo_participants': 1,
        'app_sequence': ['iat'],
    },

]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },

    {
        'name': 'TRIAL',
        'display_name': 'トライアル用，50名まで対応',
        'participant_label_file': '_rooms/TRIAL.txt',
    },
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
        test server for "明治大学行動経済学研究所"
<ul>
    <li>
        oTreeの改修中です.
    </li>
    <li>
        何らかの改変を行ったプログラムは先頭に「(改)」を、<BR>
        改変を行わなかった場合は「（未改変）」をそれぞれ付けています.
</ul>

"""

# don't share this with anybody.
SECRET_KEY = '6lertt4wlb09zj@4wyuy-p-6)i$vh!ljwx&r9bti6kgw54k-h8'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# inactive session configs
# dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
# dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
#      app_sequence=['prisoner', 'payment_info']),
# dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
#      app_sequence=['volunteer_dilemma', 'payment_info']),
# dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
#     'cournot', 'payment_info'
# ]),
# dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
#      app_sequence=['dictator', 'payment_info']),
# dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
#     'matching_pennies',
# ]),
# dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
#      app_sequence=['traveler_dilemma', 'payment_info']),
# dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
#      app_sequence=['bargaining', 'payment_info']),
# dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
#      app_sequence=['common_value_auction', 'payment_info']),
# dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
#     'bertrand', 'payment_info'
# ]),
# dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
#      num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
# dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
#      app_sequence=['trust_simple']),
