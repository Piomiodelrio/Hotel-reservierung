from data_access.database_connection import DatabaseConnection
from model.invoice import Invoice

class InvoiceService:
    @staticmethod
    def get_invoice_by_booking_id(booking_id):
        conn = DatabaseConnection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Invoice WHERE booking_id = ?", (booking_id,))
        row = cursor.fetchone()
        if row:
            return Invoice(row["invoice_id"], row["booking_id"], row["issue_date"], row["total_amount"])
        return None
