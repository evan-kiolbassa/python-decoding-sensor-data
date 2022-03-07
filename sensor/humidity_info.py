from house_info import HouseInfo

class HumidityData(HouseInfo):
    def _convert_data(self,data):
        recs = []
        for rec in data:
            rec = float(rec) * 100
            recs.append(rec)
        return recs

    