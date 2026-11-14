# CyberGuard AI – AI Development Prompt Log

**Developer:** Arlette Torres  
**Project:** CyberGuard AI  
**Course:** COSC 4272 – Senior Seminar

## 1. Project Planning

**Prompt:**

"Help me develop a beginner-friendly AI-powered cybersecurity assistant that can analyze security alerts, identify potential threats, and provide investigation recommendations."

**Purpose:**

Used AI assistance to brainstorm the project concept, define its features, and establish an appropriate scope for a student cybersecurity portfolio project.

## 2. Application Development

**Prompt:**

"Help me build a Python application using Streamlit that accepts cybersecurity alerts and analyzes them using an AI model."

**Purpose:**

Used AI assistance to develop the application's structure, user input functionality, and integration with a generative AI service.

## 3. AI Integration

**Prompt:**

"Help me integrate Google's Gemini API into my Python cybersecurity assistant so it can analyze submitted security alerts and generate structured responses."

**Purpose:**

Used AI assistance to understand API integration, configure the Google GenAI Python SDK, and generate cybersecurity analysis results.

## 4. Interface Design

**Prompt:**

"Help me create a professional dark-blue cybersecurity dashboard with sample security alerts, an alert input area, analysis results, and severity indicators."

**Purpose:**

Used AI assistance to improve the application's visual presentation and make its features easier to navigate.

## 5. Response Quality and Safety

**Prompt:**

"Improve the AI analysis instructions so the assistant distinguishes suspected threats from confirmed incidents, avoids inventing evidence, explains uncertainty, and provides beginner-friendly investigation recommendations."

**Purpose:**

Used AI assistance to refine the analysis instructions and encourage more responsible cybersecurity assessments.

## 6. Testing and Troubleshooting

**Prompt:**

"Help me troubleshoot Gemini API errors and improve the reliability of my Streamlit application."

**Purpose:**

Used AI assistance to investigate API availability and timeout errors and adjust the model configuration.

## 7. Application Testing and Results

CyberGuard AI was tested using three sample cybersecurity scenarios to evaluate its ability to identify different types of activity and assign appropriate severity levels.

| Test scenario | Detected severity | Result |
|---|---|---|
| Repeated failed administrator logins followed by a successful login and sensitive file access | High | Identified suspected brute-force activity and possible credential compromise |
| Normal employee login from a familiar company device during business hours | Low | Recognized the activity as normal and did not identify a confirmed threat |
| Suspicious email impersonating the IT department with an unfamiliar password-reset link | Medium | Identified suspected phishing and credential harvesting |

The application generated structured explanations, relevant MITRE ATT&CK technique mappings, investigation recommendations, and additional information needed for each scenario.

These tests demonstrated that the application could distinguish between different types of security events. However, the results are AI-generated assessments and are not proof that an attack occurred or that a system is secure.

## 8. Human Review and Development

AI-generated suggestions were reviewed and tested during development. I made decisions about the application's appearance, functionality, sample alerts, and final implementation.

I reviewed the generated results for accuracy, relevance, severity classification, and appropriate cybersecurity recommendations. I also identified areas where the AI could make unsupported assumptions or assign a technique without sufficient evidence.

## 9. Reflection

Using AI assistance helped me explore generative AI integration, Python application development, API configuration, and cybersecurity alert analysis. I learned that AI-generated results must be evaluated carefully because they can contain inaccurate assumptions or incomplete information.

Testing CyberGuard AI with different security scenarios helped me understand how severity levels and threat classifications can vary depending on the available evidence. It also reinforced the importance of human oversight when interpreting AI-generated cybersecurity assessments.

CyberGuard AI is an educational prototype, not a replacement for professional security monitoring or incident response. Its results should always be verified using actual security logs, supporting evidence, and professional judgment.