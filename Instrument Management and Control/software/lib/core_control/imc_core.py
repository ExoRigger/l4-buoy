#!/usr/bin/env python3

# =====================================================================
# This class creates logging objects for power control and data
# acquisition and contains asynchonous threadded control loops for 
# power and payload control
# =====================================================================

import threading
from time import sleep
import sys
import datetime
from lib.core_control.logger import Logger
from lib.power_control.power_interface import IMCPowerInterface
from lib.payload_control.payload_interface import IMCPayloadInterface

class Core:

    def __init__(self,log_dir,data_dir):
        # Define attached payloads
        self.payloads = {
                          1:"PAYLOAD_PC",
                          2:"CHANNEL 2",
                          3:"CHANNEL 3",
                          4:"CHANNEL 4",
                          5:"CHANNEL 5",
                          6:"CHANNEL 6",
                          7:"CHANNEL 7",
                          8:"CHANNEL 8",
                          9:"CHANNEL 9",
                          10:"CHANNEL 10",
                          11:"CHANNEL 11",
                          12:"CHANNEL 12",
                          13:"CHANNEL 13",
                          14:"CHANNEL 14",
                          15:"CHANNEL 15",
                          16:"CHANNEL 16",
                        }   
        # Setup logging and collection of data
        self.sys_log_dir = log_dir
        self.pyl_data_dir = data_dir
        self.initLogging()

                                      
    def initLogging(self):
        self.sys_log = Logger("core_logger",self.sys_log_dir + "\\core","core_log")
        self.sys_log.log.info(f"[+] (Core Control) INITIALIZED")
        
    def runCore(self):
        try:
            self.sys_log.log.info(f"[o] (Core Control) ACTIVE")
            imc_thread = threading.Thread(target=self.runImcControl)           
            pyl_thread  = threading.Thread(target=self.runPayloadControl)
            
            imc_thread.start()
            pyl_thread.start()
            
            imc_thread.join()
            pyl_thread.join()
            
            self.sys_log.log.info(f"[o] (Core Control) END")
            return 0
            
        except Exception as error:
            self.sys_log.log.error(error)
            return 1
 
# =====================================================================
# Spin up two separate threads to govern power control and data logging
# =====================================================================
# TODO: Give IMCPowerInterface the list of sensor;channel allocations
    def runImcControl(self):
        self.core_ctl = IMCPowerInterface("COM26",115200,self.sys_log_dir,self.pyl_data_dir,self.payloads)        
        self.core_ctl.sampleImc()

    def runPayloadControl(self):
        self.pyl_ctl = IMCPayloadInterface(self.sys_log_dir,self.pyl_data_dir)
        self.pyl_ctl.samplePyl()
        
# =====================================================================
