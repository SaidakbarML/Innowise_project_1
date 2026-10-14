import argparse 

def parse_args():
    parser = argparse.ArgumentParser() # cmd args parser

    parser.add_argument('-s','--students',required=True)  # path to students file
    parser.add_argument('-r', '--rooms',required=True)  # path to rooms file
    parser.add_argument('-f', '--format',choices=['json','xml'],default='json')  # output format json is default
    
    return parser.parse_args()