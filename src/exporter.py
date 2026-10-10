import json

class Exporter:
    def __init__(self,data,path):
        self.data = data
        self.path = path

    def JsonExporter(self):
        