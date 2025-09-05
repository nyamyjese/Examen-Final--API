from fastapi import FastAPI
from datetime import date

app = FastAPI()

class Booking :
    client_name : str
    phone_number : str
    email : str
    room_number : int
    room_description : str
    reservation_date : date

bookings = List[Booking]()

@app.get("/booking")
def booking():
    return bookings

