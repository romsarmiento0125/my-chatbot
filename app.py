import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.0-flash"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    if not GEMINI_API_KEY:
        return jsonify({"error": "GEMINI_API_KEY is not set on the server."}), 500

    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "No message provided."}), 400

    user_message = data["message"]
    history = data.get("history", [])

    # Build contents array with conversation history
    contents = []
    for entry in history:
        contents.append({
            "role": entry["role"],
            "parts": [{"text": entry["text"]}]
        })
    # Append the new user message
    contents.append({
        "role": "user",
        "parts": [{"text": user_message}]
    })

    payload = {"contents": contents}

    try:
        resp = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=60,
        )
        resp.raise_for_status()
        result = resp.json()

        ai_text = result["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"response": ai_text})

    except requests.exceptions.Timeout:
        return jsonify({"error": "Request to Gemini API timed out."}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Could not connect to Gemini API."}), 502
    except (KeyError, IndexError):
        return jsonify({"error": "Unexpected response format from Gemini API."}), 500
    except requests.exceptions.HTTPError as e:
        return jsonify({"error": f"Gemini API error: {e.response.status_code}"}), 502
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)