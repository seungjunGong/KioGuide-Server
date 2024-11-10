from flask import Flask, request, jsonify
import os
import base64

app = Flask(__name__)

# 이미지 저장 폴더 경로
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


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

        # 이미지 파일 이름 생성 및 저장 경로 설정
        file_name = "uploaded_image.jpg"
        file_path = os.path.join(UPLOAD_FOLDER, file_name)

        # 바이너리 데이터를 파일로 저장
        with open(file_path, "wb") as file:
            file.write(image_data)

        # 저장 성공 메시지 반환
        return jsonify({"message": "Image received successfully", "file_path": file_path}), 200

    except Exception as e:
        # 오류 발생 시 예외 처리
        return jsonify({"error": f"Failed to process image: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
