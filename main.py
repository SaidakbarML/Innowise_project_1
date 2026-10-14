from src.config import load_queries,setup_logging
from src.cli import parse_args
from src.app import App

setup_logging() # logs setup
args = parse_args() # read cmd arguments
queries = load_queries() # reads all 4 sql files
def main():
    app=App(args=args,queries=queries)
    app.run() # starts everyting

if __name__ == "__main__":
    main()