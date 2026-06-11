from flask import Flask, render_template, flash, request, session,Response,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import mysql.connector
import yagmail
import cv2
import os
from datetime import datetime
time_now = datetime.now().strftime("%H:%M:%S")
date = datetime.now().strftime('%Y-%m-%d')
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app.config['DEBUG']

@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/userregister')
def userregister():
        return render_template('userregister.html')

@app.route('/userhome')
def userhome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM iotdata ORDER BY id DESC LIMIT 1")
    data = cur.fetchone()
    print(data)

    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    # cursor = conn.cursor()
    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM parameters1 ORDER BY id DESC LIMIT 1")
    data1 = cur1.fetchone()
    print(data1)
    conn2 = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    # cursor = conn.cursor()
    cur2 = conn2.cursor()
    cur2.execute("SELECT * FROM pondlocation ORDER BY id DESC LIMIT 1")
    data2 = cur2.fetchone()
    print(data2)


    return render_template('userhome.html',data=data,data1=data1,data2=data2)

@app.route("/adminhome")
def adminhome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM iotdata ORDER BY id DESC LIMIT 1")
    data = cur.fetchone()
    print(data)
    return render_template('adminhome.html',data=data)

@app.route("/stafflogin")
def stafflogin():
    return render_template('login.html')

@app.route("/iotdata")
def iotdata():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM iotdata ORDER BY id DESC LIMIT 10")
    data = cur.fetchall()

    conn2 = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    # cursor = conn.cursor()
    cur2 = conn2.cursor()
    cur2.execute("SELECT * FROM pondlocation ORDER BY id DESC LIMIT 1")
    data2 = cur2.fetchone()
    print(data2)
    return render_template('iotdata.html',data=data,data2=data2)

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' and request.form['password'] == 'admin':
           conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
           # cursor = conn.cursor()
           cur = conn.cursor()
           cur.execute("SELECT * FROM regtb ")
           data = cur.fetchall()
           return render_template('AdminHome.html', data=data)
       else:

           alert = 'Username or Password is wrong'
           return render_template('goback.html', data=alert)

@app.route("/newregister", methods=['GET', 'POST'])
def newregister():
    if request.method == 'POST':
        name1 = request.form['name']
        gender1 = request.form['gender']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']
        password = request.form['password']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('','" + name1 + "','" + gender1 + "','" + email + "','" + pnumber + "','" + address + "','" + password + "','')")
        conn.commit()
        conn.close()
        # return 'file register successfully'
    return render_template('login.html')

@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    error = None
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        session['uname'] = request.form['email']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where email='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
            cursor = conn.cursor()
            cursor.execute("SELECT * from regtb where email='" + username + "' and password='" + password + "'")
            data = cursor.fetchone()


            return render_template('staffhome.html', data=data )



@app.route('/staffhome')
def staffhome():
    username=session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    cursor = conn.cursor()
    cursor.execute("SELECT * from regtb where email='" + username + "'")
    data = cursor.fetchone()

    return render_template('staffhome.html',data=data)

@app.route('/addstudent')
def addstudent():
    return render_template('addstudent.html')



@app.route('/viewstudent')
def viewstudent():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    cursor = conn.cursor()
    cursor.execute("SELECT * from student")
    data = cursor.fetchall()

    return render_template('viewstudent.html',data=data)

@app.route('/logout')
def logout():
    return render_template('login.html')

@app.route('/Viewattdence')
def Viewattdence():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    cursor = conn.cursor()
    cursor.execute("SELECT * from attendance ")
    data = cursor.fetchall()

    return render_template('Viewattdence.html',data=data)




@app.route("/download")
def download():
             import csv
             pname=request.args.get("data1")
             print(pname)
             location = request.args.get("data2")
             print(location)
             date = request.args.get("data3")

             conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
             cursor = conn.cursor()
             cursor.execute("select * from iotdata where pname='"+str(pname)+"' and location='"+str(location)+"' ");
             #data = cursor.fetchall()
             #print(data)

             # Get column names
             columns = [i[0] for i in cursor.description]

             # Write data to CSV
             with open("output.csv", "w", newline="") as file:
                 writer = csv.writer(file)
                 writer.writerow(columns)  # Write column headers
                 writer.writerows(cursor.fetchall())  # Write data rows

             # Close connection
             cursor.close()
             conn.close()
             path="output.csv"

             print("Data exported successfully to output.csv")
             return send_file(path, as_attachment=True)

@app.route('/staudentlogin')
def staudentlogin():
        return render_template('staudentlogin.html')



