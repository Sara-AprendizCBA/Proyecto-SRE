import os
from flask import Flask
import pymysql

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "app_user")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME", "appdb")


@app.route("/")
def home():
    return {"status": "ok", "message": "API viva"}, 200


@app.route("/health")
def health():
    try:
        conn = pymysql.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD,
            database=DB_NAME, connect_timeout=3
        )
        conn.close()
        return {"status": "ok", "db": "conectada"}, 200
    except Exception as e:
        return {"status": "error", "db": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)