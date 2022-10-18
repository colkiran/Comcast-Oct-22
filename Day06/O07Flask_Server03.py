
from flask import Flask, request
from flask_restful import Api, Resource

app  = Flask(__name__)
api = Api(app)

players = {
    'sachin': {'name': 'Sachin Tedulkar', 'runs': 34500, 'matches': 850, 'wickets': 350},
    'ponting': {'name': 'Ricky Ponting', 'runs': 25800, 'matches': 625, 'wickets': 185},
    'lara': {'name': 'Brain Lara', 'runs': 24350, 'matches':590, 'wickets': 230}
}

class Players(Resource):

    def get(self, player):
        return {player:players[player]}

    def put(self, player):
        players[player]['team'] = request.form['team']
        return {'result': players}

    def delete(self, player):
        if player in players:
            del players[player]
            return {'result': players}
        else:
            return {'KeyError': "Invalid Key, Please enter a valid key....."}


api.add_resource(Players, "/getplayer/<string:player>")

if __name__ == '__main__':
    app.run(debug=True)
