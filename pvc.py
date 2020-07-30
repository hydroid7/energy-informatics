#realized by Nahla and Karim

class pvController:

    def __init__(self):
        self.U_nom = 230.0
        self.P_peak = 10.0

    def adjust_real_power_output(self, U_I):
        """Adjust real power output based on grid conditions."""

        if U_I > (1.1 * self.U_nom):
            P_set = 0;
        elif U_I < (1.05 * self.U_nom):
            P_set = self.P_peak;
        else:
            P_set =  self.P_peak * (22 - 20 * (U_I/self.U_nom));
        return P_set

    def adjust_feedin_power(self, pvStatus, P_set):
        """Adjust feed in power output based on P_set and PV status."""
        if pvStatus == 0:
            P_feedin = 0;
        else:
            P_feedin = P_set;
        return P_feedin

    def get_result(self):
        data = self.adjust_feedin_power();
        return data
