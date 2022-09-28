import serial
import RPi.GPIO as GPIO
import string
import time
import datetime
import random
from time import gmtime, strftime
import sqlite3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

ser=serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600


#actor (blinking LED)

def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return


#SQlite table creation and data entry

connection = sqlite3.connect("thermistor.db")
cursor = connection.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS data (unix REAL, date REAL, timestamp REAL, degreeC REAL)")

def data_entry():
    cursor.execute("INSERT INTO data VALUES(12341234, '2022-09-28', '00:01', '14.14')")
    connection.commit()
    
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d"))
    timestamp = str(datetime.datetime.fromtimestamp(unix).strftime("%H:%M:%S"))
    degreeC = float(read_ser.decode("utf-8"))
    cursor.execute("INSERT INTO data (unix, date, timestamp, degreeC) VALUES(?, ?, ?, ?)",
                   (unix, date, timestamp, degreeC))
    connection.commit()

create_table()
data_entry()




while True:
    read_ser=ser.readline()
    print (strftime("%Y-%m-%d"), strftime("%H-%M-%S"), float(read_ser.decode("utf-8") + '\n')) 
    time.sleep(2)
    if (float(read_ser.decode("utf-8")) >= 17):
        blink(11)
    dynamic_data_entry()
    