@app.route("/studlogin", methods=['GET', 'POST'])
def studlogin():
    error = None
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        session['sname'] = request.form['email']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
        cursor = conn.cursor()
        cursor.execute("SELECT * from student where emailid='" + username + "' and regno='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
            cursor = conn.cursor()
            cursor.execute("SELECT * from student where emailid='" + username + "' and regno='" + password + "'")
            data = cursor.fetchone()


            return render_template('studenthome.html', data=data )
@app.route("/newstudent", methods=['GET', 'POST'])
def newstudent():
    if request.method == 'POST':
        regno = request.form['regno']
        name1 = request.form['name']
        gender1 = request.form['gender']
        dob = request.form['dob']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']
        dept = request.form['dept']
        year = request.form['year']

        file = request.files['file']
        file.save("static/upload/" + file.filename)
        # Import QRCode from pyqrcode
        import pyqrcode
        import png
        from pyqrcode import QRCode

        # String which represents the QR code
        s = str(regno)

        # Generate QR code
        url = pyqrcode.create(s)

        # Create and save the svg file naming "myqr.svg"
        url.svg("myqr.svg", scale=8)

        # Create and save the png file naming "myqr.png"
        url.png('static/qrimage/'+str(regno)+'.png', scale=6)
        qrname=str(regno)+'.png'
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO student VALUES ('','"+regno+"','" + name1 + "','" + gender1 + "','"+dob+"','" + email + "','" + pnumber + "','" + address + "','" + dept + "','"+year+"','"+file.filename+"','"+qrname+"')")
        conn.commit()
        conn.close()
        # return 'file register successfully'
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    cursor = conn.cursor()
    cursor.execute("SELECT * from student ")
    data = cursor.fetchall()

    return render_template('viewstudent.html',data=data)


@app.route('/studhome')
def studhome():
    username=session['sname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    cursor = conn.cursor()
    cursor.execute("SELECT * from student where emailid='" + username + "'")
    data = cursor.fetchall()

    return render_template('studenthome.html',data=data)
@app.route('/Viewattdence1')
def Viewattdence1():
    uname=session['sname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    cursor = conn.cursor()
    cursor.execute("SELECT * from student where emailid='" + uname + "'")
    data = cursor.fetchone()
    if data is None:
        print("No data Fount in this Records")
    else:
        regno=data[1]

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
    cursor = conn.cursor()
    cursor.execute("SELECT * from attendance where regno='"+regno+"'")
    data = cursor.fetchall()

    return render_template('Viewattdence1.html',data=data)

@app.route('/scanqrimage')
def scanqrimage():
    import cv2
    import numpy as np
    from pyzbar.pyzbar import decode


    def scan_qr():
        cap = cv2.VideoCapture(0)  # Open the webcam

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Decode QR codes in the frame
            for barcode in decode(frame):
                data = barcode.data.decode('utf-8')
                print(f"QR Code Data: {data}")
                print(data)

                # Draw rectangle around the QR code
                pts = barcode.polygon
                if len(pts) > 4:
                    hull = cv2.convexHull(np.array([pt for pt in pts], dtype=np.float32))
                    hull = list(map(tuple, np.squeeze(hull)))
                else:
                    hull = pts
                n = len(hull)
                for j in range(0, n):
                    cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)
                from datetime import datetime

                current_time = datetime.now().time()  # Get current time
                print(current_time)

                # Define time ranges
                morning_start = datetime.strptime("09:00", "%H:%M").time()
                morning_end = datetime.strptime("16:00", "%H:%M").time()

                morning_start1 = datetime.strptime("14:00", "%H:%M").time()
                morning_end1 = datetime.strptime("14:30", "%H:%M").time()
                if morning_start <= current_time <= morning_end:
                    conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
                    # cursor = conn.cursor()
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM student where regno='" + str(data) + "'")
                    data2 = cur.fetchone()
                    print(data2)
                    if data2 is None:
                        print("No Records Fount This Number")
                    else:
                        name=data2[2]
                        print(name)
                        print(date)
                        conn = mysql.connector.connect(user='root', password='', host='localhost', database='studentqrcode')
                        # cursor = conn.cursor()
                        cur = conn.cursor()
                        cur.execute(
                            "SELECT * FROM attendance where regno='" + str(data) + "' and date='"+str(date)+"'")
                        data1 = cur.fetchone()
                        print(data1)
                        if data1 is None:
                            print("hai")
                            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                           database='studentqrcode')
                            cursor = conn.cursor()
                            cursor.execute(
                                "INSERT INTO attendance VALUES ('','" + str(date) + "','" + str(data) + "','"+str(name)+"','" + str(current_time) + "','','present')")
                            conn.commit()
                            conn.close()

                elif morning_start1 <= current_time <= morning_end1:

                    conn = mysql.connector.connect(user='root', password='', host='localhost', database='Anganwadi')
                    # cursor = conn.cursor()
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM attendance where regno='" + str(data) + "' and date='" + date + "' and status='Present'")
                    data = cur.fetchone()
                    if data is None:
                        print("not")
                    else:
                            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                                           database='studentqrcode')
                            cursor = conn.cursor()
                            cursor.execute(
                                "update  attendance set outtime='" + str(current_time) + "' where regno='" + str(
                                    data) + "' and date='" + str(date) + "' ")
                            conn.commit()
                            conn.close()



            cv2.imshow("QR Scanner", frame)

            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    scan_qr()

    return "save"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)