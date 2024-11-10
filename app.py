from flask import Flask, request, jsonify
import base64

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB


@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/upload', methods=['POST'])
def upload_image():
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400

    data = request.get_json()
    if not data or 'image' not in data:
        return jsonify({"error": "No image data provided"}), 400

    base64_image = data['image']
    try:
        image_data = base64.b64decode(base64_image)
        response_data = {
            "message": "Image received successfully",
        }
        return jsonify(response_data), 200

    except base64.binascii.Error:
        # Base64 디코딩 오류
        return jsonify({"error": "Invalid Base64 image data"}), 400

    except Exception as e:
        return jsonify({"error": f"Failed to process image: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
