from flask import Flask, request, jsonify
from sportsbet.datasets import SoccerDataLoader

app = Flask(__name__)

# Endpoint to initialize the dataloader
@app.route('/init_dataloader', methods=['POST'])
def init_dataloader():
    data = request.json
    leagues = data['leagues']
    years = data['years']
    global dataloader
    dataloader = SoccerDataLoader({'league': leagues, 'year': years})
    return jsonify({'message': 'Dataloader initialized successfully'})

if __name__ == '__main__':
    app.run(debug=True)
