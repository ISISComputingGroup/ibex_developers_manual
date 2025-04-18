# Reducing `ISISICP` memory use in simulation mode

If you want a minimal ICP with no real DAE support then:

In c:/labview modules/dae/isisicp.properties    add the line
```    
isisicp.simulation.detcards.shared = false
```
In c:/labview modules/dae/icp_config.xml    change the CRPTSize  line to a smaller value e.g.
```
<I32>     <Name>CRPTSize</Name>                <Val>10000</Val>           </I32>  <!-- In words -->
```

Load some very simple wiring tables defining a handful of detector and specify only a few time channels (e.g. SURF monitor only tables, muon tables, ibex RPCTT tables). Number_of_spectra * number_of_time_channels * number_of_period must be less than CRPTSize above