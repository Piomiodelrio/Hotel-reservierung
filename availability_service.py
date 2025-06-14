from data_access.database_connection import DatabaseConnection
from datetime import datetime

class AvailabilityService:
    @staticmethod
    def is_room_available(room_id, check_in, check_out):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM Booking 
            WHERE room_id = ? AND is_cancelled = 0 AND
                (check_in_date < ? AND check_out_date > ?)
        """
        cursor.execute(query, (room_id, check_out, check_in))
        return cursor.fetchone() is None

    @staticmethod
    def filter_available_rooms(rooms, check_in, check_out):
        available_rooms = []
        for room in rooms:
            if AvailabilityService.is_room_available(room.room_id, check_in, check_out):
                available_rooms.append(room)
        return available_rooms
