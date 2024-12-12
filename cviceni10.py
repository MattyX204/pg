import json 
import datetime


def date_time_serializer(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat
    raise TypeError("Not serialized")



data = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "Main Street",
        "city": "New York"
    },
    "phone":[
        "1234566",
        "987987979",
    ],
    "isMArried": True,
    "isEmployed": False,
    "born": datetime.datetime(1990, 1, 1).isformat()


}

print(json.dumps(data))