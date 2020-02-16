from mongoengine.queryset.visitor import Q
import mongoengine as me
import src.mongoEngineDefinition as meDef
import datetime
from mongoengine.context_managers import switch_db, switch_collection
import pandas as pd


def connectDB():
    db = me.connect('Moka', host='localhost', port=27017)
    # mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
    return db


def _displayList(key, qList):
    tmp = [getattr(q, key) for q in qList.order_by('dates')]
    print(tmp)
    return tmp


def bookingQuery(*args, **kwargs):
    with switch_collection(meDef.Booking, 'Bookings') as Booking:
        return _query(Booking, *args, **kwargs)


def _query(collection, *args, **kwargs):
    tmp = collection.objects(*args, **kwargs)
    _displayList("customer", tmp)
    return tmp


def bookingQueryAsDf(*args, **kwargs):
    bookings = bookingQuery(*args, **kwargs)
    tmp_list = [b.to_mongo() for b in bookings]
    # converting to df for easier manipulation
    tmp_df = pd.DataFrame(tmp_list)
    dates_loc = tmp_df.columns.get_loc('dates')
    dates = tmp_df.pop("dates")
    dates_check_in = dates.apply(lambda x: x["checkIn"].strftime('%d-%m-%Y'))
    dates_check_out = dates.apply(lambda x: x["checkOut"].strftime('%d-%m-%Y'))
    tmp_df.insert(dates_loc, "check in", dates_check_in)
    tmp_df.insert(dates_loc+1, "check out", dates_check_out)

    # del tmp_df["_id"]
    return tmp_df


if False:
    bookingQuery()
    bookingQuery(dates__checkIn__lt=datetime.date(2020, 1, 1))
    bookingQuery(
            Q(dates__checkIn__lt=datetime.date(2019, 12, 31)) &
            Q(dates__checkOut__gt=datetime.date(2019, 12, 1)))

if __name__ == "__main__":
    connectDB()
    df = bookingQueryAsDf()
