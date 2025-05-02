from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from ai_model.model import analyze_hair

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['image']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    result = analyze_hair(filepath)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
