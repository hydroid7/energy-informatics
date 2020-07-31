from interfaces.informationObjects import GridPowerReading
from interfaces.interfaces import AbstractPVController


class PVController(AbstractPVController):

    def get_real_feed_in(self) -> GridPowerReading:
        pass

    def set_grid_voltage(self):
        return 120

    def set_operation_state(self, feed_in=True) -> None:
        pass

    def adjust_real_power_output(self) -> None:
        pass
