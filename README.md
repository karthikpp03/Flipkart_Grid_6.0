# **Smart Vision Technology for Quality Control**  
*A Robotic Conveyor System for Automated Product Sorting and Inspection*

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
![Contributors](https://img.shields.io/badge/contributors-5-brightgreen.svg)  
![Python](https://img.shields.io/badge/Language-Python-yellow.svg)

---
## **Screenshots**

- **Real-Time Object Detection**
![Object Detection](https://example.com/object-detection.png)

- **Project Explanation**
![Web Interface](https://youtu.be/oNc2Ep8MHuY?si=BACJ-F_PqxqwT8Cq)

---
## **Project Overview**

Welcome to the **Smart Vision Technology for Quality Control** project! This innovative system integrates **YOLO v11**, **Random Forest**, and **Custom OCR** technologies to automate the inspection and sorting of products on a conveyor belt. Our system is designed to detect product quality, sort items, and analyze product information like expiry dates, serial numbers, and defects—offering a robust solution for modern-day quality control needs in industries like **food processing**, **healthcare**, and **consumer goods**.

## **Key Features**
- **Real-Time Object Detection** using **YOLO v11** and **Random Forest** for accurate identification of products and their quality.
- **Custom OCR** model to extract product text details such as **expiry dates**, **serial numbers**, and other label information.
- A **conveyor system** powered by **DC motors**, integrated with **ultrasonic sensors** and **servo-controlled gates** to sort products automatically.
- **High-resolution cameras** and warm lighting for optimal object detection, avoiding shadows and reflections.
- A user-friendly **web interface** to track product details, expired items, and defective products, built using **HTML**, **CSS**, **JavaScript**, and **Flask**.
- A **MongoDB** database for storing product data, including classification results and quality control reports.

---

## **Hardware Specifications**
- **Conveyor System**: 5 feet long, 2 feet wide, with three sorting gates controlled by **servo motors**.
- **ESP8266 Microcontroller**: Controls ultrasonic sensors, motors, and handles the object detection logic.
- **High-Resolution Cameras**: Captures images of products for analysis and sorting.
- **Warm LED Lighting**: Ensures optimal image clarity by minimizing reflections and shadows.
- **12V DC Motor**: Powers the conveyor belt, with PVC pipes used as rollers for smooth motion.
- **Ultrasonic Sensors**: Detect objects on the conveyor belt and trigger sorting mechanisms.

---

## **Software & Technologies Used**
- **Python**: Core language used for implementing object detection and OCR models.
- **YOLO v11**: Used for real-time object detection and classification.
- **Random Forest**: Supports classification and prediction of defective products.
- **EC OCR (Custom OCR Model)**: For detecting text-based details like product names, serial numbers, and expiry dates.
- **MongoDB**: NoSQL database used to store product data and inspection results.
- **NodeMCU**: To control sorting gates and manage sensor data.
- **Web Technologies**: HTML, CSS, JavaScript, Flask for building an intuitive user interface.
- **OpenCV**: For image processing and object detection.
  
---

## **Installation & Setup Instructions**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/smart-vision-quality-control.git
   cd smart-vision-quality-control
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MongoDB:**
   Set up MongoDB and update the connection string in the configuration file:
   ```bash
   MONGODB_URI=mongodb://localhost:27017/smartvision
   ```

4. **Run the YOLO detection system:**
   ```bash
   python yolo_detect.py
   ```

5. **Launch the web interface:**
   ```bash
   python app.py
   ```

6. **Connect the hardware components** (Microcontroller, Cameras, Sensors) and test the system.

---

## **Project Workflow**

1. **Image Capture**: High-resolution cameras capture images of products as they pass through the conveyor system.
2. **Object Detection**: The images are processed using **YOLO v11** and **Random Forest** to detect product type and quality.
3. **Text Recognition**: The **OCR model** reads product details, including **expiry dates** and **serial numbers**.
4. **Sorting Mechanism**: Based on the detected product attributes, the NodeMCU activates the appropriate gate to sort the product.
5. **Database Logging**: Product data is stored in **MongoDB** for analysis and can be viewed through the web interface.
6. **User Interface**: The web application allows users to view product details, including defective products and expired items.

---



## **Team Members**
- **Team Leader**: Karthik PP (IT) - Project architecture, microcontroller programming, and object detection.
- **Team Member 1**: Sridhar RA (IT) - Data processing and MongoDB integration.
- **Team Member 2**: Harish M (AI/DS) - Model training and implementation of YOLO v11 and Random Forest.
- **Team Member 3**: Benny Samuel S] (EEE) - Circuit design and hardware implementation of the conveyor system.
- **Team Member 4**: Mahesh P (ECE) - Sensor integration, servo control, and microcontroller programming.

---
