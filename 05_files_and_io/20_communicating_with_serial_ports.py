import serial


# Read and write data over a serial port, typically to interact with some kind
# of hardware device, using the pySerial package.
ser = serial.Serial('COM0', baudrate=9600, bytesize=8, parity='N', stopbits=1)

# Once open, read and write data using read(), readline(), and write() calls.
ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()
