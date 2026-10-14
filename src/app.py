from src.config import load_queries,load_config
from src.exporter import JsonExporter,XmlExporter
from src.repository import Repository
from src.data_loader import load_json
from src.database import Database



class App:
    def __init__(self,args,queries:load_queries):
        self.args = args
        self.q1,self.q2,self.q3,self.q4 = queries
        self.db = Database(load_config())

    def run(self):
        
        # chose exporter class by format from cli
        exporters = {'json':JsonExporter,'xml':XmlExporter}
        exporter = exporters[self.args.format]
        rep = Repository(self.db) # repository talks with db
        rep.create_schema() # delete old sschmea fully and recreate
        # load json files and insert to db
        rep.insert_rooms(load_json(self.args.rooms))
        rep.insert_students(load_json(self.args.students))
        rep.create_index() # creates index

        # pair each query with its output name and export result
        for j in zip([self.q1,self.q2,self.q3,self.q4],['q1_output','q2_output','q3_output','q4_output']):
            query,name=j
            result=rep.fetch(query)
            exporter().export(result,name)