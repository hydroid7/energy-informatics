# Energy Informatics Simulation Project
### Phase IV

#### Distribution of the Tasks
- Task a: Lóránt Meszlényi
- Task b: Nahla Ben Mosbah, Karim Toumi
- Task c: Basma Dakech, Priyanka Nagulapally
- Task d: Lóránt Meszlényi

#### General
The file `interfaces.py` contains all required interfaces for the implementations.
The following interfaces are designed:
- ~~AbstractLocalMeasurementDevice~~ -> Integrated into `AbstractPVController`
- ~~AbstractEnergyMarketSystem~~ -> Simple CSV Reader of Mosaik
- `AbstractVPPServer`
- `AbstractPVController`
  The Component has to set its real power output to `min(VPPValue, LocalPowerRegulatorValue)`

In order to implement an interface, import the base class from the `interfaces.py` with 
`from interfaces import AbstractVPPServer` and
make a subclass of the interface with
```python
from interfaces.interfaces import AbstractVPPServer

class VPPServer(AbstractVPPServer):
    ...
```
and implement its methods. The documentation is also available for each method in its superclass.