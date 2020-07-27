# -*- coding: utf-8 -*-
"""
Data classes for encapsulating information readings.
"""

__author__ = 'Lóránt Meszlényi'
__email__ = 'meszle01@ads.uni-passau.de'

from datetime import datetime
from dataclasses import dataclass

@dataclass
class BaseTimeInterval:
    valid_from: datetime = datetime.now()
    valid_until: datetime = datetime.now()

@dataclass
class GridVoltageReading(BaseTimeInterval):
    voltage: float = 0.0

@dataclass
class TimeIntervalPowerRequirement(BaseTimeInterval):
    power_requirement: int = 0

@dataclass
class GridPowerReading(BaseTimeInterval):
    current_feed_in: int = 0