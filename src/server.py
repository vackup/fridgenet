import io
from flask import Flask, Response
from flask import request
from flask import jsonify
from PIL import Image

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def parse_image():
    print('Jiiripiiri', file=sys.stderr)
    print(image_data, file=sys.stderr)
    image_data = request.data
    Image.open(io.BytesIO(image_data))
    return jsonify(returnValue="tomato")
