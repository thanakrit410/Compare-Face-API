from flask import Flask, request, jsonify
from face_verify import compare_faces

app = Flask(__name__)


@app.route('/compare', methods=['POST'])
def verify():
    data = request.get_json()
    image1 = data['image1']
    image2 = data['image2']
    result = compare_faces(image1, image2)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
