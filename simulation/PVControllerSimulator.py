from mosaik_api import Simulator
from simulators.PVController import PVController
from typing import Dict
meta = {
    'models': {
        'PVController': {
            'public': False,
            'params': [],
            'attrs': 'current_output',
            'any_inputs': False
        }
    }
}


class PVSimulation(Simulator):
    def __init__(self):
        super().__init__(meta)
        self.simulator = Simulator(meta=meta)
        self.eid_prefix = 'PVController_'
        self.entities: Dict[str, PVController] = {}

    def init(self, sid, eid_prefix=None):
        if eid_prefix is not None:
            self.eid_prefix = eid_prefix
        return self.meta

    def create(self, num, model, **model_params):
        next_eid = len(self.entities)
        entities = []
        for i in range(next_eid, next_eid + num):
            eid = '%s%d' % (self.eid_prefix, i)
            model = PVController()
            entities.append({'eid': eid, 'model': model})
        return entities

    def step(self, time, inputs=None):
        """Requires data """
        for entity in self.entities.values():
            var = entity['model'].adjust_feedin_power(pvStatus=, P_set=)
        # TODO do calculation for each pv controller in the array here. Take care about switching off and on.
        return time + 60 # one minute later

    def get_data(self, outputs):
        # TODO Return feed in data as array? No idea.
        return {

        }