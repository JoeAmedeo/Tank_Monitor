import sys
import RPi.GPIO as GPIO
from time import sleep
import datetime
import Adafruit_DHT
import requests

#url for your api
url = "insert url for api here"

#the numbers you want to attribute each sensor in the database
#can be changed if, for example, you hook up two pi's to a database and want to differentiate all 4 sensors
sensor1 = 1
sensor2 = 2

#utilize adafruit library to retrieve data from humidity/temp sensors
def getSensorData(GPIO_number):
    Humidity, Tempurature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, GPIO_number)
    print(str(Humidity), str(Tempurature))
    return (Humidity, Tempurature)

#put data gathered from this pi into the database
def createTableEntry(sensorNumber, time, humidity, tempurature):
    requests.put(url, json={'sensorNumber': sensorNumber, 'time': time, 'humidity': humidity, 'tempurature': tempurature})

#check to see if our database is getting too large (struggles of free mongodb hosting)
#remove oldest entries if the we are getting close to our data limit
def checkTableSize():
    collectionCount = requests.get(url)
    if collectionCount > 60000:
        requests.delete(url, json={'sensorNumber': sensor1})
        requests.delete(url, json={'sensorNumber': sensor2})

# main function will run indefinately until an exception occurs. It will gather information from your sensors, push data to the database, and put the thread to sleep for 5 minutes.
def main():
    while True:
        try:
            #NOTE: do not use sensor variables for input, alter inputs to these two calls according to the gpio number used in your pi
            Humidity1, Tempurature1 = getSensorData(17)
            Humidity2, Tempurature2 = getSensorData(18)

            currentDateTime = datetime.datetime.now()

            createTableEntry(sensor1, currentDateTime, Humidity1, Tempurature1)
            createTableEntry(sensor2, currentDateTime, Humidity2, Tempurature2)

            checkTableSize()

            sleep(900)
        except Exception as inst:
            print type(inst)
            print (inst.args)
            print inst
            x, y = inst.args
            print "x = ", x
            print "y = ", y
            break
            
if __name__ == '__main__':
    main()
