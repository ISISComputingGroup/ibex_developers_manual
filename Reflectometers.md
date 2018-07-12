> [Wiki](Home) > [Project overview](Project-Overview) > Design documents

The aim of the reflectometer project is to allow users of the reflectometers to have a common and easy experience to set the position of items on the beam line. The setup is fairly complex because of there are multiple items that need to be coordinated to make a measurement. This page should give an overview of what is going on and the user cases that are needed.

## Experiment to perform

The reflectometry experiment is described in part in the [mantid documentation](http://docs.mantidproject.org/v3.12.0/techniques/ISIS_Reflectometry.html) and in [more detail for POLREF](https://github.com/ISISComputingGroup/IBEX/wiki/Reflectometry-at-Isis). The important things to know from this and other are:

1. The data needed to be retrieved is neutron count vs Q.
1. The [momentum transfer](https://en.wikipedia.org/wiki/Momentum_transfer) is characterised from Q = 4π / λ sin θ 
1. The wavelength is proportional to the time of flight. So to get a large range of q the scientists stitch together spectra from multiple angles.
1. There are other experiments that can be performed where off-specular alignments are used. Also where the rock the sample.
1. When thinking about alignments, there is a path through the experiment set by the super mirror, sample point, analyser angle and detector position. Everything else can be aligned to this path but does not control that path. 

## Setup

Generally, the idea is to position the detector at **theta** around the **sample point** (= the coordinates of the beam at a fixed distance x from the detector). We make a distinction between two types of reflectometry instruments based on beamline equipment and the way their detector is positioned.

(diagram 1 goes here)

In the first case (for INTER, CRISP, SURF), the detector slides up and down on a height stage and can be angled to be perpendicular to the incident beam. This means the distance between sample and detector actually varies slightly, however the beam path on these instruments is relatively short so the resultant error is tolerable.

(diagram 2 goes here)

In the second case (for POLREF, OFFSPEC), the detector sits on a bench, that can be angled, driven up/down, and slide closer/further from the sample, which allows the detector to actually move along a radius around the sample.

The devices on the beamline fall into two categories which can be described as **tracking** and **affecting** the beam path. All equipment has to track the beam path, whereas only some equipment (such as supermirrors, or the sample itself) affect the beampath by introducing an angular offset. This means that an offset needs to be added to the height and angle of each piece of equipment downstream to remain centered in and perpendicular to the beam. In practice, everything is also affected by engineering errors which need to be accounted for.

## Questions

1. (John) Is the notional sample point x position fixes?
1. (John) I think each mode of operation sets up fixed rules and relations and this is what we need to capture.
1. (John) We need to calculate both the positions based on composite parameters and composite parameters based on the positions of the components, is this right?
    1. (John) What happens if the beam having hit the super mirror does not hit the sample axis?
    1. (John) What happens if the detector is not looking at the sample point?
