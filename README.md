# Real-Time Facial Recognition for Attendance Management

## Overview
This project implements a real-time facial recognition system for attendance management using Python, Dlib, and PostgreSQL. It detects and identifies faces accurately using deep learning techniques and ResNet-based embeddings.

## Getting Started
### Prerequisites
Ensure you have the following installed:
- Python (>=3.6)
- PostgreSQL
- Virtual Environment (venv)
- Git

### Installation Guide
1. **Clone the repository:**

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Set up the database:**
   - Start PostgreSQL and create a database:
     ```sql
     CREATE DATABASE facial_recognition;
     ```
   - Update `settings.py` with database credentials.

6. **Run database migrations:**
   ```sh
   python manage.py migrate
   ```

7. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

## Running the Project
1. Connect a webcam to the system.
2. Access the web portal at `http://127.0.0.1:8000/`.
3. Register users and enroll them in courses.
4. Start real-time attendance recording using facial recognition.

## Limitations
- Requires a high-performance GPU for real-time processing.
- Sensitive to lighting conditions and occlusions (e.g., masks, hats, or glasses).
- Facial expressions and mood variations may affect accuracy.

## Acknowledgments
Special thanks to the open-source contributors of Dlib and PostgreSQL communities.
