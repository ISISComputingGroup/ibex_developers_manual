# Serial Bruteforce Script

The following is a Python script that can be run against devices with unknown comms settings. It will attempt to get a reply out of a device using all available comms settings.

Note that the script may only get a single character from the device, even if the device responds with many characters. It is likely that several serial settings will reply - further analysis of the device will be required to determine the proper set (e.g. many devices will still give replies even with an incorrect parity or stop bits setting).

You will need to run `python -m pip install pyserial` before running this script.

```python
import serial


COMMAND = b"1OS\r"
PORT = "COM1"

def try_send(baud, stop, bits, parity, xonxoff):
    try:
        with serial.Serial(PORT, stopbits=stop, bytesize=bits, baudrate=baud, parity=parity, xonxoff=xonxoff, timeout=0.5) as p:
            print(f"trying {baud} {stop} {bits} {parity} {xonxoff}")
            p.write(COMMAND)
            print(p.read())
    except serial.SerialException as e:
        pass
    except Exception as e:
        print(e)


def force():
    for baud in [9600, 19200, 38400, 57600, 115200, 4800, 2400]:
        for stop in [serial.STOPBITS_ONE, serial.STOPBITS_ONE_POINT_FIVE, serial.STOPBITS_TWO]:
            for bits in [serial.FIVEBITS, serial.SIXBITS, serial.SEVENBITS, serial.EIGHTBITS]:
                for parity in [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD, serial.PARITY_MARK, serial.PARITY_SPACE]:
                    for xonxoff in [True, False]:
                        try_send(baud, stop, bits, parity, xonxoff)
```