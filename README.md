# Facial Attendance Portal

## Overview
The Facial Attendance Portal is an innovative project designed to streamline attendance management using facial recognition technology. This application leverages the OpenCV and face_recognition libraries to identify and track individuals, making attendance marking more efficient and secure.

## Features
- **Facial Recognition**: Uses the `face_recognition` library to identify individuals based on facial features.
- **Attendance Marking**: Automatically marks attendance and logs the timestamp.
- **Real-time Updates**: Provides real-time feedback and updates via a user-friendly interface.
- **Messaging Integration**: Sends notifications about attendance via WhatsApp using `pywhatkit`.

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Pip (Python package installer)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/stva01/Face_Attendance.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Face_Attendance
    ```
3. Install the required Python packages:
    ```bash
    pip install opencv-python numpy face_recognition pywhatkit
    ```

## Usage
1. **Prepare your facial images**:
    - Place images of individuals in the `imageattendance` directory. Ensure each image file name corresponds to the person's name.
2. **Run the application**:
    ```bash
    python final.py
    ```
3. **Use the application interface**:
    - Enter the roll number in the provided input field and click on "Click For Attendance" to start the facial recognition process.

## Code Explanation
- **Facial Recognition**: The application captures images from the webcam, processes them to detect and recognize faces, and matches them with known faces.
- **Attendance Logging**: The attendance is recorded in a CSV file with the timestamp.
- **Messaging**: Notifications about attendance are sent via WhatsApp using `pywhatkit`.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## Acknowledgements
- **OpenCV**: For image processing.
- **face_recognition**: For facial recognition capabilities.
- **pywhatkit**: For WhatsApp messaging.
- **Tkinter**: For creating the GUI.

## Contact
For any questions or feedback, please contact me at [satvalite@gmail.com](mailto:satvalite@gmail.com).
