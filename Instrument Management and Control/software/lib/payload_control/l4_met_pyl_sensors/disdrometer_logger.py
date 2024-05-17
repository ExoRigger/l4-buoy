#!/usr/bin/env python3

from logger import Logger
import serial

# -----------------------------------------------------------------------------
# Class Definition of Disdrometer Payload Instrument
# -----------------------------------------------------------------------------

# Inputs:
#  > Hardware port for logging (COMXX)
#  > Communication settings
#  > Path to log data files to

class Disdrometer:

    visiometer_logger = Logger("MET-Disdrometer","./MET-Disdrometer","visiometer")

  # RS232, 36400, 8,N,1
    def __init__(self):

        self.hardware_port = "" # Check once integrated onto L4 Buoy PC
        self.baudrate = 36400
        # Additional settings if required

        self.visiometer_logger.log.info(f"[+] Disdrometer Passive Logging Initialized")
        pass

    def run(self):
        self.visiometer_logger.log.info(f"[+] Disdrometer Passive Logging Active")
        # Open serial port and while there is data, log to logfile
        pass



def testDisdrometer():
    test_visiometer = Disdrometer()
    test_visiometer.run()


if __name__ == '__main__':
    testDisdrometer()
