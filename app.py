from flask import Flask, jsonify, request

app = Flask(__name__)

core_items = [
    {"id": 1, "name": "Marketing Professionals"},
    {"id": 2, "name": "Software Engineers"},
    {"id": 3, "name": "Human Resources Managers"},
    {"id": 4, "name": "Sales Executives"},
    {"id": 5, "name": "Financial Analysts"},
    {"id": 6, "name": "Project Managers"},
    {"id": 7, "name": "Data Scientists"},
    {"id": 8, "name": "Healthcare Administrators"},
    {"id": 9, "name": "IT Support Specialists"},
    {"id": 10, "name": "Product Managers"},
]


@app.route("/core_items", methods=["GET", "POST"])
def get_core_itmes():
    if request.method == "GET":
        if len(core_items) > 0:
            return jsonify(core_items)
        else:
            return "Not Found", 404
    if request.method == "POST":
        app.logger.info(request.form["name"])
        new_item = request.form["name"]
        last_id = core_items[-1]["id"]
        core_items.append({"id": last_id + 1, "name": new_item})
        return jsonify(core_items), 201


@app.route("/core_item/<int:id>", methods=["GET", "PUT", "DELETE"])
def get_core_items_by_id(id):
    if request.method == "GET":
        for item in core_items:
            if item["id"] == id:
                return jsonify(item), 200
        return jsonify({"error": "Element not found"}), 404

    if request.method == "PUT":
        for item in core_items:
            if item["id"] == id:
                item["name"] = request.form["name"]
                return jsonify(item)
        return jsonify({"error": "Element not found"}), 404

    if request.method == "DELETE":
        for item in core_items:
            if item["id"] == id:
                core_items.remove(item)
                return jsonify({"message": "Item deleted successfully"}), 200
        return jsonify({"error": "Element not found"}), 404
