from flask import Flask, request, jsonify
import json

gestureData = None

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    name = data.get("Name")
    symbol = data.get("Symbol")
    count = data.get("Count")
    try:
        with open("players.json", "r") as file:
            players = json.load(file)
    except:
        players = {}
    if name in players:
        success = False
        for i in range(len(players[name])):
            if players[name][i]['Symbol'] == symbol:
                players[name][i]['Count'] += count
                success = True
        if not success:
            players[name].append({"Symbol": symbol, "Count": count})
    else:
        players[name] = [{"Symbol": symbol, "Count": count}]
    with open("players.json", "w") as file:
        json.dump(players, file)
    return jsonify({"status": "success"})

@app.route("/player/<name>", methods=["GET"])
def get_player(name):
    try:
        with open("players.json", "r") as file:
            players = json.load(file)
    except:
        return jsonify({"error": "No player data found"})
    if name in players:
        return jsonify({"data":players[name]})
    else:
        return jsonify({"error": "Player not found"})

@app.route('/gesture', methods=['GET'])
def get_gesture():
    global gestureData
    if gestureData is None:
        try:
            with open("all_data.json", "r") as json_file:
                gestureData = json.load(json_file)
        except Exception as e:
            return jsonify({"error": f"Error loading data: {e}"}), 500
    return jsonify(gestureData)

if __name__ == "__main__":
    app.run(debug=True)