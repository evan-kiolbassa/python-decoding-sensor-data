from datetime import date, datetime

class HouseInfo:

    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area = 0):
        '''
        Accepts a field that a user wants to look-up and an
        area arg. The method iterates through the list of
        dictionaries and appends the value of the corresponding 
        dictionary key where the area boolean is True to an array.
        The method then return the array
        '''
        field_data = []

        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data

    def get_data_by_date(self, field, rec_date = date.today()):
        '''
        Traverses the data dictionary and returns values of a key specified in the function arg,
        corresponding to the date specified in the args
        '''
        field_data = []
        for record in self.data:
            if rec_date.strftime("%m/%d/%y") == record['date']:
                field_data.append(record[field])
        return field_data

    