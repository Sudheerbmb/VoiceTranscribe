# Audio Transcription and Summarization Web App

This Flask web application allows users to upload an audio file (M4A format), convert it to WAV, transcribe the audio to text, and then summarize the content using Google's Gemini API. The app also extracts key topics from the transcription.

## Features
- Upload an M4A audio file for transcription.
- Convert M4A files to WAV format.
- Transcribe audio using Whisper.
- Summarize the transcribed text using Google's Gemini API.
- Extract key topics from the transcribed text using Google's Gemini API.
- Download the summary and key topics as text files.

## Technologies Used
- **Flask**: Web framework for the backend.
- **Whisper**: OpenAI's speech-to-text model to transcribe audio.
- **Google Gemini API**: To summarize and extract key topics from the transcription.
- **FFmpeg**: To convert M4A audio files to WAV format.
- **NLTK**: For natural language processing tasks.
- **Werkzeug**: For secure file handling.

## Prerequisites
Before running the application, you need to install the required dependencies. You can do this by setting up a virtual environment and installing the packages.

### Requirements
1. Python 3.7 or higher.
2. Install the required packages by running:
   ```bash
   pip install -r requirements.txt
