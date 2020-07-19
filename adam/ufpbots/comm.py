import sys
import glob
import serial
from  serial.tools import list_ports
import threading
import pyudev

# from https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python

# def serial_ports():
#     """ Lists serial port names
#
#         :raises EnvironmentError:
#             On unsupported or unknown platforms
#         :returns:
#             A list of the serial ports available on the system
#     """
#     if sys.platform.startswith('win'):
#         ports = ['COM%s' % (i + 1) for i in range(256)]
#     elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
#         # this excludes your current terminal "/dev/tty"
#         ports = glob.glob('/dev/tty[A-Za-z]*')
#     elif sys.platform.startswith('darwin'):
#         ports = glob.glob('/dev/tty.*')
#     else:
#         raise EnvironmentError('Unsupported platform')
#
#     result = []
#     for port in ports:
#         try:
#             s = serial.Serial(port)
#             s.close()
#             result.append(port)
#         except (OSError, serial.SerialException):
#             pass
#     return result

# def ask_for_port():
#     """Returns a list of all serial ports found, e.g. 'COM1' in Windows"""
#     return sorted([port.name for port in list_ports.comports()])
#
# print(ask_for_port())
class USBDetector():
    ''' Monitor udev for detection of usb '''

    def __init__(self):
        ''' Initiate the object '''
        self.thread = threading.Thread(target=self._work)
        self.thread.daemon = True
        self.thread.start()

    def _work(self):
        ''' Runs the actual loop to detect the events '''
        self.context = pyudev.Context()
        self.monitor = pyudev.Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem='usb')
        # this is module level logger, can be ignored
        self.monitor.start()
        for device in iter(self.monitor.poll, None):
            if device.action == 'add':
                # some function to run on insertion of usb
                print('{} connected'.format(device))
a = USBDetector()
a._work()
a.thread.join()
print('asdf')
# a.join()
