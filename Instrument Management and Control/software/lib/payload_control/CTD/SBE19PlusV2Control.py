import serial
from time import sleep
import sys,os
from logger import Logger

# Class Definition
# - Integration Steps:
# -  > Demo CTD Sampling for 10mins as before
# -  > Demo Tx of Winch Pressure as before
# -  > Demo Hex Data Download introduced
# -------------------------------------------------------
# NOTE: To Save bloat in the code, utilize switching modes between hex and eng units
class SBE19PlusV2:
    ctd_data_logger = Logger("SBE19PlusV2",".\CTD","ctd_data")
    ctd_control_logger = Logger("SBE19PlusV2","\.CTD","ctd_control")
  # Initialize control object parameters
    def __init__(self,CTD_COM_PORT,CTD_DATA_DIR):
        self.CTD_COM_PORT = CTD_COM_PORT
        self.CTD_DATA_DIR = CTD_DATA_DIR
        self.WINCH_COM_PORT = "COM17"

        self.ctd_control_logger.log.info("[+] (CTD Control) CTD CONTROL INITIALIZED")

  # Connect to CTD, wake and configure sampling parameters
    def initializeCTD(self):
      # Clear memory, send twice to confirm
        self.ctd_control_logger.log.info("[+] (CTD Control) CONFIGURE CTD START")
        self.sendCmd(b'OutputFormat=3\r')
        self.sendCmd(b'initlogging\r')
        self.sendCmd(b'initlogging\r')
        self.ctd_control_logger.log.info("[+] (CTD Control) CONFIGURE CTD END")

  # Put CTD into Low Power Mode (QS)
    def deactivateCTD(self):
        self.sendCmd(b'Stop\r')
        self.sendCmd(b'QS\r')
        self.ctd_control_logger.log.info("[+] (CTD Control) CTD IN QUIESCENT STATE")

  # Send control command to CTD over UART, optionally returning an open session to the 
  # instrument for further communication
    def sendCmd(self,cmd,return_handle=False):
        handle = serial.Serial(self.CTD_COM_PORT, 4800, timeout=1)
        handle.flushInput()
        handle.write(cmd.encode() + b'\n')
        time.sleep(0.1)
        if return_handle:
            return handle
        else:
            handle.close()
        self.ctd_control_logger.log.info("[+] (CTD Control) CMD SEND: {cmd}")

  # Send control command to CTD over UART
  # TODO: Compare with getStatus to see if data loss is an issue
    def downloadData(self):
        self.ctd_control_logger.log.info("[+] (CTD Control) DATA DOWNLOAD START")
        cmd = b'DD\r'
        stream_handle = serial.Serial(self.CTD_COM_PORT, 4800, timeout=1)
        stream_handle.flushInput()
        stream_handle.write(cmd.encode() + b'\n')
        while stream_handle.in_waiting():
            scan = stream_handle.readline()
            self.ctd_data_logger.log.info(scan)
        stream_handle.close()

        self.ctd_control_logger.log.info("[+] (CTD Control) DATA DOWNLOAD END")

  # Start CTD sampling and log data for a duration of time
    def takeSample(self,duration=10,frequency=4):
        self.ctd_control_logger.log.info("[+] (CTD Control) SAMPLE START")
        self.initializeCTD()
        dt = 1/frequency
        n_samples = frequency * (duration * 60)
        stream_handle = self.sendCmd(b'Startnow\r',return_handle=True)
        # - Sample Code - 
        for i in range(n_samples):
            scan = stream_handle.readline()
            self.ctd_data_logger.log.info(scan)
            self.sendPressure(scan)
            time.sleep(dt)
        stream_handle.close()
        self.sendCmd(b'Stop\r')
        self.deactivateCTD()
        self.ctd_control_logger.log.info("[+] (CTD Control) SAMPLE END")
        self.ctd_control_logger.log.info()

  # Log CTD System Information
    def getStatus(self):
        stream_handle = self.sendCmd(b'DS\r',return_handle=True)
        while stream_handle.in_waiting():
            status_str = stream_handle.readline()
            self.ctd_control_logger.log.info(status_str)
        self.ctd_control_logger.log.info("[+] (CTD Control) STATUS OK")

  # Read and send pressure value to winch system over UART
  # TODO: Find out where the pressure value is in the scan line
    def sendPressure(self,scan):
        pressure = scan[1:] 
        try:
            with serial.Serial(port=self.WINCH_COM_PORT,baudrate=9600,timeout=1) as winch:
                winch.write(pressure.encode()) 
                time.sleep(0.1)
            self.ctd_control_logger.log.info(f"[+] Sent to Winch system: {pressure}")

        except Exception as error:
            self.ctd_control_logger.log.info("[-] Pressure Tx Fail: {error}")
           
# Test Code
# ------------------------
def testCTD():

    ctd_test = SBE19PlusV2("COM19","./")
    ctd_test.takeSample(duration=10,frequency=4)

if __name__ == '__main__':

    testCTD()
