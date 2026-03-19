import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# --- Load environment variables from .env file ---
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # API key is stored in .env for security
client = OpenAI(api_key=api_key)

# --- Page Title (centered) ---
st.markdown("<h1 style='text-align: center;'>Credit Memo Tool</h1>", unsafe_allow_html=True)

# --- User Input Form ---
company = st.text_input("Company name")

revenue = st.number_input(
    "Annual revenue (EUR)",
    min_value=0.0,
    max_value=100_000_000.0,
    value=100_000.0,
    step=1000.0
)

loan_amount = st.number_input(
    "Loan amount (EUR)",
    min_value=0.0,
    max_value=50_000_000.0,
    value=10_000.0,
    step=1000.0
)

years_in_business = st.number_input(
    "Years in business",
    min_value=0.01,   # Minimum 0.01 years (~3.5 days)
    max_value=100.0,
    value=1.0,
    step=0.1
)

existing_debt = st.selectbox("Existing debt level", ["Low", "Medium", "High"])

# --- Risk Calculation Function ---
def calculate_risk(revenue, loan_amount, years, debt):
    """
    Calculates the risk level and numeric score for a loan application.
    Factors:
    - Loan amount vs revenue
    - Years in business
    - Existing debt
    - Old, low-revenue business gets additional risk
    """
    if revenue <= 0 or years <= 0:
        return "High", 200  # Hard stop if invalid input

    score = 0
    ratio = loan_amount / revenue

    # Loan vs Revenue
    if ratio < 0.25:
        score += 10
    elif ratio < 0.5:
        score += 30
    else:
        score += 60

    # Years in Business
    if years > 5:
        score += 10
    elif years > 2:
        score += 30
    else:
        score += 50

    # Existing debt
    if debt == "Low":
        score += 10
    elif debt == "Medium":
        score += 35
    else:
        score += 60

    # Additional risk for old low-revenue businesses
    if years > 20 and revenue < 50_000:
        score += 20

    # Classify risk
    if score <= 40:
        return "Low", score
    elif score <= 90:
        return "Medium", score
    else:
        return "High", score

# --- Button: Generate Credit Memo ---
if st.button("Generate Credit Memo"):

    # --- Input validation ---
    if not company.strip():
        st.error("Please enter a company name.")
    elif revenue <= 0:
        st.error("Annual revenue must be greater than 0.")
    elif loan_amount <= 0:
        st.error("Loan amount must be greater than 0.")
    elif years_in_business < 0.01:
        st.error("Years in business must be greater than 0.")
    else:
        # --- Calculate risk ---
        risk_level, risk_score = calculate_risk(
            revenue, loan_amount, years_in_business, existing_debt
        )

        st.write(f"Calculated Risk Level: **{risk_level}**")
        st.write(f"Risk Score: {risk_score}")

        # --- Prepare prompt for OpenAI GPT ---
        prompt_text = f"""
        You are a senior credit analyst.

        Create a professional credit memo including:
        - Client overview
        - Financial summary
        - Risk assessment
        - Recommendation

        Company: {company}
        Revenue: EUR{revenue}
        Loan Amount: EUR{loan_amount}
        Years in Business: {years_in_business}
        Existing Debt: {existing_debt}

        Calculated Risk Level: {risk_level}
        Risk Score: {risk_score}
        """

        # Ensure prompt is Unicode-safe
        prompt_text = str(prompt_text)

        try:
            response = client.chat.completions.create(
                model="gpt-4.1",
                messages=[{"role": "user", "content": prompt_text}]
            )

            memo = response.choices[0].message.content

            st.subheader("Generated Credit Memo")
            st.write(memo)

        except Exception as e:
            st.error(f"Error generating memo: {e}")