# Credit Memo Tool

A **Streamlit** web app that generates professional credit memos for loan applications using **OpenAI GPT**.

---

## Features

- Calculates **risk level** and **risk score** based on:
  - Annual revenue
  - Loan amount
  - Years in business
  - Existing debt
- Generates a professional **Credit Memo**, including:
  - Client overview
  - Financial summary
  - Risk assessment
  - Recommendation

---

## Prerequisites

- Python 3.9 or higher  
- OpenAI API key  

---

## Setup Instructions

1. **Clone the repository**

bash
git clone <repository_link>
cd <repository_folder>

2. **Create and activate a virtual environment**

python -m venv venv

Windows:venv\Scripts\activate

Mac/Linux:source venv/bin/activate

3. **Install dependencies**

pip install -r requirements.txt

4. **Create a .env file in the project root:**

Create a .env file in the project root:

5. **Run the application**

streamlit run main.py
