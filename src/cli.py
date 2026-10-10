import argparse 

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s','--students',required=True)     
    parser.add_argument('-r', '--rooms',required=True)      
    parser.add_argument('-f', '--format',choices=['json','xml'],default='json')  
    
    return parser.parse_args()