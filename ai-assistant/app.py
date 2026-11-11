
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="centered"
)

# Application title
st.title("🛡️ CyberGuard AI")
st.subheader("AI Cybersecurity Assistant")

st.write(
    "Analyze suspicious activity, understand security alerts, "
    "and learn basic cybersecurity investigation techniques."
)

st.divider()

# Alert input
st.header("Security Alert Analyzer")

alert = st.text_area(
    "Enter a cybersecurity alert:",
    placeholder="Example: Multiple failed login attempts "
                "detected from an unfamiliar IP address.",
    height=150
)

# Analyze button
if st.button("Analyze Security Alert", type="primary"):

    if not alert.strip():
        st.warning("Please enter a security alert first.")

    else:
        alert_lower = alert.lower()

        st.subheader("Analysis Results")

        # Basic rule-based detection
        if any(word in alert_lower for word in
               ["failed login", "brute force", "password attempts"]):

            st.error("Potential Threat: Suspicious Login Activity")

            st.write(
                "Repeated failed login attempts may indicate "
                "a brute-force attack or unauthorized access attempt."
            )

            st.write("Recommended investigation steps:")
            st.write("- Review authentication logs.")
            st.write("- Identify the source IP address.")
            st.write("- Check for successful logins.")
            st.write("- Consider account protection measures.")

        elif any(word in alert_lower for word in
                 ["phishing", "suspicious email", "malicious link"]):

            st.warning("Potential Threat: Phishing Activity")

            st.write(
                "This alert may indicate an attempt to trick "
                "users into revealing sensitive information."
            )

            st.write("Recommended investigation steps:")
            st.write("- Inspect the sender's email address.")
            st.write("- Examine suspicious links safely.")
            st.write("- Check email security logs.")
            st.write("- Report the message to the security team.")

        elif any(word in alert_lower for word in
                 ["malware", "ransomware", "trojan"]):

            st.error("Potential Threat: Malware Activity")

            st.write(
                "This alert may indicate malicious software "
                "or potentially harmful activity."
            )

            st.write("Recommended investigation steps:")
            st.write("- Review endpoint security alerts.")
            st.write("- Identify the affected device.")
            st.write("- Preserve relevant security logs.")
            st.write("- Follow your organization's incident response plan.")

        else:
            st.info("General Security Alert")

            st.write(
                "The alert does not match the application's "
                "current detection rules."
            )

            st.write("Recommended investigation steps:")
            st.write("- Review the original alert.")
            st.write("- Identify affected systems.")
            st.write("- Examine relevant system logs.")
            st.write("- Escalate suspicious findings when necessary.")

        st.caption(
            "Disclaimer: This is a basic educational prototype. "
            "Results are not a substitute for professional security analysis."
        )

st.divider()

st.subheader("About CyberGuard AI")

st.write(
    "CyberGuard AI is a student-developed cybersecurity "
    "assistant designed to demonstrate security alert "
    "analysis and beginner-friendly investigation guidance."
)

st.caption("Developed by Arlette Torres | COSC 4272 Senior Seminar")
