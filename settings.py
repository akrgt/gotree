import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
DEBUG = False

OTREE_PRODUCTION = '1'

# don't share this with anybody.
SECRET_KEY = 'XXXXXXXXXX'


#XXXXXXXXXX部分は各個人に割り振られるキー．誰にも教えちゃいけない感じなので内緒．

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

environ['DATABASE_URL'] = 'postgres://postgres:XXXXXXXXXX@localhost:5433/django_db'

#XXXXXXXXXX部分はPostgresqlのパスワード．流石にここはごめんなさい．

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

AUTH_LEVEL = 'DEMO'

ADMIN_USERNAME = 'test'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'test'


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'ja'

#ついでに日本時間にしちゃいましょう．
TIME_ZONE = 'Asia/Tokyo'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'otreeutils']


DEMO_PAGE_TITLE="""【公開中】oTreeを用いた経済ゲーム実験環境"""


DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        このページは多摩大学経営情報学部の後藤晶（ごとうあきら）により運営されています．
        何かあればgoaki[at]me.comまでどうぞ．
    </li>
    <li>
        暫定版として公開しています．随時，整理等をしていきます．もし授業・研究等の目的で使われる場合は，前もってお知らせいただけると幸いです．
    </li>
    <li>
        社会科学におけるゲーム実験研究を促進するために公開しています．
    </li>
    <li>
        <a href="https://www.otree.org" target="_blank">oTree</a>により作成したものを公開しています．
    </li>
    
    
    <li>
        補足資料は<a href="https://www.slideshare.net/goaki/otree-102704688" target="_blank">コチラ</a>へ　
    </li>
    
    <li>
        随時更新していきます．また、一部にはカスタマイズしたものも掲載していますが、そのうち直します．
    </li>
    <li>
        なお，このサーバは「一般財団法人電気通信普及財団」による研究助成に基づき運営・公開されています．
    </li>
    <li>
        このサーバのすべてのサイトにアクセスするためにはユーザ名とパスワードが必要です．いずれも"test"です．
    </li>
</ul>

