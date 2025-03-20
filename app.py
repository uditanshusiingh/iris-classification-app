from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import pandas as pd
import cv2
import pytesseract
import requests
from datetime import datetime, timedelta

# Flask app setup
app = Flask(__name__)

DATABASE = "license_plates.db"
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"

WATCHLIST = {"ABC123", "XYZ789"}  # Add plate numbers for alerts


# ---- 1. DATABASE SETUP ---- #
def setup_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS plates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate_number TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate_number TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            alert_sent INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


# ---- 2. CHECK IF ALERT ALREADY SENT ---- #
def plate_already_alerted(plate_number):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT timestamp FROM alerts 
        WHERE plate_number = ? 
        ORDER BY timestamp DESC LIMIT 1
    """, (plate_number,))
    last_alert = cursor.fetchone()
    conn.close()

    if last_alert:
        last_alert_time = datetime.strptime(last_alert[0], "%Y-%m-%d %H:%M:%S")
        if datetime.now() - last_alert_time < timedelta(minutes=10):
            return True
    return False


# ---- 3. SEND TELEGRAM ALERT ---- #
def send_telegram_alert(plate_number):
    message = f"🚨 Alert! Detected License Plate: {plate_number}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)
    print("Telegram alert sent!")


# ---- 4. LICENSE PLATE DETECTION ---- #
def detect_license_plate():
    cap = cv2.VideoCapture(0)  # Open webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, threshold_plate = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        plate_text = pytesseract.image_to_string(threshold_plate, config="--psm 8").strip()

        if plate_text:
            print(f"Detected Plate: {plate_text}")

            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()

            cursor.execute("INSERT INTO plates (plate_number) VALUES (?)", (plate_text,))
            conn.commit()

            # Send alert if needed
            if plate_text in WATCHLIST and not plate_already_alerted(plate_text):
                send_telegram_alert(plate_text)

                cursor.execute("INSERT INTO alerts (plate_number, alert_sent) VALUES (?, 1)", (plate_text,))
                conn.commit()

            conn.close()

        cv2.imshow("License Plate Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# ---- 5. GET DATA FROM DATABASE WITH FILTERS ---- #
def get_data(search="", start_date="", end_date="", alert_status=""):
    query = "SELECT * FROM alerts WHERE 1=1"
    params = []

    if search:
        query += " AND plate_number LIKE ?"
        params.append(f"%{search}%")
    
    if start_date:
        query += " AND timestamp >= ?"
        params.append(start_date)
    
    if end_date:
        query += " AND timestamp <= ?"
        params.append(end_date)

    if alert_status:
        query += " AND alert_sent = ?"
        params.append(1 if alert_status == "sent" else 0)

    query += " ORDER BY timestamp DESC"

    conn = sqlite3.connect(DATABASE)
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


# ---- 6. FLASK ROUTES ---- #
@app.route("/", methods=["GET", "POST"])
def home():
    search = request.form.get("search", "")
    start_date = request.form.get("start_date", "")
    end_date = request.form.get("end_date", "")
    alert_status = request.form.get("alert_status", "")

    data = get_data(search, start_date, end_date, alert_status)
    return render_template("dashboard.html", data=data, search=search, start_date=start_date, end_date=end_date, alert_status=alert_status)

@app.route("/delete/<int:id>")
def delete_record(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alerts WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))


# ---- 7. RUN APP ---- #
if __name__ == "__main__":
    setup_database()
    app.run(debug=True)
