from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# 최대 요청 크기 설정 (예: 16MB)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB


@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/upload', methods=['POST'])
def upload_image():
    # 요청에 JSON 데이터가 있는지 확인
    data = request.get_json()
    if not data or 'image' not in data:
        return jsonify({"error": "No image data provided"}), 400

    # Base64 이미지 데이터 가져오기
    base64_image = data['image']
    try:
        # Base64 데이터를 디코딩하여 바이너리 데이터로 변환
        image_data = base64.b64decode(base64_image)

        # Base64 데이터를 JSON으로 반환
        base64_image_str = base64.b64encode(image_data).decode('utf-8')
        response_data = {
            "message": "Image received successfully",
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"error": f"Failed to process image: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
