# Chatbot Backend - Sign Language Translator

This project implements a backend API for a chatbot that translates sign language into text using a Flask API and OpenCV for video processing. The project uses various AI tools and libraries to recognize sign language gestures.

## Prerequisites

- Python 3.8 or higher
- Virtual environment tools (`venv`)
- Basic understanding of Flask, OpenCV, and AI libraries

## Setup Instructions

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chatbot-backend.git
cd chatbot-backend
```

### 2. Create and activate virtual environment. Install required dependencies

```bash
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Install Neuspell for using Bert Checker

```bash
cd src
git clone git clone https://github.com/neuspell/neuspell
cd neuspell
pip install -e .
pip install -r extras-requirements.txt
```

### 4. Install Additional files for using Bert Checker

```bash
cd ..
python neuspell_utils.py
```

### 5. Run flask app

```bash
cd ..
python app.py
```