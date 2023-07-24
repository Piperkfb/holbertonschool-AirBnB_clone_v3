#!/usr/bin/python3
"""
Comments
"""

# api/v1/views/index.py

from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    return {"status": "OK"}

    counts = {
        "your_object_type": storage.count("your_object_type"),
    }

    return jsonify(counts)