"""

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


# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.00,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}


SESSION_CONFIGS = [

    {
        'name': 'pggfg',
        'display_name': 'Fehr and Gaechterの20期処罰あり公共財ゲーム',
        'num_demo_participants': 3,
        'app_sequence': ['pggfg'],
    },
    {
        'name': 'pggfg5',
        'display_name': 'Fehr and Gaechterの5期処罰あり公共財ゲーム',
        'num_demo_participants': 3,
        'app_sequence': ['pggfg5'],
    },


    {
        'name': 'public_goods',
        'display_name': "公共財ゲーム",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods'],
    },

    {
        'name': 'repeat_public_goods',
        'display_name': "繰り返し公共財ゲーム",
        'num_demo_participants': 3,
        'app_sequence': ['repeat_public_goods'],
    },
    {
        'name': 'ind_info_and_exppublic_goods',
        'display_name': '個人情報と公共財ゲーム',
        'num_demo_participants': 3,
        'app_sequence': ['exppublic_goods', 'ind_info'],
    },
    {
        'name': 'expsvotree',
        'display_name': '社会的価値指向性（SVO）テスト',
        'num_demo_participants': 1,
        'app_sequence': ['svotree'],
    },
    {
        'name': 'dictator_ultimatum_non_strategy',
        'display_name': "独裁者と直接応答法による最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['dictator','ultimatum'],
        'treatment': 'direct_response',
    },
    {
        'name': 'dic_ult_tru_pub',
        'display_name': "独裁者，最終提案，信頼，公共財ゲーム",
        'num_demo_participants': 6,
        'app_sequence': ['dictator','ultimatum','trust', 'exppublic_goods'],
    },
    {
        'name': 'trust',
        'display_name': "信頼ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['trust'],
    },
    {
        'name': 'guess_two_thirds',
        'display_name': "美人コンテスト",
        'num_demo_participants': 3,
        'app_sequence': ['guess_two_thirds'],
    },
    {
        'name': 'survey',
        'display_name': "調査",
        'num_demo_participants': 1,
        'app_sequence': ['survey'],
    },
    {
        'name': 'quiz',
        'display_name': "クイズ",
        'num_demo_participants': 1,
        'app_sequence': ['quiz'],
    },
    {
        'name': 'prisoner',
        'display_name': "1回限り囚人のジレンマ",
        'num_demo_participants': 2,
        'app_sequence': ['prisoner'],
    },
    {
        'name': 'ultimatum',
        'display_name': "ストラテジーメソッドと直接応答法が混ざっている最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum'],
    },
    {
        'name': 'repeat_ultimatum',
        'display_name': "10期繰り返しストラテジーメソッドと直接応答法が混ざっている最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum'],
    },
    {
        'name': 'ultimatum_strategy',
        'display_name': "ストラテジーメソッドによる最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum'],
        'treatment': 'strategy',
    },
    {
        'name': 'repeat_ultimatum_strategy',
        'display_name': "10期繰り返しストラテジーメソッドによる最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum'],
        'treatment': 'repeat_strategy',
    },
    {
        'name': 'ultimatum_non_strategy',
        'display_name': "直接応答法による最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum'],
        'treatment': 'direct_response',
    },
    {
        'name': 'repeat_ultimatum_non_strategy',
        'display_name': "10期繰り返し直接応答法による最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum'],
        'treatment': 'repeat_direct_response',
    },
    {
        'name': 'vickrey_auction',
        'display_name': "Vickrey Auction",
        'num_demo_participants': 3,
        'app_sequence': ['vickrey_auction', 'payment_info'],
    },
    {
        'name': 'volunteer_dilemma',
        'display_name': "Volunteer's Dilemma",
        'num_demo_participants': 3,
        'app_sequence': ['volunteer_dilemma', 'payment_info'],
    },
    {
        'name': 'cournot',
        'display_name': "Cournot Competition",
        'num_demo_participants': 2,
        'app_sequence': [
            'cournot', 'payment_info'
        ],
    },
    {
        'name': 'principal_agent',
        'display_name': "Principal Agent",
        'num_demo_participants': 2,
        'app_sequence': ['principal_agent', 'payment_info'],
    },
    {
        'name': 'dictator',
        'display_name': "独裁者ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['dictator'],
    },


    {
        'name': 'repeat_dictator',
        'display_name': "10期繰り返し独裁者ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['dictator'],
    },
    {
        'name': 'matching_pennies',
        'display_name': "マッチングペニー",
        'num_demo_participants': 2,
        'app_sequence': [
            'matching_pennies',
        ],
    },
    {
        'name': 'traveler_dilemma',
        'display_name': "旅人のジレンマ",
        'num_demo_participants': 2,
        'app_sequence': ['traveler_dilemma', 'payment_info'],
    },
    {
        'name': 'bargaining',
        'display_name': "Bargaining Game",
        'num_demo_participants': 2,
        'app_sequence': ['bargaining', 'payment_info'],
    },
    {
        'name': 'common_value_auction',
        'display_name': "共通価値オークション",
        'num_demo_participants': 3,
        'app_sequence': ['common_value_auction'],
    },
    {
        'name': 'stackelberg',
        'display_name': "Stackelberg Competition",
        'real_world_currency_per_point': 0.01,
        'num_demo_participants': 2,
        'app_sequence': [
            'stackelberg', 'payment_info'
        ],
    },
    {
        'name': 'bertrand',
        'display_name': "Bertrand Competition",
        'num_demo_participants': 2,
        'app_sequence': [
            'bertrand', 'payment_info'
        ],
    },
    {
        'name': 'real_effort',
        'display_name': "Real-effort transcription task",
        'num_demo_participants': 1,
        'app_sequence': [
            'real_effort',
        ],
    },

    {
        'name': 'ret_typing',
        'display_name': "Real Effort Task - タイピング課題",
        'num_demo_participants': 1,
        'app_sequence': [
            'ret_typing',
        ],
        'ret_timer': 180,
        'showupfee': 30,
    },

    {
        'name': 'ret_adding',
        'display_name': "Real Effort Task - 足し算課題",
        'num_demo_participants': 1,
        'app_sequence': [
            'ret_adding',
        ],
        'ret_timer': 180,
        'showupfee': 30,
    },


    {
        'name': 'lemon_market',
        'display_name': "Lemon-Market Game",
        'num_demo_participants': 3,
        'app_sequence': [
            'lemon_market'
        ],
    },
    {
        'name': 'battle_of_the_sexes',
        'display_name': "男女の闘い",
        'num_demo_participants': 2,
        'app_sequence': [
            'battle_of_the_sexes', 'payment_info'
        ],
    },
    {
        'name': 'public_goods_simple',
        'display_name': "練習用の単純な公共財ゲーム",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods_simple', 'survey', 'payment_info'],
    },
    {
        'name': 'trust_simple',
        'display_name': "練習用の単純な信頼ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['trust_simple'],
    },



    {
        'name': 'repeat_prisoner',
        'display_name': "繰り返し囚人のジレンマ(10回)",
        'num_demo_participants': 2,
        'app_sequence': ['repeat_prisoner'],

    },

    {
        'name': 'three_ultimatum',
        'display_name': '三人独裁者ゲーム',
        'num_demo_participants': 3,
        'app_sequence': ['three_ultimatum'],
    },
    {
        'name': 'ind_info',
        'display_name': '個人情報',
        'num_demo_participants': 1,
        'app_sequence': ['ind_info'],
    },

    {
        'name': 'svotree',
        'display_name': '社会的価値指向性（SVO）テスト',
        'num_demo_participants': 1,
        'app_sequence': ['svotree'],
    },

    {
        'name': 'svotree2',
        'display_name': '社会的価値指向性（SVO）テストDiscrete',
        'num_demo_participants': 1,
        'app_sequence': ['svotree2'],
    },

    {
        'name': 'ind_info_and_svotree',
        'display_name': '個人情報と社会的価値指向性（SVO）テスト',
        'num_demo_participants': 1,
        'app_sequence': ['svotree', 'ind_info'],
    },
     {
        'name': 'iat',
        'display_name': 'Implicit Association Test',
        'num_demo_participants': 1,
        'app_sequence': ['iat'],
    },
    {
        'name': 'FW_disaster',
        'display_name': '災害経験',
        'num_demo_participants': 1,
        'app_sequence': ['FW_disaster'],
    }


]





# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
