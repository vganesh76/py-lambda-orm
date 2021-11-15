import datetime
import decimal

class ServiceUtils():
    @staticmethod
    def json_date_coverter(o):
        if(isinstance(o, datetime.datetime)):
            #return o.__str__()
            return o.replace(microsecond=0).isoformat()
        elif isinstance(o, decimal.Decimal):
            return o.__str__()
