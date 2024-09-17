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

```bash
python -m venv venv

```bash
venv\Scripts\activate

```bash
pip install -r requirements.txt

```bash
cd src/neuspell
pip install -e .
pip install -r extras-requirements.txt

```bash
cd ../..
python app.py