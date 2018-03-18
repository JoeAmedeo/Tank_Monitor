import sys
import RPi.GPIO as GPIO
from time import sleep
import datetime
import Adafruit_DHT
import MySQLdb

# establish databse connection and cursor for querying
db = MySQLdb.connect(host="localhost", user="root", passwd="something", db="SensorData")

#utilize adafruit library to retrieve data from humidity/temp sensors
def getSensorData(GPIO_number):
    Humidity, Tempurature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, GPIO_number)
    print(str(Humidity), str(Tempurature))
    return (Humidity, Tempurature)
def createTableEntry(GPIO_number, time, humidity, tempurature):
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO Data VALUES ('" + str(GPIO_number) + "', '" + str(time) + "', '" + str(humidity) + "', '" + str(tempurature) + "')")
        db.commit()
    except:
        db.rollback()
    return 0
    
# main function will run indefinately until an exception occurs. It will gather information from your sensors, push data to the database, and put the thread to sleep for 5 minutes.
def main():
    while True:
        try:
            Humidity17, Tempurature17 = getSensorData(17)
            Humidity18, Tempurature18 = getSensorData(18)
            
            currentDateTime = datetime.datetime.now()
            createTableEntry(17, currentDateTime, Humidity17, Tempurature17)
            createTableEntry(18, currentDateTime, Humidity18, Tempurature18)
            sleep(900)
        except Exception as inst:
            print type(inst)
            print (inst.args)
            print inst
            x, y = inst.args
            print "x = ", x
            print "y = ", y
            db.close()
            break
            
if __name__ == '__main__':
    main()
