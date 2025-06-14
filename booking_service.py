from data_access.database_connection import DatabaseConnection
from data_access.booking_dao import BookingDAO
from datetime import datetime
from business_logic.dynamic_pricing import DynamicPricing
from model.booking import Booking
from model.invoice import Invoice

class BookingService:
    @staticmethod
    def create_booking(guest_id, room, check_in, check_out):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()

        nights = (check_out - check_in).days
        check_in_month = check_in.month
        dynamic_price = DynamicPricing.apply_seasonal_price(room.price_per_night, check_in_month)
        total_amount = round(nights * dynamic_price, 2)

        cursor.execute("""
            INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, total_amount)
            VALUES (?, ?, ?, ?, ?)
        """, (guest_id, room.room_id, check_in.isoformat(), check_out.isoformat(), total_amount))
        booking_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO Invoice (booking_id, total_amount)
            VALUES (?, ?)
        """, (booking_id, total_amount))

        conn.commit()

        return Booking(booking_id, guest_id, room.room_id, check_in, check_out, False, total_amount)

    @staticmethod
    def cancel_booking(booking_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Booking SET is_cancelled = 1 WHERE booking_id = ?", (booking_id,))
        cursor.execute("UPDATE Invoice SET total_amount = 0 WHERE booking_id = ?", (booking_id,))
        conn.commit()

    @staticmethod
    def get_bookings_by_guest(guest_id):
        return BookingDAO.get_bookings_by_guest(guest_id)
