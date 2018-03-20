import RPi.GPIO as GPIO
import ftplib

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)


server = '31.170.167.171'
username = 'u935469477'
password = 'murtaza1'
ftp_connection = ftplib.FTP(server, username, password)

unit=0

while(True):
    s=GPIO.input(11)


    while(s==1):
        unit=unit+0.1
        print("%s gg",unit)
        ff=open("/home/pi/meter.txt",'w')
        ff.write("%s kWh"%(unit))
        ff.close()

        fh = open("/home/pi/meter.txt", 'rb')
        ftp_connection.storbinary('STOR meter.txt', fh)
        fh.close()

        s=GPIO.input(11)
