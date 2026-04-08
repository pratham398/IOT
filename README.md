# IOT
# Secure Framework for IoT Enabled Applications


## 📌 Project Overview

This project presents a **Secure Intrusion Detection Framework for IoT-enabled smart camera systems**. The system uses **face recognition and machine learning techniques** to detect whether a person appearing in a camera feed is a **known individual or an intruder**.

The framework integrates **IoT devices, computer vision, and machine learning** to improve surveillance security. When an unknown person is detected, the system automatically sends an **SMS alert notification** to the user, enabling quick response to potential security threats.

---

## 🎯 Objectives

The main objectives of this project are:

* To build an **IoT-enabled smart security framework**.
* To detect **intruders in real time using face recognition**.
* To store and identify **known individuals using a database**.
* To send **instant SMS alerts** when an intruder is detected.
* To enhance security systems using **Machine Learning and Computer Vision**.

---

## 📊 Applications

This intrusion detection system can be used in various environments:

* 🏠 Home security systems
* 🏬 Retail stores and businesses
* 🏭 Industrial environments
* 🏙 Smart cities surveillance
* ✈ Airports and transportation hubs

These smart cameras help detect suspicious activities and improve security by providing **real-time monitoring and alerts**.

---

## 🛠 Technologies Used

### Programming Language

* Python

### Libraries and Tools

* OpenCV (Computer Vision)
* Dlib (Face Recognition)
* NumPy
* Pandas
* Jupyter Notebook

### Database

* SQLite

### API Integration

* Twilio API (for SMS alerts)

---

## ⚙️ System Workflow

The proposed system works in two main stages:

### 1. Adding Known Faces to the Database

Images of authorized individuals are stored in a database so the system can recognize them later.

### 2. Intrusion Detection

The system analyzes live camera footage and compares detected faces with the stored database.

### Modules of the System

1. Live Video Feed Capture
2. Database Access
3. Machine Learning Face Detection Model
4. Face Comparison with Stored Database
5. Intruder Detection and SMS Alert Generation

If the detected face **does not match any stored profile**, the system classifies it as an **intruder** and sends an alert.

---

## 🧠 Face Recognition Model

The system uses **Dlib’s HOG (Histogram of Oriented Gradients) based Face Recognition Model**.

### Process

1. Detect faces in the video frame
2. Identify facial landmarks (eyes, nose, lips)
3. Convert facial features into numerical descriptors
4. Compare descriptors with stored database
5. Classify the person as **known or intruder**

This approach provides **high accuracy in face recognition applications**.

---

## 📱 Intruder Alert System

When an intruder is detected:

* The system captures the image of the intruder.
* The image is stored for security purposes.
* An **SMS alert is sent using the Twilio API** to notify the user immediately.

This ensures **fast response to potential threats**.

---

## 📂 Project Structure

```
Secure-IoT-Intrusion-Detection
│
├── capture.py
├── script.py
├── reset_db.py
├── database
│
├── images
│
└── README.md
```

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```
git clone https://github.com/your-username/secure-iot-intrusion-detection.git
```

### Step 2: Install Required Libraries

```
pip install opencv-python dlib numpy pandas
```

### Step 3: Run the System

```
python script.py
```

The system will start monitoring the camera feed and detect intruders.

---

## 📈 Results

The system successfully:

* Detects faces from live camera feeds
* Identifies whether a person is **known or unknown**
* Sends **real-time SMS alerts** on intrusion detection
* Stores captured images of intruders for record keeping

This makes the framework suitable for **real-world security applications**.

---

## 🔮 Future Improvements

Future enhancements of the system may include:

* Improving performance in **low lighting conditions**
* Adding **behavior analysis and anomaly detection**
* Implementing **deep learning-based models**
* Integrating **edge computing for faster processing**
* Adding **cloud-based monitoring systems**

---

## 👨‍💻 Author

**Pratham Rana**
B.Tech – Computer Science & Engineering
Graphic Era Hill University, Dehradun

