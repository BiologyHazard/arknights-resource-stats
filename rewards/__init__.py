from models import ResourceStats

from .annihilation import *
from .check_in import *
from .daily_weekly_monthly import *
from .dev_news import *
from .event import *
from .integrated_strategies import *
from .intelligence_store import *
from .limited_gacha_gift import *
from .login import *
from .lucky_wall import *
from .mail_box import *
from .manager import manager
from .reclamation_algorithm import *
from .recurit_refresh import *
from .stationary_security_service import *
from .trials_for_navigator import *
from .zone_record import *


def add_rewards(resource_stats: ResourceStats):
    for function in manager:
        function(resource_stats)
