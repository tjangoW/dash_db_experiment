# WebApp with dash

![CI without test](https://github.com/tjangoW/dash_db_experiment/workflows/CI%20without%20test/badge.svg)

a simple project to play with dash to create 
a simple web app with db query (and playing around with github action).

## How to run this
Guide from scratch (no python etc)
- clone/download the repo
- set up python
  - install python from <https://www.python.org/downloads/>. I am using python3.7 but i believe any python3 will work.
  - install the python requirements `pip install -r requirements.txt`
- install mongoDB (full documentation available here <https://docs.mongodb.com/manual/installation/>). I am using community edition.
  - I also installed the mongoDB Compass as it provides a GUI to view the db (I am a newbie to db stuff).
- running the webapp
  1. start a local mongoDB server. For windows, it is the *mongod.exe*.
  1. create a sample db to be used by the webapp by running the python file *test/db/createSampleDB.py*.
  1. finally, run the *src/webapp.py*.
- misc
  - I was trying PyCharm and find it working quite well with python project. By all means, feel free to pick your favourite poison of IDE :)
