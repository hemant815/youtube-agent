# 🎥 AI YouTube Video Analyzer

## Overview

AI YouTube Video Analyzer is a Streamlit-based application that analyzes YouTube videos using transcript data and Large Language Models (LLMs). Users can simply provide a YouTube video URL, and the application generates a concise summary, key insights, and important takeaways from the video's content.

The project leverages Groq's Qwen model and Agno's YouTube tools to extract and analyze video transcripts efficiently.

---

## Features

* 🔗 Analyze any YouTube video using its URL
* 📝 Automatic transcript extraction
* 🤖 AI-powered video summarization
* 💡 Key insights and important takeaways
* ⚡ Fast inference using Groq LLMs
* 🎨 Clean and interactive Streamlit interface

---

## Tech Stack

### Frontend

* Streamlit

### AI & NLP

* Groq (Qwen 3 32B)
* Agno Framework
* Large Language Models (LLMs)

### Utilities

* Python
* Python Dotenv

---

## How It Works

1. User enters a YouTube video URL.
2. The application extracts the video's transcript.
3. The transcript is processed by the Groq LLM.
4. The model generates:

   * Summary
   * Key Insights
   * Important Topics
   * Technologies/Tools Mentioned
5. Results are displayed in a structured format.

---

## Project Structure

```text
AI-YouTube-Video-Analyzer/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/hemant815/AI-YouTube-Video-Analyzer.git
cd AI-YouTube-Video-Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

---

## Use Cases

* Educational Content Analysis
* Tutorial Summarization
* Technical Video Insights
* Quick Learning from Long Videos
* Research and Note Taking

---

## Future Improvements

* Multi-language transcript support
* Export summaries to PDF
* Question Answering on Video Content
* Timestamp-based topic extraction
* Video comparison analysis

---

## Learning Outcomes

* LLM Integration
* Prompt Engineering
* Streamlit Development
* API Integration
* NLP Applications
* AI-Powered Content Analysis

---

## Author

**Hemant Patidar**

B.Tech CSE (Artificial Intelligence)

Passionate about Artificial Intelligence, Machine Learning, NLP, Computer Vision, and Generative AI.
