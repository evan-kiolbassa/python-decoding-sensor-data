class HouseInfo:

    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area):
        '''
        Accepts a field that a user wants to look-up and an
        area arg. The method iterates through the list of
        dictionaries and appends the value of the corresponding 
        dictionary key where the area boolean is True to an array.
        The method then return the array
        '''
        
        if rec_area is None:
            rec_area = 0
        field_data = []

        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record['area']):
                field_data.append(record[field])
        return field_data

    