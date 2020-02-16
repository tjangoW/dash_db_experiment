import mongoengine as me
import random
import string


def bookingIdGenerator():
    # (26+10)**6 = 2176782336 (2E9)
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))


class BookingDates(me.EmbeddedDocument):
    checkIn = me.DateField(required=True)
    checkOut = me.DateField(required=True)


class Booking(me.Document):
    _id = me.StringField()
    customer = me.StringField(required=True)
    unit = me.StringField(required=True, max_length=200)
    dates = me.EmbeddedDocumentField(BookingDates, default=BookingDates)
    price = me.FloatField(required=True)  # embedded doc!
    platform = me.StringField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._id = bookingIdGenerator()
