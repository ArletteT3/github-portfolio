
import os
import re
import streamlit as st
from google import genai

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="CyberGuard AI | Security Assistant",
    page_icon="🛡️",
    layout="wide"
)

# ==========================================
# CUSTOM DARK BLUE DESIGN
# ==========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #071426, #0d1e36);
    color: #e5edf7;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    max-width: 1150px;
}

h1, h2, h3 {
    color: #f0f6ff !important;
}

p, label, li {
    color: #cbd5e1;
}

.hero {
    background: linear-gradient(120deg, #102b4c, #153e66);
    border: 1px solid #28527c;
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 25px;
}

.hero-title {
    font-size: 34px;
    font-weight: 800;
    color: #ffffff;
}

.hero-subtitle {
    color: #b9cce2;
    font-size: 16px;
    margin-top: 8px;
}

.section-card {
    background: #10233b;
    border: 1px solid #244361;
    border-radius: 14px;
    padding: 22px;
    margin: 12px 0;
}

.metric-card {
    background: #102b46;
    border: 1px solid #28527c;
    border-radius: 12px;
    padding: 18px;
    text-align: center;
}

.metric-title {
    color: #9fb8d3;
    font-size: 13px;
}

.metric-value {
    color: #ffffff;
    font-size: 23px;
    font-weight: bold;
}

.severity {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 20px;
    font-weight: bold;
    margin: 8px 0;
}

.severity-low {
    background: #123e35;
    color: #6ee7b7;
}

.severity-medium {
    background: #493916;
    color: #fcd34d;
}

.severity-high {
    background: #512b18;
    color: #fdba74;
}

.severity-critical {
    background: #511e2a;
    color: #fda4af;
}

.stTextArea textarea {
    background-color: #0b1c30 !important;
    color: #ffffff !important;
    border: 1px solid #355577 !important;
    border-radius: 10px !important;
}

.stTextArea textarea::placeholder {
    color: #ffffff !important;
    opacity: 1 !important;
}

/* BLACK FONT ON BUTTONS */

.stButton button {
    border-radius: 9px;
    font-weight: 600;
    color: #000000 !important;
}

.stButton button p {
    color: #000000 !important;
}

/* PRIMARY BUTTON */

.stButton button[kind="primary"] {
    background: #1976d2;
    border: none;
    color: #ffffff !important;
}

.stButton button[kind="primary"] p {
    color: #ffffff !important;
}

.stButton button[kind="primary"]:hover {
    background: #2689ed;
}

div[data-testid="stAlert"] {
    border-radius: 10px;
}

.footer {
    text-align: center;
    color: #7891ac;
    font-size: 13px;
    padding: 25px 0;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE
# ==========================================

if "alert_input" not in st.session_state:
    st.session_state.alert_input = ""

if "analysis" not in st.session_state:
    st.session_state.analysis = ""

if "severity" not in st.session_state:
    st.session_state.severity = "Unknown"


def load_sample(sample):
    st.session_state.alert_input = sample
    st.session_state.analysis = ""
    st.session_state.severity = "Unknown"


def clear_analysis():
    st.session_state.alert_input = ""
    st.session_state.analysis = ""
    st.session_state.severity = "Unknown"


def extract_severity(text):
    section = re.search(
        r"2\.\s*\**Severity\**\s*:?\s*(.*?)(?=\n\s*(?:###\s*)?3\.|$)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if section:
        match = re.search(
            r"\b(Critical|High|Medium|Low)\b",
            section.group(1),
            re.IGNORECASE
        )

        if match:
            return match.group(1).capitalize()

    return "Unknown"


# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="hero">
    <div class="hero-title">🛡️ CyberGuard AI</div>
    <div class="hero-subtitle">
        AI-Powered Cybersecurity Assistant
        <br>
        Analyze security alerts, identify potential threats,
        and receive investigation guidance.
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# DASHBOARD METRICS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">PLATFORM</div>
        <div class="metric-value">AI Powered</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">ANALYSIS ENGINE</div>
        <div class="metric-value">Gemini</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">PROJECT STATUS</div>
        <div class="metric-value">Operational</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==========================================
# SAMPLE SECURITY ALERTS
# ==========================================

st.subheader("🧪 Sample Security Alerts")
st.write("Choose an example to quickly test the assistant.")

sample1, sample2, sample3 = st.columns(3)

with sample1:
    st.button(
        "🔐 Brute-Force Attack",
        use_container_width=True,
        on_click=load_sample,
        args=("Multiple failed login attempts were detected from IP address 192.168.1.105. The account experienced 25 failed login attempts within 2 minutes, followed by a successful login.",)
    )

with sample2:
    st.button(
        "📧 Phishing Email",
        use_container_width=True,
        on_click=load_sample,
        args=("An employee received an email claiming to be from the company's IT department. The sender address appears slightly different from the official domain. The email requests Microsoft 365 account verification through a link. The employee has not clicked it.",)
    )

with sample3:
    st.button(
        "🦠 Malware Detection",
        use_container_width=True,
        on_click=load_sample,
        args=("An endpoint security tool detected a suspicious executable file on an employee workstation. The file attempted to modify startup registry settings and establish an outbound network connection to an unfamiliar IP address.",)
    )

# ==========================================
# ALERT ANALYZER
# ==========================================

st.divider()

st.subheader("🔍 Security Alert Analyzer")

alert = st.text_area(
    "Enter your security alert:",
    height=180,
    key="alert_input",
    placeholder="Describe the suspicious activity or paste a security alert here..."
)

analyze_col, clear_col = st.columns([3, 1])

with analyze_col:
    analyze_clicked = st.button(
        "🔍 Analyze Security Alert",
        type="primary",
        use_container_width=True
    )

with clear_col:
    st.button(
        "🗑️ Clear",
        use_container_width=True,
        on_click=clear_analysis
    )

# ==========================================
# GEMINI AI ANALYSIS
# ==========================================

if analyze_clicked:

    if not alert.strip():
        st.warning("Please enter a security alert before analyzing.")

    elif not os.getenv("GEMINI_API_KEY"):
        st.error(
            "Gemini API key not found. "
            "Check your Windows environment variable."
        )

    else:

        prompt = f"""
You are CyberGuard AI, a beginner-friendly cybersecurity assistant.

Analyze the following security alert:

{alert}

Organize your response into these sections:

1. Potential Threat
2. Severity (Low, Medium, High, or Critical)
3. Explanation
4. Relevant MITRE ATT&CK Technique, if applicable
5. Three Recommended Investigation Steps
6. Additional Information Needed

Important instructions:
- Explain technical concepts in beginner-friendly language.
- Never invent evidence or assume an attack succeeded.
- Distinguish suspected threats from confirmed incidents.
- Base severity on the evidence provided.
- Explain uncertainty when information is missing.
- Do not recommend destructive actions without proper authorization.
"""

        try:

            with st.spinner("🛡️ CyberGuard AI is analyzing your alert..."):

                client = genai.Client(
                    api_key=os.getenv("GEMINI_API_KEY")
                )

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt,
                    config={
                        "http_options": {
                            "timeout": 120000
                        },
                        "max_output_tokens": 1500
                    }
                )

            if response.text:

                st.session_state.analysis = response.text

                st.session_state.severity = extract_severity(
                    response.text
                )

            else:
                st.warning("Gemini returned an empty response.")

        except Exception as error:

            st.error("Gemini analysis failed.")
            st.error(
                "The AI service may be temporarily unavailable "
                "or the request may have exceeded its time limit."
            )
            st.exception(error)

# ==========================================
# ANALYSIS RESULTS
# ==========================================

if st.session_state.analysis:

    st.divider()
    st.subheader("📊 Analysis Results")

    severity = st.session_state.severity

    severity_class = {
        "Low": "severity-low",
        "Medium": "severity-medium",
        "High": "severity-high",
        "Critical": "severity-critical"
    }.get(severity, "")

    result_col1, result_col2 = st.columns([1, 2])

    with result_col1:

        st.markdown(
            f"""
            <div class="section-card">
                <div class="metric-title">DETECTED SEVERITY</div>
                <div class="severity {severity_class}">
                    {severity}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with result_col2:

        st.markdown("""
        <div class="section-card">
            <div class="metric-title">ANALYSIS ENGINE</div>
            <div class="metric-value">Gemini AI</div>
            <div class="metric-title">
                AI-generated security assessment
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(st.session_state.analysis)

    st.caption(
        "Severity is extracted from the AI-generated assessment. "
        "Always verify findings using actual security logs and evidence."
    )

# ==========================================
# ABOUT AND DISCLAIMER
# ==========================================

st.divider()

with st.expander("About CyberGuard AI"):

    st.write(
        "CyberGuard AI is a student-developed cybersecurity assistant "
        "designed to demonstrate AI-powered security alert analysis "
        "and beginner-friendly investigation guidance."
    )

    st.write(
        "The project uses Python, Streamlit, and Google's Gemini API."
    )

with st.expander("Educational Disclaimer"):

    st.write(
        "CyberGuard AI is an educational prototype. "
        "Its AI-generated results may be inaccurate or incomplete. "
        "It does not replace professional security analysis, "
        "incident response procedures, or human verification."
    )

# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    Developed by Arlette Torres | COSC 4272 Senior Seminar
    <br>
    CyberGuard AI • Educational Cybersecurity Project
</div>
""", unsafe_allow_html=True)
