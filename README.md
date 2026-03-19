# Credit Memo Tool

This is a Streamlit web application that generates professional credit memos for loan applications using OpenAI GPT.

---

## Features

- Calculate **risk level** and **risk score** based on:
  - Annual revenue
  - Loan amount
  - Years in business
  - Existing debt
- Generate a **Credit Memo** including:
  - Client overview
  - Financial summary
  - Risk assessment
  - Recommendation

---

## Prerequisites

- Python 3.9+ installed
- OpenAI API key

---

## Setup Instructions

1. **Clone the repository:**

bash

git clone <repository_link>
cd <repository_folder>

2 .Create a virtual environment (recommended):

python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # Mac/Linux

3.Install dependencies:

pip install -r requirements.txt

4. Create a .env file in the project root:

OPENAI_API_KEY=sk-your_openai_api_key_here

Do not commit .env to GitHub. Each user should use their own API key.

5.Run the application:

streamlit run main.py

6.Open the browser when Streamlit provides a local URL
