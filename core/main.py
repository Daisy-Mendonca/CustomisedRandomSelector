from core.selector import RandomSelector
from flask import Flask, jsonify, render_template
import os
import json
from flask import request

from backend.src.data_reader import DataReader
from backend.src.update_entry import new_timestamp
from backend.services.settings import FILE_PATH, PORT

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../frontend/templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../frontend/static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
data_reader= DataReader(FILE_PATH)

@app.route('/generate', methods=['POST'])
def run_dish_selector():
    data = request.get_json()
    selected_category = data.get('category', None)
    selected_type = data.get('type', None)
    data_frame = data_reader.read_data_db() 
    random_dish = RandomSelector().select_element(data_frame, selected_category, selected_type)
    return jsonify({"selected_dish":random_dish})   

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-categories')
def get_category():
    categories = data_reader.get_categories()
    return jsonify({"categories": categories})

@app.route('/get-types')
def get_types():
    types = data_reader.get_types()
    return jsonify({"types": types})

@app.route('/like-choice', methods=['POST'])
def like_choice():
    data = request.get_json()
    liked = data.get('liked', False)
    selected_dish = data.get('dish', None)
    if liked:
        new_timestamp(selected_dish)
    print(f"User liked the choice: {liked}")
    return jsonify({"status": "success"}), 200

@app.route('/selection-status', methods=['GET'])
def selection_status():
    df = data_reader.read_data_db()
    return jsonify({
        "Breakfast": RandomSelector().food_selected_today(df, "Breakfast"),
        "Meal": RandomSelector().food_selected_today(df, "Meal")
    })

@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8000, debug=True, use_reloader=False)
    app.run(
    host="0.0.0.0",
    port=PORT,
    debug=True
)
