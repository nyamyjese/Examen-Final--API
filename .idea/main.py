from fastapi import FastAPI
from datetime import date
from starlette.response import JSONResponse

app = FastAPI()

class Booking :
    client_name : str
    phone_number : str
    email : str
    room_number : int
    room_description : str
    reservation_date : date

bookings = List[Booking]()

@app.get("/booking" , responnse_model = List[Booking])
def booking():
    return bookings

@app.post("/booking" , response_model = List[Booking])
def create_booking(new_booking: Booking):
    for booking in bookings:
        if booking.room_number == new_booking.room_number and booking.reservation_date == new_booking.reservation_date:
            return JSONResponse(
                content = {
                    "success": False,
                    "error" : f"La chambre {new_booking.room_number} est déjà réservée"
                }, status_code = 409
            )
    bookings.append(new_booking)
    return JSONResponse(
        content = {
            "success": True,
        }, status_code = 200
    )