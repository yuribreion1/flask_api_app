from flask_restful import Resource, reqparse

hotels = [
    {
        'id': 'alpha',
        'name': 'Alpha Hotel',
        'rating': 4.5,
        'price': 420.00,
        'city': 'São Paulo'
    },
    {
        'id': 'bravo',
        'name': 'Bravo Hotel',
        'rating': 3.0,
        'price': 320.00,
        'city': 'Rio de Janeiro'
    },
    {
        'id': 'charlie',
        'name': 'Charlie Hotel',
        'rating': 4.5,
        'price': 420.00,
        'city': 'Florianopolis'
    },
]


class Hotels(Resource):
    def get(self):
        return {
            'hotels': hotels
        }


class Hotel(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name')
    args.add_argument('rating')
    args.add_argument('price')
    args.add_argument('city')

    # Function to get hotel by ID
    def find_hotel(hotel_id):
        for hotel in hotels:
            if hotel['id'] == hotel_id:
                return hotel
        return None

    # Get hotel by ID
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found'}, 404

    # Add new hotel
    def post(self, hotel_id):

        request_data = self.args.parse_args()

        new_hotel = {
            'id': hotel_id,
            'name': request_data['name'],
            'rating': request_data['rating'],
            'price': request_data['price'],
            'city': request_data['city']
        }

        hotels.append(new_hotel)
        return new_hotel, 200

    def put(self, hotel_id):

        request_data = self.args.parse_args()

        new_hotel = {'id': hotel_id, **request_data}

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(new_hotel)
            return new_hotel, 200
        hotels.append(new_hotel)
        return new_hotel, 201

    def delete(self, id):
        pass

