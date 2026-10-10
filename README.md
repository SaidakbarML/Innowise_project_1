# dorm project

this project loads students and rooms from json files to postgres, runs 4 queries and saves the result as json or xml. no orm, only sql. all the math is done in the database

## what queries do

- q1 rooms and how many students live in each
- q2 5 rooms with smalest avarage age
- q3 5 rooms with biggest age diffrence
- q4 rooms where boys and girls live together

## folders

- main.py just starts the app
- src/ all python code (cli, database, repository, exporter, app)
- sql/ schema, indexes and the 4 queries
- data/ input json files
- output/ results are saved here

## how to run with docker

make .env file like this

```
DB_NAME=postgres
DB_USER=postgres
DB_PASS=admin
DB_HOST=db
DB_PORT=5432
```

then run

```
docker compose run --rm app python main.py --students data/students.json --rooms data/rooms.json --format json
```

format can be json or xml, default is json. results will apear in output/json or output/xml

## how to run without docker

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py --students data/students.json --rooms data/rooms.json --format xml
```

you need postgres running and DB_HOST=localhost in .env

## index

i made index on students(room) because we join on it. i tested few other indexes with explain analyze and they dont change anything, the queries read all the students so postgres just scans the whole table anyway. index helps only when you search for small part like where room = 5

## notes

every run deletes the old tables and creates them again so dont worry about duplicates
