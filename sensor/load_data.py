import os
import glob
import csv
from wsgiref.simple_server import demo_app

def load_sensor_data():
    '''
    Reads in sensor data from csv files using the DictReader class
    of the csv library and stores in array
    '''
    sensor_data = []
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))

    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            data_reader = csv.DictReader(data_file, delimiter = ',')
            for row in data_reader:
                sensor_data.append(row)

    return sensor_data