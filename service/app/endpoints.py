import json

from flask import Flask, jsonify, request

from service.utils.helper import (compute_hamming, compute_jaro,
                                  compute_levenshtein_distance, compute_ratio)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home() -> None:
    """Return a friendly HTTP greeting."""
    return "Compute Levenshtein Distances"


@app.route("/distance/lev/json", methods=["GET"])
def get_lev():
    request_data = request.get_json()
    dump = dict(request_data)
    if "weights" in dump:
        dump["weights"] = tuple(dump["weights"])

    result = {
        "sentences1": dump["s1"],
        "sentences2": dump["s2"],
        "output": {"levenshtein distance": compute_levenshtein_distance(dump)},
    }
    return jsonify(result)


@app.route("/distance/ratio/json", methods=["GET"])
def get_ratio():
    request_data = request.get_json()
    dump = dict(request_data)
    result = {
        "sentences1": dump["s1"],
        "sentences2": dump["s2"],
        "output": {"indel similarity": compute_ratio(dump)},
    }
    return jsonify(result)


@app.route("/distance/hamming/json", methods=["GET"])
def get_hamming():
    request_data = request.get_json()
    dump = dict(request_data)
    result = {
        "sentences1": dump["s1"],
        "sentences2": dump["s2"],
        "output": {"hamming distance": compute_hamming(dump)},
    }
    return jsonify(result)


@app.route("/distance/jaro/json", methods=["GET"])
def get_jaro():
    request_data = request.get_json()
    dump = dict(request_data)
    result = {
        "sentences1": dump["s1"],
        "sentences2": dump["s2"],
        "output": {"jaro similarity": compute_jaro(dump)},
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
