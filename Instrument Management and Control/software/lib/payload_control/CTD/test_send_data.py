import serial


def send_pressure():
    com_dest = "COM17"
    file_loc = "latest_ctd.csv"

    with open(file_loc,'r') as f:
        l = f.readlines()
        pressure = l[1].split()[-5]

    try:

        with serial.Serial(port=com_dest,baudrate=4800,timeout=1) as winch:
            winch.write(pressure.encode()) 
        print("OK")

    except Exception as err:
        print("errorrrrrrrrr")


def main():
    send_pressure()

if __name__ == '__main__':

    main()