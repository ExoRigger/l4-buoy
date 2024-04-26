#!/usr/bin/env python3

from logger import Logger
import serial

# -----------------------------------------------------------------------------
# Class Definition of Visiometer Payload Instrument
# -----------------------------------------------------------------------------

# Inputs:
#  > Hardware port for logging (COMXX)
#  > Communication settings
#  > Path to log data files to

class Visiometer:

    visiometer_logger = Logger("MET-Visiometer","./MET-Visiometer","visiometer")

    def __init__(self):

        self.hardware_port = ""
        self.baudrate = ""
        # Additional settings if required

        self.visiometer_logger.log.info(f"[+] Visiometer Passive Logging Initialized")
        pass

    def run(self):
        self.visiometer_logger.log.info(f"[+] Visiometer Passive Logging Active")
        pass



def testVisiometer():
    test_visiometer = Visiometer()
    test_visiometer.run()


if __name__ == '__main__':
    testVisiometer()
