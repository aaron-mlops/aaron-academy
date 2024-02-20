import time
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health_check", methods=["GET"])
def health_check():
    return jsonify(msg="server alive")


@app.route("/sleep", methods=["GET"])
def sleep_one_second():
    start_time = time.time()
    time.sleep(1)
    end_time = time.time()
    return jsonify(msg=f"elapsed_time: {end_time - start_time}")


@app.route("/count", methods=["GET"])
def count_50_million():
    start_time = time.time()
    for _ in range(50000000):
        pass
    end_time = time.time()
    return jsonify(msg=f"elapsed_time: {end_time - start_time}")

