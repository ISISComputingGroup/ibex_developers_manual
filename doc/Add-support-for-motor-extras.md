> [Wiki](Home) > [The Backend System](The-Backend-System) > [Creating and Basics of IOCs](IOCs) > [Add support for motor extras](Add-support-for-motor-extras)

Look at Beckhoff and copy the file `motor_extras_from_config.cmd`. Also add needed libraries in make file and release. These include:

    - transform
    - calc
    - axis
    - sample_changer
    - tiny_xml
 