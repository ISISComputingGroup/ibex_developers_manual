{#ds_hardware_architecture}

# Data streaming: hardware architecture

```{mermaid}
architecture-beta
    group control_board[CONTROL BOARD]
    service timing_fanout(server)[Timing fanout board] in control_board
    service vxi_control_board(server)[VXI Control board] in control_board
    
    group wlsf_module[WLSF MODULE]
    service detector_fpga(server)[WLSF Detector FPGA] in wlsf_module
    
    group linux(server)[LINUX STREAMING SERVER]
    service kafka_runInfo(database)[kafka runInfo] in linux
    service kafka_udp(database)[kafka UDP] in linux
    service udp(server)[udp to kafka Rust] in linux
    service event_processor(server)[event processor Rust] in linux
    service kafka_events(database)[kafka Events] in linux
    
    group external_signals[EXTERNAL SIGNALS]
    service isis_timing(server)[ISIS Timing TOF GPS PPP Vetos] in external_signals
    
    group ibex[IBEX IOCs] in linux
    service kdae_control(server)[KDAE Control] in ibex
    service kdae_diag(server)[KDAE Diagnostics] in ibex
    
    udp:T --> B:kafka_udp
    kafka_udp:R --> L:event_processor
    event_processor:B --> T:kafka_events
    
    detector_fpga:R --> L:udp
    timing_fanout:T  --> B:detector_fpga
    vxi_control_board:T --> B:timing_fanout
    
    vxi_control_board:B <-- T:isis_timing
    
    kdae_control:L --> R:vxi_control_board
    kafka_events:B  --> T:kdae_diag
    kdae_control:B --> T:kafka_runInfo    
```

## Hardware components

### VXI Control Board

Each instrument will have exactly one VXI streaming control board. It controls "global" instrument state, gets timing signals and PPP fed into it. It it what `KDAE_control` primarily talks to begin and end event streaming.

### Timing Fanout board

This sends data from the VXI board to the (potentially multiple) WLSF modules. IBEX will not need to communicate to this. 

### WLSF Fibre module (FPGA)

An instrument may have several of these, depending on the instrument detector configuration. These have a similar UDP-based interface to the VXI boards but also have settings for each detector module. 

IBEX will not need to talk to these except for "advanced" diagnostics. 

### Linux streaming server
This hosts a Kafka cluster, for this bit of infrastructure there are three topics: 
- `runInfo` - this contains `pl72` and `6s4t` run starts/stops send by `kdae_control` 
- `raw_udp` - this contains kafka messages corresponding to each UDP packet which was received (with metadata such as IP address) sent by the [rust udp to Kafka process](https://gitlab.stfc.ac.uk/isis-detector-systems-group/software/data-streaming/rust-udp-to-kafka) which is also hosted on this server
- `events` -  this contains `ev44` formed by the [event stream processor](https://gitlab.stfc.ac.uk/isis-detector-systems-group/software/data-streaming/rust-data-stream-processor/-/tree/main?ref_type=heads) which is also hosted on this server


This also hosts the `kdae_control` and `kdae_diagnostics` IOCs.
