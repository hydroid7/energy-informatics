
import random
from mosaik.util import connect_randomly, connect_many_to_one
import mosaik

SIM_CONFIG = {
    'CSV': {
        'python': 'mosaik_csv:CSV',
    },
    'DB': {
        'cmd': 'mosaik-hdf5 %(addr)s',
    },
    'CMD': {
        'python': 'console-sim:Console'
    },
    'CONST': {
        'python': 'constant-sim:Constant'
    },
    'VPPServer': {
        'python': 'simulators.VPPServer:VPPServer',
    },
    'HouseholdSim': {
        'python': 'householdsim.mosaik:HouseholdSim',
    },
    'HHConstantSim': {
        'python': 'simulators.HHConstantSim:HHConstantSim',
    }, #uses HHConstantSim simulator for the constant variables
    'PVController': {
        'python': 'simulator.PVController:PVController',
    },
    'PyPower': {
        'python': 'mosaik_pypower.mosaik:PyPower',
    }
}
START = '24-01-01 00:00:00'
END = 24 * 3600  # 1 day
PV_DATA = 'data/pv_10kw.csv'
PV_CONST_DATA = 'data/pv_constant.csv'
ENERGY_REQUIREMENTS_FILE = 'data/market.csv'
ENERGY_REQUIREMENTS_CONST_FILE = 'data/market_constant.csv'
PROFILE_FILE = 'data/profiles.data.gz'
GRID_NAME = 'demo_lv_grid'
GRID_FILE = 'data/%s.json' % GRID_NAME
PV_PEAK = 10000
NUMBER_OF_PV_PLANTS = 10


def main():
    change_parameter=["adjust_feedin", "adjust_market_requirements", "adjust_hh_demand"] #parameters to be changed
    random.seed(24)
    world = mosaik.World(SIM_CONFIG)
    for parameter in change_parameter: #run three different scenarios
        scenarios = create_scenario(world,parameter)
        runs = world.run(until=END, rt_factor=1 / 3600)
    print(scenarios) #print the result of the three different scenarios


def create_scenario(world,parameter):
    # start simulators
    # check the constant and the variable parameters
    if parameter == "adjust_feedin":
        pvsim = world.start('CSV', sim_start=START, datafile=PV_DATA)
    else:
        pvsim = world.start('CSV', sim_start=START, datafile=PV_CONST_DATA)

    if parameter == "adjust_market_requirements":
        energy_market = world.start('CSV', sim_start=START, datafile=ENERGY_REQUIREMENTS_FILE)
    else:
        energy_market = world.start('CSV', sim_start=START, datafile=ENERGY_REQUIREMENTS_CONST_FILE)

    if parameter == "adjust_hh_demand":
        hhsim = world.start('HouseholdSim')
    else:
        hhsim = world.start('HouseholdConstSim')

    pypower = world.start('PyPower', step_size=15 * 60)

    const = world.start('CONST')


    vpp_server = world.start('VPPServer')
    pvcontroller = world.start('PVController')
    cmd = world.start('CMD')
    # Instantiate models
    grid = pvcontroller.Grid(gridfile=GRID_FILE).children
    houses = hhsim.ResidentialLoads(sim_start=START, profile_file=PROFILE_FILE, grid_name=GRID_NAME).children
    pvs = pvsim.PV.create(20)
    market = energy_market.Market.create(20)
    vpps = vpp_server.VPPServer(p_peak=PV_PEAK)
    pvcs = pvcontroller.PVController.create(NUMBER_OF_PV_PLANTS)
    console = cmd.Console()
    consts = const.Const.create(10, value=1)  # list of ten constants with value 1

    # connect entities
    connect_randomly(world, pvs, [e for e in grid if 'node' in e.eid], 'P')

    connect_many_to_one(world, pvs, market, vpps, 'P')
    world.connect(world, vpps, pvcs, 'V')

    # Database
    db = world.start('DB', step_size=60, duration=END)
    hdf5 = db.Database(filename='demo.hdf5')
    connect_many_to_one(world, houses, hdf5, 'P_out')
    connect_many_to_one(world, pvs, hdf5, 'P')

    nodes = [e for e in grid if e.type in ('RefBus, PQBus')]
    connect_many_to_one(world, nodes, hdf5, 'P', 'Q', 'Vl', 'Vm', 'Va')
    connect_many_to_one(world, consts, console, 'val')
    branches = [e for e in grid if e.type in ('Transformer', 'Branch')]
    connect_many_to_one(world, branches, hdf5,
                        'P_from', 'Q_from', 'P_to', 'P_from')


def connect_buildings_to_grid(world, houses, grid):
    buses = filter(lambda e: e.type == 'PQBus', grid)
    buses = {b.eid.split('-')[1]: b for b in buses}
    house_data = world.get_data(houses, 'node_id')
    for house in houses:
        node_id = house_data[house]['node_id']
        world.connect(house, buses[node_id], ('P_out', 'P'))


if __name__ == '__main__':
    main()