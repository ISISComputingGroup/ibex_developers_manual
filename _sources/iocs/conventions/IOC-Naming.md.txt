# IOC Naming

An example IOC name is `HMEG8123`, to which a suffix like `_01`, `_02` is automatically appended. New IOC names should be max 8 characters long (excluding the `_01` suffix) and be in uppercase letters. The same name (with the same casing) should be used also for the top-level IOC directory under `EPICS\ioc\master`.

You don't have to use the full 8 characters, use the smallest number that form a sensible truncated representation of the name that captures its overall form. Often this can be obtained by removing vowels (in general remove all the vowels not just some), generally just truncating the name as is doesn't always look good. You may also be able to shorten a model name or use the general model series if that is applicable e.g. `Eurotherm2000` -> `eurotherm2k`, `TPG3xx` etc or just TPG if it is model series independent.

Support modules may have a slightly longer name if need be, but if truncated please follow guidelines above.

If an IOC is *truly* instrument specific (i.e. there is absolutely no chance that this equipment will ever be used on any other instrument), the first three letters of the IOC name can indicate the instrument. E.g. EGX for Engin-X or RKN for Riken.

