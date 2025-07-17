

from flask import Flask, request, jsonify
from upload_CAM import handle_upload
from llm_extract import extract_entities
from form_selector import select_form
from form_populator import populate_form

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_cam():
    file = request.files['file']
    ocr_text = handle_upload(file)
    entities = extract_entities(ocr_text)
    form_name = select_form(entities)
    final_doc = populate_form(form_name, entities)
    return jsonify({"form_generated": final_doc})

if __name__ == "__main__":
    app.run(debug=True)
