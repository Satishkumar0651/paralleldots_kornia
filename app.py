from flask import Flask, request,send_file
from loftr_inference import matchimage_save_output
from os import environ

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_word():
    return "Hello World"


@app.route('/match_images', methods=['POST'])
def match_images():
    # Retrieve images from the request
    print(request.files)
    image1 = request.files.get('image1')
    image2 = request.files.get('image2')
    print(image1)
    print(image2)
    # Perform LoFTR inference on the images
    output_path = matchimage_save_output(image1, image2)

    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(environ.get('PORT', 8080)))
