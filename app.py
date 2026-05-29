import streamlit as st
from google import genai
from fpdf import FPDF
import tempfile

# ----------------------------
# API Key
# ----------------------------

try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
except Exception:
    st.error("Please add GOOGLE_API_KEY in Streamlit Secrets.")
    st.stop()

client = genai.Client(api_key=API_KEY)

# ----------------------------
# Page Config
# ----------------------------

st.set_page_config(
    page_title="TravelGuard AI",
    page_icon="✈️",
    layout="wide"
)

# ----------------------------
# Styling
# ----------------------------

st.markdown("""
<style>
.main {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------

st.title("✈️ TravelGuard AI")
st.subheader("Your Real-Time Travel Problem Solver powered by Gemma 4")

st.markdown("""
### Travel Problems We Help With

✅ Flight Delays  
✅ Lost Passport  
✅ Lost Wallet  
✅ Taxi Scams  
✅ Medical Emergencies  
✅ Hotel Issues  
✅ Travel Safety Risks  
✅ Language Barriers
""")

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("Travel Settings")

category = st.sidebar.selectbox(
    "Issue Type",
    [
        "Flight Delay",
        "Lost Passport",
        "Lost Wallet",
        "Taxi Scam",
        "Medical Emergency",
        "Hotel Issue",
        "Travel Safety",
        "Custom Problem"
    ]
)

language = st.sidebar.selectbox(
    "Response Language",
    [
        "English",
        "Hindi",
        "Telugu"
    ]
)

# ----------------------------
# User Input
# ----------------------------

problem = st.text_area(
    "Describe Your Travel Problem",
    height=200,
    placeholder="Example: My passport is lost at Hyderabad Airport and I don't know what to do."
)

# ----------------------------
# Prompt Builder
# ----------------------------

def create_prompt(user_problem, issue_type, language):
    return f"""
You are TravelGuard AI.

A traveler needs help.

Issue Type:
{issue_type}

Problem:
{user_problem}

Provide:

# Immediate Actions

# Safety Tips

# Alternative Options

# Emergency Recommendations

# Important Contacts To Search

# Next Steps

Keep the response practical, concise, and traveler-friendly.

Respond only in {language}.
"""

# ----------------------------
# PDF Generator
# ----------------------------

def create_pdf(content):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=11)

    for line in content.split("\n"):
        try:
            pdf.multi_cell(0, 8, line)
        except:
            pass

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    pdf.output(temp_file.name)

    return temp_file.name

# ----------------------------
# Generate Solution
# ----------------------------

if st.button("🚀 Get Travel Assistance"):

    if not problem.strip():
        st.warning("Please describe your issue.")
    else:

        try:

            with st.spinner("Gemma 4 is analyzing your travel issue..."):

                prompt = create_prompt(
                    problem,
                    category,
                    language
                )

                response = client.models.generate_content(
                    model="gemma-4-26b-a4b-it",
                    contents=prompt
                )

                answer = response.text

            st.success("Travel Guidance Generated")

            st.markdown("## 📋 AI Travel Guidance")

            st.markdown(answer)

            pdf_path = create_pdf(answer)

            with open(pdf_path, "rb") as pdf_file:

                st.download_button(
                    label="📄 Download PDF Report",
                    data=pdf_file,
                    file_name="TravelGuard_Report.pdf",
                    mime="application/pdf"
                )

        except Exception as e:

            st.error(f"Error: {str(e)}")

# ----------------------------
# Footer
# ----------------------------

st.markdown("---")

st.caption(
    "Built with Streamlit + Google AI Studio + Gemma 4"
)