#!/usr/bin/env python3

from disdrometer_logger import Disdrometer
from visiometer_logger import Visiometer

def main():

    met_disdrometer = Disdrometer()
    met_visiometer = Visiometer()

    met_disdrometer.run()
    met_visiometer.run()

if __name__ == '__main__':

    main()
