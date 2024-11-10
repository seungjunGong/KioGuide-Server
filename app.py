from flask import Flask, request, jsonify
import base64

app = Flask(__name__)


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

        # 이미지 처리가 성공적으로 완료되었음을 반환
        return jsonify({"message": "Image processed successfully"}), 200

    except Exception as e:
        # 오류 발생 시 예외 처리
        return jsonify({"error": f"Failed to process image: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
