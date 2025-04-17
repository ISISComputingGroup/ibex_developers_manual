> [Wiki](Home) > [Project overview](Project-Overview) > [Design documents](Design-Documents) > [Reflectometers](Reflectometers) > [Reflectometry Testing](Reflectometry-Testing) > [Experiment script](reflectometry_blind_script)

```Python
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(r"C:\\", "Instrument", "scripts")))

from genie_python import genie as g
from technique.reflectometry import SampleGenerator, run_angle, contrast_change, transmission


def runscript(dry_run=False):
    """
    Run my script
    :param dry_run: True just print what would happen; False do it
    """

    if not dry_run:
        g.change_number_soft_periods(1)

    # Set up defaults for all samples
    sample_generator = SampleGenerator(
        translation=-18.500,
        height2_offset=0,
        phi_offset=0.005-0.3,
        psi_offset=-0.940,
        height_offset=-37.067,
        resolution=0.03,
        footprint=60)

    # Set up all the samples
    sample = sample_generator.new_sample(
            title="Si_D2O")
    #run_angle(sample, angle=0.3, count_uamps=10, s1vg=0.609, s2vg=0.206, s3vg=0.6, s4vg=0.9, mode="NR", dry_run=dry_run)    
    #transmission(sample, "Si_Trans", count_uamps=30, s1vg=0.25, s2vg=0.25, height_offset=5, mode="NR", dry_run=dry_run)
                
    while True:
        sample.title="Si_D2O"
        run_angle(sample, angle=0.3, count_uamps=50, s1vg=0.609, s2vg=0.206, s3vg=0.6, s4vg=0.9, mode="NR", dry_run=dry_run)
        run_angle(sample, angle=0.6, count_uamps=120, s1vg=0.609*2, s2vg=0.206*2, s3vg=0.6*2, s4vg=0.9*2, mode="NR", dry_run=dry_run)
        run_angle(sample, angle=1.5, count_uamps=200, s1vg=0.609*5, s2vg=0.206*5, s3vg=0.6*5, s4vg=0.9*5, mode="NR", dry_run=dry_run)
        
        contrast_change(1, [38, 0, 62, 0], flow=1.5, volume=30, dry_run=dry_run)
        
        transmission(sample, "Si_Trans", count_uamps=180, s1vg=0.25, s2vg=0.25, height_offset=5, mode="NR", dry_run=dry_run)
        sample.title="Si_SMW"
        run_angle(sample, angle=0.3, count_uamps=100, s1vg=0.609, s2vg=0.206, s3vg=0.6, s4vg=0.9, mode="NR", dry_run=dry_run)
        run_angle(sample, angle=0.6, count_uamps=180, s1vg=0.609*2, s2vg=0.206*2, s3vg=0.6*2, s4vg=0.9*2, mode="NR", dry_run=dry_run)
        run_angle(sample, angle=1.5, count_uamps=300, s1vg=0.609*5, s2vg=0.206*5, s3vg=0.6*5, s4vg=0.9*5, mode="NR", dry_run=dry_run)
        
        contrast_change(1, [0, 0, 100, 0], flow=1.5, volume=30, wait=True, dry_run=dry_run)
        sample.title="Si_H20"
        run_angle(sample, angle=0.3, count_uamps=80, s1vg=0.609, s2vg=0.206, s3vg=0.6, s4vg=0.9, mode="NR", dry_run=dry_run)
        run_angle(sample, angle=0.6, count_uamps=150, s1vg=0.609*2, s2vg=0.206*2, s3vg=0.6*2, s4vg=0.9*2, mode="NR", dry_run=dry_run)
        run_angle(sample, angle=1.5, count_uamps=250, s1vg=0.609*5, s2vg=0.206*5, s3vg=0.6*5, s4vg=0.9*5, mode="NR", dry_run=dry_run)

        contrast_change(1, [100, 0, 0, 0], flow=1.5, volume=30, dry_run=dry_run)
        transmission(sample, "Si_Trans", count_uamps=180, s1vg=0.25, s2vg=0.25, height_offset=5, mode="NR", dry_run=dry_run)
        
        if (dry_run):
            print("Repeat infinitum")
            break
```
