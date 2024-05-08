from enum import Enum

CarType = Enum('CarType', ['SEDAN', 'HATCHBACK', 'SUV', 'PICAPE', 'MINIVAN', 'ESPORTIVO'])

def get_member_name(value):
    for member in CarType:
        if member.value == value:
            return member.name
    return None 
