from flask import Flask, request, jsonify
from flask_cors import CORS

# Importa los algoritmos desde tus módulos
from fcfs import fcfs
from sstf import sstf
from scan import scan
from cscan import cscan
from look import look
from clook import clook

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def hello():
    return {
        "message": "use /usage to get information"
    }

@app.route("/usage", methods=['GET'])
def help():
    return {
        "message": "use FIFO, SSTF, SCAN, CSCAN, LOOK or CLOOK algorithms",
        "instructions": {
            "endpoint": "/sched",
            "method": "POST",
            "payload": {
                "algorithm": "1:FCFS, 2:SSTF, 3:SCAN, 4:C-SCAN, 5:LOOK, 6:C-LOOK",
                "tracks": "number of cylinders",
                "arm": "initial position",
                "requests": "list of tracks"
            },
            "payload_example": {
                "algorithm": 1,
                "tracks": 200,
                "arm": 96,
                "requests": [125, 17, 23, 67, 90, 128, 189, 115, 97]
            },
            "description": "This endpoint performs disk scheduling algorithms"
        }
    }

@app.route("/sched", methods=['POST'])
def sched():
    try:
        # Obtén el payload del usuario
        data = request.get_json()
        algorithm = data.get("algorithm")
        tracks = data.get("tracks")
        arm = data.get("arm")
        requests = data.get("requests")

        # Validación básica de datos
        if not all([algorithm, tracks, arm, requests]):
            return jsonify({"error": "Missing fields in the payload"}), 400
        if not isinstance(algorithm, int) or algorithm not in range(1, 7):
            return jsonify({"error": "Invalid algorithm. Use values between 1 and 6"}), 400
        if not isinstance(tracks, int) or not isinstance(arm, int) or not isinstance(requests, list):
            return jsonify({"error": "Invalid data types"}), 400

        # Ejecuta el algoritmo correspondiente
        if algorithm == 1:  # FCFS
            result = fcfs(arm, requests)
        elif algorithm == 2:  # SSTF
            result = sstf(arm, requests)
        elif algorithm == 3:  # SCAN
            result = scan(arm, requests, tracks)
        elif algorithm == 4:  # C-SCAN
            result = cscan(arm, requests, tracks)
        elif algorithm == 5:  # LOOK
            result = look(arm, requests)
        elif algorithm == 6:  # C-LOOK
            result = clook(arm, requests)
        else:
            return jsonify({"error": "Invalid algorithm"}), 400

        # Respuesta exitosa
        return jsonify({
            "algorithm": algorithm,
            "tracks": tracks,
            "arm_start": arm,
            "requests": requests,
            "result": result
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


