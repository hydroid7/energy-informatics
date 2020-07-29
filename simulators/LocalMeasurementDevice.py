from interfaces.informationObjects import GridPowerReading, GridVoltageReading
from interfaces.interfaces import AbstractLocalMeasurementDevice

meta = {
    'models': {
        'LocalMeasurementDevice': {
            'public': True,
            'params': ['value'],
            'attrs': 'val'
        }
    }
}


class LocalMeasurementDevice(AbstractLocalMeasurementDevice):

    def read_grid_voltage(self) -> GridVoltageReading:
        pass

    def read_real_feed_in(self) -> GridPowerReading:
        pass

    def init(self, sid, **sim_params):
        pass

    def create(self, num, model, **model_params):
        pass

    def step(self, time, inputs):
        pass

    def get_data(self, outputs) -> dict:
        pass
