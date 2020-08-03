#Realized by Nahla and Karim

from interfaces.informationObjects import GridPowerReading
from interfaces.interfaces import AbstractPVController


class PVController(AbstractPVController):

    def __init__(self):
        self.U_nom = 230.0
        self.P_peak = 10000
        self.activeState = None


    def _max_power(self):
        value_max = (1.1 * self.U_nom);
        return value_max

    def _min_power(self):
        value_min = (1.05 * self.U_nom);
        return value_min

    def _linear_curve_equation(self, U_I):
        value_mid = (22 - 20 * (U_I/self.U_nom));
        return value_mid

    def adjust_real_power_output(self, U_I):
        """Adjust real power output based on grid conditions."""

        if U_I > self._max_power():
            P_set = 0;
        elif U_I < self._min_power():
            P_set = self.P_peak;
        else:
            P_set =  self.P_peak * self._linear_curve_equation(U_I);
        return P_set

    def _active_operation_state(self, pvStatus):
        if self.activeState == True:
            pvStatus == 1;
        else:
            pvStatus == 0;
        return pvStatus

    def adjust_feedin_power(self, pvStatus, P_set):
        """Adjust feed in power output based on P_set and PV status."""
        if self._active_operation_state(pvStatus):
            P_feedin = P_set;
        else:
            P_feedin = 0;
        return P_feedin

    def get_result(self):
        data = self.adjust_feedin_power();
        return data

