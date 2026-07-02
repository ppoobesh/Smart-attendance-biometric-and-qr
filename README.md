# Smart Biometric & QR-Based Attendance Management System

A robust, full-stack automated attendance tracking solution utilizing Computer Vision (Facial Recognition) and encrypted QR Code verification. This system is designed to streamline entry logs, eliminate proxy attendance, and provide real-time data synchronization with an intuitive dashboard interface.

## 🚀 Key Features
* **Dual-Layer Verification:** Integrates AI-driven face recognition along with dynamic QR-code scanning for high-accuracy tracking.
* **Computer Vision Pipeline:** Real-time face detection, alignment, and facial feature extraction for seamless identification.
* **Secure QR Code Processing:** Generates and decodes individual student/user QR tokens for instant authentication.
* **Automated Data Lifecycle:** Performs automated CRUD operations to log timestamp records, update relational database tables, and track daily history.
* **Dynamic Dashboard Reporting:** Comprehensive reporting features allowing administrators to manage rosters, view metrics, and export data.

## 🛠️ Technical Stack
* **Languages:** Python, SQL, JavaScript
* **Computer Vision / AI:** OpenCV, Face Recognition libraries
* **Backend Framework:** Flask
* **Database:** MySQL
* **Tools & Utilities:** NumPy, Pandas, PyQRCode

## 🏗️ System Architecture & Workflow
1. **User Enrollment:** Captures facial data vectors and securely saves them along with a generated unique QR code.
2. **Authentication Loop:** 
   * Camera feed triggers the Computer Vision engine to match facial embeddings against the database.
   * Companion QR scanner reads the localized token for instant structural cross-verification.
3. **Log Update:** Upon successful validation, a database script handles real-time attendance logging with exact Unix/Server timestamps.

## 💻 Installation & Setup
```bash
# Clone the repository
git clone [https://github.com/ppoobesh/Smart-attendance-biometric-and-qr.git](https://github.com/ppoobesh/Smart-attendance-biometric-and-qr.git)

# Navigate to the directory
cd Smart-attendance-biometric-and-qr

# Install required packages
pip install -r requirements.txt

# Run the application
python project.py
