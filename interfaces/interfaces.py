# -*- coding: utf-8 -*-
"""
Abstract component classes for each SGAM component definition.
"""

__author__ = 'Lóránt Meszlényi'
__email__ = 'meszle01@ads.uni-passau.de'

from abc import ABC, abstractmethod
from interfaces.informationObjects import TimeIntervalPowerRequirement, GridPowerReading
from mosaik_api import Simulator


class AbstractSimulationObject(ABC, Simulator):
    """Abstract class for a simulation object."""

    @abstractmethod
    def init(self, sid, **sim_params):
        """Creates the simulation instance with the arguments."""
        pass

    @abstractmethod
    def create(self, num, model, **model_params):
        pass

    @abstractmethod
    def step(self, time, inputs):
        """Runs the simulation instance in a simulation step."""
        pass

    @abstractmethod
    def get_data(self, outputs) -> dict:
        pass


class AbstractVPPServer(AbstractSimulationObject):
    """Component that is responsible for the switching of PV systems dependent of the needs of the energy market."""

    @abstractmethod
    def set_market_energy_requirement(self, requirements: TimeIntervalPowerRequirement):
        pass

    """Calculates the setpoint for the PV controllers."""
    @abstractmethod
    def get_pv_setpoints(self):
        pass


class AbstractPVController(AbstractSimulationObject):
    """
    Component responsible for switching on/off the PV system. It also adjust the real power output according the local
    voltage reads and communicates the real power output to the VPPServer.
    """

    @abstractmethod
    def adjust_real_power_output(self) -> None:
        """Adjust real power output based on grid conditions."""
        pass

    @abstractmethod
    def set_grid_voltage(self):
        pass

    @abstractmethod
    def set_operation_state(self, feed_in=True) -> None:
        """Sets the controllers state to either "Feed-in" or "Disabled" """
        pass

    @abstractmethod
    def get_real_feed_in(self) -> GridPowerReading:
        """Reads the current grid feed in"""
        pass
