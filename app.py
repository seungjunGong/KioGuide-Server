from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 이미지 저장 폴더 경로
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/upload', methods=['POST'])
def upload_image():
    # Android에서 전송된 파일이 있는지 확인
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    # 파일 가져오기
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # 파일 저장
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # 파일 처리 완료 메시지 반환
    return jsonify({"message": "Image received successfully", "file_path": file_path}), 200


if __name__ == '__main__':
    app.run(debug=True)
