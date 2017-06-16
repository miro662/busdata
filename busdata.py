""" Simple functions for managing busdata
"""
import json
from re import split

class BusData:
    """ Class presenting single file with bus departures data
    """

    def save(self, filename):
        """ Saves data to given file
        """
        savefile = open(filename, 'w')
        json.dump(self.data, savefile)

    def add_bus(self, bus, day):
        """ Adds one bus departure to file
        """
        if not day in self.data:
            self.data[day] = []

        self.data[day].append(bus)

    def add_buses(self, buses, day):
        """ Adds multiple buses departures to file
        """
        if not day in self.data:
            self.data[day] = []

        self.data[day].extend(buses)


    def __init__(self, filename=None):
        if filename is None:
            self.file = None
            self.data = {}
        else:
            self.file = open(filename)
            self.data = json.load(self.file)


def parse_mks_data(bustype: str, data: str):
    departures_strings = split(r"\s+", data)
    print(departures_strings)
    return [{
        "Hour": int(d.split(":")[0]),
        "Minute": int(d.split(":")[1]),
        "BusType": bustype
    } for d in departures_strings]


if __name__ == "__main__":
    print(parse_mks_data("MKS", "05:12   05:58   06:45   07:20   07:57   08:35   09:20   10:40   11:50   13:22   14:10   15:05   15:30   16:20   16:57   17:30   18:33   19:28   20:28   21:12   22:17"))