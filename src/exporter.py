import json
import xml.etree.ElementTree as ET
from pathlib import Path

class JsonExporter:    
    def __init__(self):
        pass

    def export(self,data,name):
        # creates folder if not exist then write json
        Path('output/json').mkdir(parents=True, exist_ok=True)
        name = f'output/json/{name}.json'
        with open(name,'w') as f:
            json.dump(data,f,default=str,indent=2)


class XmlExporter:
    def __init__(self):
        pass
    
    def export(self,data,name,root_name='records',item_name='record'):
        Path('output/xml').mkdir(parents=True, exist_ok=True)

        name = f'output/xml/{name}.xml' 
        root = ET.Element(root_name)
        for d in data: # every row become one record tag
            item = ET.SubElement(root,item_name)
            for key,val in d.items():
                ET.SubElement(item,key).text=str(val)

        tree = ET.ElementTree(root) # makes tree from root
        # pretty look
        ET.indent(tree,space="    ")
        tree.write(name,encoding='utf-8', xml_declaration=True)
