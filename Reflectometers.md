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

I will create a diagram for this at some point but I don't understand it well enough yet.

## Questions

1. (John) Is the notional sample point x position fixes?
1. (John) I think each mode of operation sets up fixed rules and relations and this is what we need to capture.
1. (John) We need to calculate both the positions based on composite parameters and composite parameters based on the positions of the components, is this right?
    1. (John) What happens if the beam having hit the super mirror does not hit the sample axis?
    1. (John) What happens if the detector is not looking at the sample point?
