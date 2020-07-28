# -*- coding: utf-8 -*-
"""
Abstract component classes for each SGAM component definition.
"""

__author__ = 'Lóránt Meszlényi'
__email__ = 'meszle01@ads.uni-passau.de'

from abc import ABC, abstractmethod
from informationObjects import GridVoltageReading, TimeIntervalPowerRequirement, GridPowerReading
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


class AbstractLocalMeasurementDevice(AbstractSimulationObject):
    """Device Placed at the connection point of the PV System and the power grid."""

    @abstractmethod
    def read_grid_voltage(self) -> GridVoltageReading:
        """Reads the current local grid voltage"""
        pass

    @abstractmethod
    def read_real_feed_in(self) -> GridPowerReading:
        """Reads the current grid feed in"""
        pass


class AbstractEnergyMarketSystem(AbstractSimulationObject):
    """System that communicates the required amount of electric power"""

    @abstractmethod
    def read_required_energy(self) -> TimeIntervalPowerRequirement:
        """Determines the required amount of energy"""
        pass


class AbstractVPPServer(AbstractSimulationObject):
    """Component that is responsible for the switching of PV systems dependent of the needs of the energy market."""

    @abstractmethod
    def read_power_requirement(self) -> TimeIntervalPowerRequirement:
        pass

    @abstractmethod
    def calculate_feed_in(self):
        """Reads the current feed-in power accumulated across all PV controllers."""
        pass

    @abstractmethod
    def set_pv_setpoints(self) -> None:
        """Sets its assigned PV Controllers to the determined value."""
        pass


class AbstractPVController(AbstractSimulationObject):
    """
    Component responsible for switching on/off the PV system. It also adjust the real power output according the local
    voltage reads.
    """

    @abstractmethod
    def adjust_real_power_output(self) -> None:
        """Adjust real power output based on grid conditions."""
        pass

    @abstractmethod
    def set_operation_state(self, feed_in=True) -> None:
        """Sets the controllers state to either "Feed-in" or "Disabled" """
        pass
