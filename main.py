from src.config import load_queries
from src.cli import parse_args
from src.app import App

args = parse_args()
queries = load_queries()
def main():
    app=App(args=args,queries=queries)
    app.run()

if __name__ == "__main__":
    main()