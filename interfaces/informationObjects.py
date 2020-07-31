# -*- coding: utf-8 -*-
"""
Data classes for encapsulating information readings.
"""

__author__ = 'Lóránt Meszlényi'
__email__ = 'meszle01@ads.uni-passau.de'

from datetime import datetime
from dataclasses import dataclass
from typing import List
from functools import reduce


@dataclass
class GridVoltageReading:
    voltage: float = 0.0


@dataclass
class MarketPowerRequirement:
    """Power requirement of the market in W/h / 0.25 h"""
    power_requirement: int = 0

    def power_requirement_per_minute(self):
        return self.power_requirement / 15


@dataclass
class PowerFeedIn:
    pv_plants: List[int]

    def total_feed_in(self):
        return reduce(lambda a, b: a + b, self.pv_plants)

    def index_max_feeder(self):
        return self.pv_plants.index(max(self.pv_plants))
