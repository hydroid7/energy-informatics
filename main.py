import mosaik

sim_config = {
    'WebVis': {
        'cmd': 'mosaik-web -s 0.0.0.0:8000 %(addr)s',
    },
    'CSV': {
        'python': 'mosaik_csv:CSV',
    },
    'VPPServer': {
        'python': 'simulators.VPPServer:VPPServer',
    },
    'PVController': {
        'python': 'simulators.PVController:PVController'
    },
    'HouseholdSim': {
        'python': 'householdsim.mosaik:HouseholdSim',
        # 'cmd': 'mosaik-householdsim %(addr)s',
    },
    'PyPower': {
        'python': 'mosaik_pypower.mosaik:PyPower',
        # 'cmd': 'mosaik-pypower %(addr)s',
    },
}

START = '2014-01-01 00:00:00'
END = 10  # 1 day
PV_DATA = 'data/pv_10kw.csv'
PROFILE_FILE = 'data/profiles.data.gz'
GRID_NAME = 'demo_lv_grid'
GRID_FILE = 'data/%s.json' % GRID_NAME
ENERGY_REQUIREMENTS_FILE = 'data/energy-requirements.csv'
PV_PEAK = 7000
NUMBER_PV_PLANTS = 10
def main():
    world = mosaik.World(sim_config)
    create_scenario(world)


def create_scenario(world):
    # Start simulators
    pypower = world.start('PyPower', step_size=15 * 60)
    hhsim = world.start('HouseholdSim')
    pvsim = world.start('CSV', sim_start=START, datafile=PV_DATA)

    energy_market = world.start('CSV', sim_start=START, datafile=ENERGY_REQUIREMENTS_FILE)
    vpp_server = world.start('VPPServer')
    pv_controller = world.start('VPController')

    # Instantiate models
    grid = pypower.Grid(gridfile=GRID_FILE).children
    houses = hhsim.ResidentialLoads(sim_start=START,
                                    profile_file=PROFILE_FILE,
                                    grid_name=GRID_NAME).children
    pvs = pvsim.PV.create(20)
    server = vpp_server.VPPServer(p_peak=PV_PEAK)
    pvcs = pv_controller.PVController.create(NUMBER_PV_PLANTS)

if __name__ == '__main__':
    main()
