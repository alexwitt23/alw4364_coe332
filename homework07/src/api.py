"""An API to submitte and query information about jobs."""

import flask
from flask import jsonify
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
            jsonify({"status": "Error", "message": "Invalid JSON: {}.".format(e)}),
        )
    return jsonify(jobs.add_job(job["start"], job["end"]))


@app.route("/job_status", methods=["GET"])
def get_job_status():
    try:
        job_id = request.args.get("job_id", type=str)
    except Exception as e:
        return (
            True,
            jsonify({"status": "Error", "message": "Invalid JSON: {}.".format(e)}),
        )
    return jsonify(jobs.get_job_status(job_id))


@app.route("/completed_jobs", methods=["GET"])
def get_completed_jobs():
    return jsonify(jobs.get_completed_jobs())


@app.route("/incomplete_jobs", methods=["GET"])
def get_incomplete_jobs():
    return jsonify(jobs.get_incomplete_jobs())


@app.route("/inprogress_jobs", methods=["GET"])
def get_inprogress_jobs():
    return jsonify(jobs.get_inprogress_jobs())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
