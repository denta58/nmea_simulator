import pynmea2
import serial
import time

ser = serial.Serial('COM4', 9600, timeout=1)  # open serial port

  
file = open('examples\connected.txt', encoding='utf-8')
lines=file.readlines()

difstartlow = 0

line_num=len(lines)


first = difstartlow


def onepacket_message(start_line):
    check_line=""
    while check_line != "$GNVTG":
        check_line=lines[start_line]
        
        check_line=check_line[:6]
        start_line+=1

        if start_line > line_num:
            start_line = 0

    

    return start_line
            
def serial_write(in_first,in_last):
    
    onePostion=lines[in_first:in_last]

    for onePositionLine in onePostion:
       
        serSend=onePositionLine
        print(serSend)
        ser.write(serSend.encode()) 
    
    print()
    return in_last

def decode_nmea():
    for line in file.readlines():
        try:
            msg = pynmea2.parse(line)
            print(repr(msg))
        except pynmea2.ParseError as e:
            print('Parse error: {}'.format(e))
            continue



while True:
    
    first=serial_write(first,onepacket_message(first))
    
    time.sleep(1)




print(lines[0:6])
"""""
for line in file.readlines():
    print(line)
"""