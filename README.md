# 🎓 Student Attendance Management System using Face Recognition and QR Code

A smart attendance management system that automates student attendance tracking using **Face Recognition** and **QR Code Verification**. The system reduces manual attendance errors, prevents proxy attendance, and provides a fast, secure, and efficient attendance process.

---

## 📌 Features

### 👤 Face Recognition Attendance
- Register student face data.
- Real-time face detection and recognition.
- Automatic attendance marking.
- Prevents manual attendance manipulation.

### 📱 QR Code Attendance
- Unique QR code for each student.
- Fast attendance scanning.
- Alternative attendance method when face recognition is unavailable.

### 📊 Attendance Management
- Daily attendance records.
- Attendance history tracking.
- Student attendance reports.
- Export attendance data.

### 🔐 Admin Features
- Student registration and management.
- Attendance monitoring.
- View and manage attendance logs.
- Generate reports.

---

## 🛠️ Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Libraries
- OpenCV
- face_recognition
- NumPy
- Pandas
- QRCode
- MySQL

---

## 📂 Project Structure

```text
Student-Attendance-Management-System/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── database/
│
├── face_recognition/
│
├── qr_code/
│
├── attendance/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ppoobesh/Student-Attendance-Management-system-using-Face-and-QR-Code.git
cd Student-Attendance-Management-system-using-Face-and-QR-Code
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

---

## 📸 System Workflow

1. Admin registers students.
2. Student face data is captured and trained.
3. QR code is generated for each student.
4. Student can mark attendance using:
   - Face Recognition
   - QR Code Scanning
5. Attendance is automatically stored in the database.
6. Admin can view attendance records and reports.

---

## 🎯 Advantages

- Faster attendance process.
- Eliminates manual record keeping.
- Reduces proxy attendance.
- Improves accuracy.
- Secure and scalable.


## 🔮 Future Enhancements

- Email notifications.
- SMS alerts.
- Mobile application.
- Cloud database integration.
- AI-based attendance analytics.
- Multi-camera support.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📜 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

**Poobesh Pradeepkumar**

- GitHub: https://github.com/ppoobesh
- LinkedIn: (https://www.linkedin.com/in/poobeshpradeepkumar/)

---

⭐ If you found this project useful, consider giving it a star.
