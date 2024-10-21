# **Smart Vision Technology for Quality Control**  
*A Robotic Conveyor System for Automated Product Sorting and Inspection*
---
## **Screenshots**

- **Conveyor-Images**
![IMG_20241020_203810](https://github.com/user-attachments/assets/0faa4da6-3737-482b-8660-176a97d70b96)

- **List of Products**
![image](https://github.com/user-attachments/assets/4b4f8f38-131c-495f-ad38-9d9ab21b116c)

- **Products -**
Acnestar Soap,
Dove Pink Bar Beauty Bathing Bar,
GRB Instant Payasam (Kheer) Mix,
Manna Health Mix,
Lipton,
GRB Pure Cow Ghee,
 Harima Home Desserts Mango Flavour Ice Cream Mix Powder,
Himalaya Baby Lotion,
Aachi Pani Puri Kit,
Bigen Men's Speedy Color,
Laxolite,
Acnemoist Cream,
Ponds Bright Beauty Serum Cream,
Surf Excel,
Ariel,
Vim Dishwash Gel,
Pantene,
Britannia,
Parachute,
AXE,
Biotique,
Himalaya,
Softouch.

- **Fruits-**
Tomato,
Apple,
Mosambi.

- **Real-Time Object Detection**

![image](https://github.com/user-attachments/assets/263eb10b-2bb2-4442-99a1-91e3c213ebf1)

![image](https://github.com/user-attachments/assets/22db4ccf-0606-45ca-9dda-ef21563a6be0)



---

- **Front-End**
![image](https://github.com/user-attachments/assets/a85566db-8a7d-46b7-bd5e-f8b7781ce8fb)




- **Project Explanation (https://youtu.be/oNc2Ep8MHuY)**

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

**Connect the hardware components** (Microcontroller, Cameras, Sensors) and test the system.
![image](https://github.com/user-attachments/assets/096517ad-d1b8-4b5c-a7e4-af342fb27d4e)
![image](https://github.com/user-attachments/assets/9da92c21-19e1-456f-971e-5fe6265b701c)
![image](https://github.com/user-attachments/assets/28e78b0c-66eb-47d6-b1ef-8224e0e47948)
![image](https://github.com/user-attachments/assets/5d86b9d6-9d7c-4e96-9ce1-e2c4adc5c4db)
![image](https://github.com/user-attachments/assets/62260efe-fefd-47a8-890d-cfdbad7337c5)
![image](https://github.com/user-attachments/assets/205473f5-0dca-48d7-8e2d-0edf1b011c45)
![image](https://github.com/user-attachments/assets/fe1e209f-1cd8-4fb1-8efd-fab71c91d2f2)
![image](https://github.com/user-attachments/assets/7e5a6da7-fdb3-4942-bc35-c77383fabcac)




---

## **Project Workflow**

1. **Image Capture**: High-resolution cameras capture images of products as they pass through the conveyor system.
2. **Object Detection**: The images are processed using **YOLO v11** and **Random Forest** to detect product type and quality.
3. **Text Recognition**: The **OCR model** reads product details, including **expiry dates** and **serial numbers**.
4. **Sorting Mechanism**: Based on the detected product attributes, the NodeMCU activates the appropriate gate to sort the product.
5. **Database Logging**: Product data is stored in **MongoDB** for analysis and can be viewed through the web interface.
6. **User Interface**: The web application allows users to view product details, including defective products and expired items.

---
## **Team**
**![image](https://github.com/user-attachments/assets/d7e0ec1d-4c8b-44d5-87fd-94b8cc0564f8)**
## **Team Members**
- **Team Leader**: Karthik PP (IT) - Project architecture, microcontroller programming, and object detection.
- **Team Member 1**: Sridhar RA (IT) - Data processing and MongoDB integration.
- **Team Member 2**: Harish M (AI/DS) - Model training and implementation of YOLO v11 and Random Forest.
- **Team Member 3**: Benny Samuel S] (EEE) - Circuit design and hardware implementation of the conveyor system.
- **Team Member 4**: Mahesh P (ECE) - Sensor integration, servo control, and microcontroller programming.

---
