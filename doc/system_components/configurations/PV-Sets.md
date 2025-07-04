# PV Sets

PV Sets are a feature that is rarely used, if at all. According to Freddie, it was originally made at the request of an instrument scientist on LARMOR. Later, said scientist said he might not need it anymore and then never came back with the issue. It can only be set for the Galil according to John and Freddie. However, there is a page called [Linmot](/specific_iocs/motors/Linmot) in the dev wiki which says that the Linmot IOC should have PV Sets for Engin-X and MAPS, however I could not find any PV Set in any Linmot ioc in any component.

:::{seealso}
The {external+ibex_user_manual:ref}`manage_configs_pv_sets` documentation on the user manual.
:::

The logic to add pv sets exists in the back end, but there does not seem to be an implementation in the GUI beyond the view. If you manually add pv sets encoded in XML according to the schema in a component of your dev machine, then load that component, then the pv sets table will still be empty. The XML schemas in inst_servers describe how pv sets should look in XML. There is also no button that allows you to add a PV Set.

I have added some tests that check if components or configurations contain any non empty PV sets and ran the config checker for all instruments and that test never failed, therefore there no instrument that uses any pv set. The code with the test is on this branch https://github.com/ISISComputingGroup/ConfigChecker/tree/add_pv_sets_test .

Looking through the IBEX issues for the key words "pv set", there is a ticket for expanding this feature from august of 2016 that has never been included into a sprint: https://github.com/ISISComputingGroup/IBEX/issues/1449. In June of 2016, a bug for this feature was found in https://github.com/ISISComputingGroup/IBEX/issues/1353. This issue describes a bug that made the ioc PV Set for the Galil IOC disappear from a component, which means at some point in time the Galils had pv sets. But the ticket says that meanwhile the layout of the PV Sets table changed, which made the issue of that ticket not relevant any more. In April of 2017, another ticket was made regarding the IOC PV Sets disappearing after saving said component. This ticket was never pulled in any sprint. This means there were PV Sets for Galils at some point but they have disappeared since then.

Freddie says we might not need them anymore and that he thinks he has a better solution than PV Sets.