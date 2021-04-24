import json

import flask
from flask import request

import jobs

app = flask.Flask(__name__)


@app.route("/jobs", methods=["POST"])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return (
            True,
            json.dumps({"status": "Error", "message": "Invalid JSON: {}.".format(e)}),
        )
    return json.dumps(jobs.add_job(job["start"], job["end"]))


@app.route("/job_status", methods=["GET"])
def get_job_status():
    try:
        job_id = request.args.get("job_id", type=str)
    except Exception as e:
        return (
            True,
            json.dumps({"status": "Error", "message": "Invalid JSON: {}.".format(e)}),
        )
    return json.dumps(jobs.get_job_status(job_id))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
