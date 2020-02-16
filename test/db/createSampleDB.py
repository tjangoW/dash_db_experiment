#############################################
# create using PyMongo (raw)
#############################################
import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["Moka"]
# mycol = mydb["Bookings"]
# mydict = { "name": "Ater", "address": "Lowstreet 27" }
# x = mycol.insert_one(mydict)
# print(x.inserted_id)


#############################################
# create using MongoEngine
#############################################
import mongoengine as me
from mongoengine.context_managers import switch_db, switch_collection
import src.mongoEngineDefinition as meDef
import src.dbUtils as utils
import datetime

db = utils.connectDB()
db.drop_database("Moka")
# db.Bookings.drop_collection("Bookings")

with switch_collection(meDef.Booking, 'Bookings') as Booking:  # change collection name instead of default class name
    bookings = [
        Booking(customer="Bla Ä",
                unit="best ever unit",
                dates={
                    "checkIn": datetime.date(2019, 12, 11),
                    "checkOut": datetime.date(2019, 12, 25)},
                price=10000),
        Booking(customer="dumb dumb",
                unit="worst ever unit",
                dates={
                    "checkIn": datetime.date(2019, 12, 11),
                    "checkOut": datetime.date(2019, 12, 25)},
                price=44444444444,
                platform="newspaper"),
        Booking(customer="Jan",
                unit="misc unit",
                dates={
                    "checkIn": datetime.date(2020, 1, 11),
                    "checkOut": datetime.date(2020, 1, 25)},
                price=44444,
                platform="newspaper"),
        Booking(customer="old record",
                unit="best ever unit",
                dates={
                    "checkIn": datetime.date(2011, 12, 11),
                    "checkOut": datetime.date(2011, 12, 25)},
                price=10000),

    ]

    [booking.save() for booking in bookings]
