
import streamlit as st
import requests
import os
import time
from PIL import Image

st.set_page_config(page_title="Issuet Hiring Assistant", layout="centered")

# ✅ Backend URL (Deployed on Render)
BACKEND_URL = "https://issuet-3dxf.onrender.com/api/candidates/"

# 🖤 Improved Visibility Theme
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background: linear-gradient(120deg, #f3f6ff 0%, #eef2f9 100%);
        font-family: 'Poppins', sans-serif;
        color: #000000 !important;
    }

    .card {
        width: 100%;
        max-width: 560px;
        margin: 20px auto 60px auto;
        background: #ffffff;
        border-radius: 18px;
        padding: 40px 36px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
    }

    label, .stTextInput label, .stTextArea label, .stFileUploader label {
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }

    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        border-radius: 10px !important;
        border: 2px solid #000000 !important;
        padding: 14px !important;
        font-size: 15px !important;
        color: #000000 !important;
        background-color: #ffffff !important;
    }

    .stFileUploader > div {
        border-radius: 10px !important;
        border: 2px dashed #000000 !important;
        padding: 15px !important;
        background: #ffffff !important;
        color: #000000 !important;
    }

    .submit-button > button {
        width: 100%;
        background: linear-gradient(90deg, #2563eb, #1e40af);
        color: white !important;
        border-radius: 10px;
        padding: 12px 0;
        font-size: 16px;
        font-weight: 600;
        border: none;
        transition: all 0.25s ease;
        box-shadow: 0 4px 12px rgba(37,99,235,0.3);
    }
    .submit-button > button:hover {
        background: linear-gradient(90deg, #1e3a8a, #2563eb);
        transform: scale(1.02);
    }

    .heading {
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        color: #000000 !important;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .logo-wrap {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 0px;
    }

    .footer {
        text-align: center;
        color: #000000 !important;
        margin-top: 50px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Logo Section
logo_path_candidates = [
    "issuet_logo.png", "logo.png", "Screenshot (128).png",
    "Screenshot.png", "issuet.png"
]
logo_used = next((p for p in logo_path_candidates if os.path.exists(p)), None)

st.markdown('<div class="logo-wrap">', unsafe_allow_html=True)
if logo_used:
    st.image(Image.open(logo_used), width=760)
else:
    st.markdown("<h2 style='text-align:center;color:#000000;'>Issuet</h2>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Heading
st.markdown("<div class='heading'> ISSUET IS HIRING - Fill the form</div>", unsafe_allow_html=True)

# Candidate form
with st.form("candidate_form"):
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.text_input("Experience (in years)")
    position = st.text_input("Position Applied For")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Technical Skills (e.g., Python, Django, React)")
    resume = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])
    submitted = st.form_submit_button("Submit", use_container_width=True)

# Validation
def valid_email(email):
    import re
    return re.match(r"^[^@]+@[^@]+\.[^@]+$", email)

if submitted:
    if not all([full_name.strip(), email.strip(), phone.strip(), position.strip(), resume]):
        st.warning("⚠️ Please fill all required fields and upload your resume.")
    elif not valid_email(email):
        st.warning("📧 Please enter a valid email address.")
    else:
        with st.spinner("Uploading your application... ⏳"):
            time.sleep(1)
            try:
                files = {"resume": (resume.name, resume.getvalue(), resume.type)}
                data = {
                    "full_name": full_name,
                    "email": email,
                    "phone": phone,
                    "experience": experience,
                    "position": position,
                    "location": location,
                    "tech_stack": tech_stack,
                }
                response = requests.post(BACKEND_URL, data=data, files=files, timeout=15)
                if response.status_code in (200, 201):
                    st.success("✅ Application submitted successfully! Thank you for applying.")
                else:
                    st.error(f"⚠️ Submission failed (HTTP {response.status_code})")
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Could not reach backend: {e}")

# Footer
st.markdown("<div class='footer'>© 2025 Issuet - Solution Based Company</div>", unsafe_allow_html=True)
import streamlit as st
import requests
import os
import time
from PIL import Image

st.set_page_config(page_title="Issuet Hiring Assistant", layout="centered")

# ✅ Backend URL (Deployed on Render)
BACKEND_URL = "https://issuet-3dxf.onrender.com/api/candidates/"

# 🖤 Improved Visibility Theme
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background: linear-gradient(120deg, #f3f6ff 0%, #eef2f9 100%);
        font-family: 'Poppins', sans-serif;
        color: #000000 !important;
    }

    .card {
        width: 100%;
        max-width: 560px;
        margin: 20px auto 60px auto;
        background: #ffffff;
        border-radius: 18px;
        padding: 40px 36px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
    }

    label, .stTextInput label, .stTextArea label, .stFileUploader label {
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }

    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        border-radius: 10px !important;
        border: 2px solid #000000 !important;
        padding: 14px !important;
        font-size: 15px !important;
        color: #000000 !important;
        background-color: #ffffff !important;
    }

    .stFileUploader > div {
        border-radius: 10px !important;
        border: 2px dashed #000000 !important;
        padding: 15px !important;
        background: #ffffff !important;
        color: #000000 !important;
    }

    .submit-button > button {
        width: 100%;
        background: linear-gradient(90deg, #2563eb, #1e40af);
        color: white !important;
        border-radius: 10px;
        padding: 12px 0;
        font-size: 16px;
        font-weight: 600;
        border: none;
        transition: all 0.25s ease;
        box-shadow: 0 4px 12px rgba(37,99,235,0.3);
    }
    .submit-button > button:hover {
        background: linear-gradient(90deg, #1e3a8a, #2563eb);
        transform: scale(1.02);
    }

    .heading {
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        color: #000000 !important;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .logo-wrap {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 0px;
    }

    .footer {
        text-align: center;
        color: #000000 !important;
        margin-top: 50px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Logo Section
logo_path_candidates = [
    "issuet_logo.png", "logo.png", "Screenshot (128).png",
    "Screenshot.png", "issuet.png"
]
logo_used = next((p for p in logo_path_candidates if os.path.exists(p)), None)

st.markdown('<div class="logo-wrap">', unsafe_allow_html=True)
if logo_used:
    st.image(Image.open(logo_used), width=760)
else:
    st.markdown("<h2 style='text-align:center;color:#000000;'>Issuet</h2>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Heading
st.markdown("<div class='heading'> ISSUET IS HIRING - Fill the form</div>", unsafe_allow_html=True)

# Candidate form
with st.form("candidate_form"):
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.text_input("Experience (in years)")
    position = st.text_input("Position Applied For")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Technical Skills (e.g., Python, Django, React)")
    resume = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])
    submitted = st.form_submit_button("Submit", use_container_width=True)

# Validation
def valid_email(email):
    import re
    return re.match(r"^[^@]+@[^@]+\.[^@]+$", email)

if submitted:
    if not all([full_name.strip(), email.strip(), phone.strip(), position.strip(), resume]):
        st.warning("⚠️ Please fill all required fields and upload your resume.")
    elif not valid_email(email):
        st.warning("📧 Please enter a valid email address.")
    else:
        with st.spinner("Uploading your application... ⏳"):
            time.sleep(1)
            try:
                files = {"resume": (resume.name, resume.getvalue(), resume.type)}
                data = {
                    "full_name": full_name,
                    "email": email,
                    "phone": phone,
                    "experience": experience,
                    "position": position,
                    "location": location,
                    "tech_stack": tech_stack,
                }
                response = requests.post(BACKEND_URL, data=data, files=files, timeout=15)
                if response.status_code in (200, 201):
                    st.success("✅ Application submitted successfully! Thank you for applying.")
                else:
                    st.error(f"⚠️ Submission failed (HTTP {response.status_code})")
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Could not reach backend: {e}")

# Footer
st.markdown("<div class='footer'>© 2025 Issuet - Solution Based Company</div>", unsafe_allow_html=True)
