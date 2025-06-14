from data_access.hotel_dao import HotelDAO
from data_access.room_dao import RoomDAO

class HotelService:
    def search_hotels_by_city(self, city):
        return HotelDAO.get_hotels_by_city(city)

    def filter_hotels_by_star(self, hotels, star_rating):
        return [hotel for hotel in hotels if hotel.stars == star_rating]

    def get_rooms_for_hotel(self, hotel_id):
        return RoomDAO.get_rooms_by_hotel(hotel_id)
