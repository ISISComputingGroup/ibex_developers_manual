> [Wiki](Home) > [The Backend System](The-Backend-System) > [IOCs](IOCs) > IOC Naming

An example IOC name is `HAMEG8123`, to which a suffix like `_01`, `_02` is automatically appended. New IOC names should be max 8 characters long (excluding the `_01` suffix) and be in uppercase letters. The same name (with the same casing) should be used also for the top-level IOC directory under `EPICS\ioc\master`.

You don't have to use 8 characters, use the smallest number that form a sensible representation of the name. Often this can be obtained by removing vowels, generally just truncating the name as is doesn't usually doesn't look good. You may also be able to shorten a model name or use the model series if that is applicable e.g. eurotherm2000 -> eurotherm2k

Other examples:

Keithley -> KTHLY
 
Support modules may have a slightly longer name if need be, but if truncated please follow guidelines above


