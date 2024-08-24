from .annihilation import *
from .check_in import *
from .integrated_strategies import *
from .intelligence_store import *
from .limited_gacha_gift import *
from .login import *
from .lucky_wall import *
from .manager import *
from .reclamation_algorithm import *
from .recurit_refresh import *
from .sidestory import *
from .trials_for_navigator import *
from .zone_record import *


def add_rewards(resource_stats: ResourceStats):
    for function in manager:
        function(resource_stats)
