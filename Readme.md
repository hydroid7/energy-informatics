# Energy Informatics Simulation Project
### Phase IV

#### Distribution of the Tasks
- Task a: Lóránt Meszlényi
- Task b, c: Nahla Ben Mosbah, Karim Toumi, Basma Dakech, Priyanka Nagulapally, Lóránt Meszlényi
- Task d: Lóránt Meszlényi

#### General
The file `interfaces.py` contains all required interfaces for the implementations.
The following interfaces are designed:
- ~~AbstractLocalMeasurementDevice~~ -> Integrated into `AbstractPVController`
- ~~AbstractEnergyMarketSystem~~ -> Simple CSV Reader of Mosaik
- `AbstractVPPServer`
- `AbstractPVController`
  The Component has to set its real power output to `min(VPPValue, LocalPowerRegulatorValue)`

#### Organization
All interfaces and data objects belongs to the interfaces folder.
Simulation entities are placed in the `simulators` folders and their tests come to the `test` folder.


#### Implementing Interfaces
To implement an interface and the test belonging to the interface, check out the files `simulators/PVController.py` and
`test/PVController.py`.

If you have to change the methods signature (because you need more data, etc.) feel free to do this. In this case please
don't forget to update the interfaces signature. Otherwise your tests will *fail*.

If you need complex data types as return values or as method parameters, e. g. Power reading with time constraints, 
create a new DataObject for this. All data objects you can find in the folder `interfaces/informationObjects.py`.
