from flask import Flask, request
import mysql.connector
import os
import cv2
import numpy as np
import pyqrcode
from pyzbar.pyzbar import decode
from datetime import datetime
from tensorflow.keras.models import load_model
import pickle

app = Flask(__name__)

DATASET = "dataset"
MODEL_DIR = "model"
QR_FOLDER = "static/qrimage"

os.makedirs(DATASET, exist_ok=True)
os.makedirs(QR_FOLDER, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

# ---------------- DATABASE CONNECTION ---------------- #

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="studentqrcode"
    )

# ---------------- HOME ---------------- #

@app.route('/')
def home():
    return "QR + CNN Attendance System Running"

# ---------------- REGISTER STUDENT ---------------- #

@app.route('/register', methods=['POST'])
def register():

    regno = request.form['regno']
    name = request.form['name']
    gender = request.form['gender']
    dob = request.form['dob']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    department = request.form['department']
    year = request.form['year']

    file = request.files['profileimage']
    file.save("static/" + file.filename)

    # Generate QR
    qr = pyqrcode.create(regno)
    qr.png(os.path.join(QR_FOLDER, regno + ".png"), scale=6)

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO student
        (regno,name,gender,dob,emailid,phone,address,department,year,profileimage,qrimage)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,(regno,name,gender,dob,email,phone,address,
         department,year,file.filename,regno+".png"))

    conn.commit()
    conn.close()

    return "Student Registered Successfully"

# ---------------- CAPTURE FACE ---------------- #

@app.route('/capture/<regno>')
def capture(regno):

    path = os.path.join(DATASET, regno)
    os.makedirs(path, exist_ok=True)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            count += 1
            face = gray[y:y+h,x:x+w]
            face = cv2.resize(face,(100,100))

            cv2.imwrite(f"{path}/{count}.jpg", face)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow("Capturing Face Images", frame)

        if cv2.waitKey(1)==27 or count>=30:
            break

    cap.release()
    cv2.destroyAllWindows()

    return f"Captured {count} images"

# ---------------- TRAIN MODEL ---------------- #

@app.route('/train')
def train():
    os.system("python train_model.py")
    return "Model Trained Successfully"

# ---------------- SCAN QR + CNN ---------------- #

@app.route('/scan')
def scan():

    model = load_model("model/face_model.h5")
    le = pickle.load(open("model/labels.pkl","rb"))

    conn = get_db()
    cursor = conn.cursor()

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        qr_codes = decode(frame)

        for qr in qr_codes:
            qr_data = qr.data.decode('utf-8')

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = cv2.resize(gray,(100,100))
            face = face.reshape(1,100,100,1)/255.0

            prediction = model.predict(face)
            predicted_regno = le.inverse_transform(
                [np.argmax(prediction)]
            )[0]

            if predicted_regno == qr_data:

                today = datetime.now().strftime("%Y-%m-%d")
                time_now = datetime.now().strftime("%H:%M:%S")

                cursor.execute(
                    "SELECT * FROM attendance WHERE regno=%s AND date=%s",
                    (qr_data,today)
                )

                if cursor.fetchone() is None:

                    cursor.execute(
                        "SELECT name FROM student WHERE regno=%s",
                        (qr_data,)
                    )
                    name = cursor.fetchone()[0]

                    cursor.execute("""
                        INSERT INTO attendance
                        (date,regno,name,intime,outtime,status)
                        VALUES (%s,%s,%s,%s,%s,%s)
                    """,(today,qr_data,name,time_now,"","present"))

                    conn.commit()
                    print("Attendance Marked")

        cv2.imshow("QR + CNN Scanner", frame)

        if cv2.waitKey(1)==27:
            break

    cap.release()
    cv2.destroyAllWindows()
    conn.close()

    return "Scan Completed"

if __name__ == '__main__':
    app.run(debug=True)