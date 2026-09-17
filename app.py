```python
import os
import json
import time
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

thu_muc = "chats"

if not os.path.exists(thu_muc):
    os.makedirs(thu_muc)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chats")
def danh_sach_chat():
    ds = []

    for ten_file in os.listdir(thu_muc):

        if ten_file.endswith(".json"):

            with open(
                os.path.join(thu_muc, ten_file),
                "r",
                encoding="utf-8"
            ) as f:
                chat = json.load(f)

            ds.append({
                "id": ten_file[:-5],
                "ten": chat["ten"]
            })

    return jsonify(ds)


@app.route("/chat/<id>")
def mo_chat(id):

    duong_dan = os.path.join(
        thu_muc,
        id + ".json"
    )

    if not os.path.exists(duong_dan):
        return jsonify({
            "loi": "Không tìm thấy cuộc trò chuyện"
        })

    with open(
        duong_dan,
        "r",
        encoding="utf-8"
    ) as f:
        chat = json.load(f)

    return jsonify(chat)


@app.route("/chat/<id>", methods=["DELETE"])
def xoa_chat(id):

    duong_dan = os.path.join(
        thu_muc,
        id + ".json"
    )

    if os.path.exists(duong_dan):

        os.remove(duong_dan)

        return jsonify({
            "ok": True
        })

    return jsonify({
        "ok": False
    })


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    cauhoi = data.get("cauhoi", "")
    id = data.get("id")

    if cauhoi == "":
        return jsonify({
            "loi": "Bạn chưa nhập câu hỏi"
        }), 400

    if not id:
        id = str(int(time.time() * 1000))

    duong_dan = os.path.join(
        thu_muc,
        id + ".json"
    )

    if os.path.exists(duong_dan):

        with open(
            duong_dan,
            "r",
            encoding="utf-8"
        ) as f:
```
