import streamlit as st
import requests
import time
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Texas State Employee Salary Estimator",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Government-Style CSS
st.markdown("""
    <style>
    /* Import Professional Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Merriweather:wght@700&display=swap');
    
    /* Main Background - Professional Government Blue */
    .stApp {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 50%, #2563eb 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Subtle Pattern Overlay */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            repeating-linear-gradient(45deg, transparent, transparent 35px, rgba(255,255,255,.03) 35px, rgba(255,255,255,.03) 70px);
        pointer-events: none;
        z-index: 0;
    }
    
    /* Main Container - Clean White Card */
    .main > div {
        background: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.2);
        position: relative;
        z-index: 1;
    }
    
    /* Professional Header with Texas/Government Colors */
    .gov-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
        padding: 2.5rem 2rem;
        border-radius: 12px 12px 0 0;
        margin: -2rem -2rem 2rem -2rem;
        border-bottom: 4px solid #dc2626;
        position: relative;
        overflow: hidden;
    }
    
    .gov-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #dc2626 0%, #ffffff 50%, #1e40af 100%);
    }
    
    /* Texas Flag Colors Accent */
    .texas-accent {
        display: flex;
        gap: 0;
        height: 6px;
        margin-bottom: 1.5rem;
    }
    
    .texas-accent > div:nth-child(1) {
        flex: 1;
        background: #002868;
    }
    
    .texas-accent > div:nth-child(2) {
        flex: 1;
        background: #bf0a30;
    }
    
    .texas-accent > div:nth-child(3) {
        flex: 1;
        background: #ffffff;
    }
    
    /* Title Styling - WHITE HEADER TEXT */
    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 800;
        color: #ffffff !important;  /* FORCE WHITE */
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        letter-spacing: -0.02em;
        font-family: 'Merriweather', serif;
    }
    
    .subtitle {
        text-align: center;
        color: #ffffff !important;  /* FORCE WHITE */
        font-size: 1.1rem;
        margin-top: 0.75rem;
        font-weight: 400;
        letter-spacing: 0.02em;
    }
    
    .official-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 0.5rem 1.5rem;
        border-radius: 50px;
        color: white;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Input Fields - Professional Style - WIDER FIELDS */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select {
        background: #f8fafc !important;
        border: 2px solid #cbd5e1;
        border-radius: 8px;
        padding: 14px 18px;  /* Increased padding for larger fields */
        font-size: 16px;     /* Larger font size */
        transition: all 0.3s ease;
        color: #1e293b !important;
        font-weight: 500;
        min-height: 55px;    /* Minimum height for larger fields */
    }
    
    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #1e40af;
        box-shadow: 0 0 0 3px rgba(30, 64, 175, 0.1);
        outline: none;
        background: #ffffff !important;
    }
    
    /* Labels - DARKER BLACK and BOLDER */
    .stTextInput > label,
    .stSelectbox > label,
    .stRadio > label,
    .stMarkdown h3 {
        font-weight: 800 !important;  /* Bolder */
        color: #000000 !important;    /* PURE BLACK */
        font-size: 1.1rem !important; /* Larger */
        margin-bottom: 0.75rem !important;
        display: block !important;
        letter-spacing: 0.01em;
        text-transform: uppercase;
    }
    
    /* Section Headers - DARKER BLACK */
    .section-title {
        font-size: 1.6rem;  /* Larger */
        font-weight: 800;   /* Bolder */
        color: #000000 !important;  /* PURE BLACK */
        margin: 2rem 0 1.5rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 4px solid #1e40af;  /* Thicker border */
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Primary Button - Government Blue */
    .stButton > button {
        background: linear-gradient(135deg, #1e40af 0%, #2563eb 100%) !important;
        color: white !important;
        font-size: 1.2rem;  /* Larger */
        font-weight: 800;   /* Bolder */
        padding: 1.2rem 2.5rem;  /* Larger padding */
        border: none;
        border-radius: 10px;  /* Slightly larger radius */
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.05em;
        border: 2px solid transparent;
        min-height: 65px;  /* Minimum height for larger button */
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(30, 64, 175, 0.4);
        border: 2px solid #60a5fa;
    }
    
    /* Success Icon */
    .success-icon {
        font-size: 5rem;  /* Larger */
        text-align: center;
        margin-bottom: 1.5rem;
        animation: bounceIn 0.8s ease;
    }
    
    @keyframes bounceIn {
        0% { transform: scale(0); opacity: 0; }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); opacity: 1; }
    }
    
    /* Salary Display - GREEN Money Color */
    .salary-amount {
        font-size: 4rem;  /* Larger */
        font-weight: 900; /* Bolder */
        text-align: center;
        color: #00aa00;   /* CHANGED TO GREEN */
        margin: 1.5rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        font-family: 'Inter', sans-serif;
    }
    
    .result-label {
        text-align: center;
        color: #000000 !important;  /* BLACK */
        font-size: 1.2rem;  /* Larger */
        margin-bottom: 2.5rem;
        font-weight: 700;   /* Bolder */
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    /* Info Cards - Professional Government Style */
    .info-card {
        background: linear-gradient(135deg, #1e40af 0%, #2563eb 100%);
        color: white;
        padding: 2rem;  /* More padding */
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.25);
        border: 1px solid rgba(255,255,255,0.2);
        transition: transform 0.3s ease;
        min-height: 140px;  /* Minimum height */
    }
    
    .info-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(30, 64, 175, 0.35);
    }
    
    .info-card h3 {
        margin: 0 0 0.75rem 0;
        font-size: 1.4rem;  /* Larger */
        color: white !important;
        font-weight: 800;   /* Bolder */
    }
    
    .info-card p {
        margin: 0;
        opacity: 0.95;
        color: white !important;
        font-size: 1.5rem;  /* Larger */
        font-weight: 800;   /* Bolder */
    }
    
    /* Sidebar - Government Professional */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%) !important;
        border-right: 3px solid #1e40af;
    }
    
    section[data-testid="stSidebar"] > div {
        background: transparent !important;
    }
    
    /* Sidebar Headers - DARKER */
    section[data-testid="stSidebar"] h3 {
        color: #000000 !important;  /* BLACK */
        font-weight: 800;
        border-bottom: 2px solid #1e40af;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
        font-size: 1.3rem;  /* Larger */
    }
    
    /* Progress Bar - Texas Colors */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #1e40af 0%, #dc2626 100%);
    }
    
    /* Alert Boxes */
    .stSuccess {
        background: #dcfce7;
        border-left: 4px solid #16a34a;
        color: #166534 !important;
    }
    
    .stError {
        background: #fee2e2;
        border-left: 4px solid #dc2626;
        color: #991b1b !important;
    }
    
    .stWarning {
        background: #fef3c7;
        border-left: 4px solid #f59e0b;
        color: #92400e !important;
    }
    
    .stInfo {
        background: #dbeafe;
        border-left: 4px solid #2563eb;
        color: #1e40af !important;
    }
    
    /* Markdown Text Visibility - DARKER */
    .stMarkdown {
        color: #000000 !important;  /* BLACK */
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;  /* BLACK */
        font-weight: 800;  /* Bolder */
    }
    
    p, li, strong {
        color: #000000 !important;  /* BLACK */
        font-weight: 600;
    }
    
    /* Official Government Badge */
    .gov-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: #eff6ff;
        border: 2px solid #2563eb;
        color: #1e40af;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        font-weight: 800;  /* Bolder */
        font-size: 0.9rem;  /* Larger */
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Confidence Badge */
    .confidence-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: #fef3c7;
        border: 2px solid #f59e0b;
        color: #92400e;
        padding: 1rem 2rem;  /* Larger */
        border-radius: 8px;
        font-weight: 800;  /* Bolder */
        font-size: 1.1rem;  /* Larger */
        margin: 1.5rem 0;
    }
    
    /* Loading Spinner */
    .stSpinner > div {
        border-top-color: #1e40af !important;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .salary-amount {
            font-size: 2.5rem;
        }
        
        .gov-header {
            padding: 1.5rem 1rem;
        }
    }
    
    /* Force all text in main content to be black */
    .main-container * {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# API Configuration - Use the correct field names
API_URL = "http://127.0.0.1:8000/predict"

# Professional Government Header - WHITE TEXT
st.markdown("""
    <div class="gov-header">
        <div class="texas-accent">
            <div></div>
            <div></div>
            <div></div>
        </div>
        <h1 class="main-title">🏛️ Texas State Employee Salary Estimator</h1>
        <p class="subtitle">Official Predictive Analytics System for Government Compensation</p>
        <div style="text-align: center;">
            <span class="official-badge">
                <span>⚡</span> Powered by Advanced AI • 149K+ Records • 72% Accuracy
            </span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Sidebar - Government Professional
with st.sidebar:
    st.markdown("### 🏛️ System Information")
    st.markdown("""
    This official salary estimation system uses advanced machine learning 
    algorithms to predict monthly compensation for Texas state employees.
    
    **Data Sources:**
    - 🏢 Texas State Agencies
    - 💼 Civil Service Classifications
    - 👤 Employment Demographics
    - ⏰ Status & Schedule Data
    
    **Model Accuracy:** 72% (R² = 0.722)
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Database Statistics")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Records", "149,481", "employees")
        st.metric("Job Titles", "1,842", "unique")
    with col2:
        st.metric("Agencies", "109", "covered")
        st.metric("Features", "5", "inputs")
    
    st.markdown("---")
    st.markdown("### 📋 Instructions")
    st.markdown("""
    1. **Enter** employee information
    2. **Click** 'Generate Prediction'
    3. **Review** estimation results
    4. **Download** report (optional)
    """)
    
    st.markdown("---")
    st.markdown("### ⚖️ Disclaimer")
    st.markdown("""
    <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; border-left: 4px solid #f59e0b;">
        <strong style="color: #92400e;">Official Use Only</strong><br>
        <span style="color: #78350f; font-size: 0.85rem;">
        Predictions are estimates based on historical data. 
        Actual salaries may vary based on budget, policy, and individual qualifications.
        </span>
    </div>
    """, unsafe_allow_html=True)

# Main Form Section - DARKER BLACK TITLES
st.markdown('<p class="section-title">📝 Employee Information Form</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**🏢 Organization Details**")
    
    agency_name = st.text_input(
        "AGENCY NAME",
        value="TEXAS DEPARTMENT OF CRIMINAL JUSTICE",
        placeholder="Enter official agency name",
        help="Enter the complete name of the Texas state agency"
    )
    
    class_title = st.text_input(
        "JOB CLASSIFICATION", 
        value="CORREC OFFICER IV",
        placeholder="Enter job title or classification",
        help="Enter the official job title or classification code"
    )
    
    ethnicity = st.selectbox(
        "ETHNICITY",
        options=["WHITE", "BLACK", "HISPANIC", "OTHER"],
        help="Select employee ethnicity category"
    )

with col2:
    st.markdown("**👤 Employee Demographics**")
    gender = st.selectbox(
        "GENDER",
        options=["MALE", "FEMALE"],
        help="Select employee gender"
    )
    
    status = st.selectbox(
        "EMPLOYMENT STATUS",
        options=["FULL-TIME", "PART-TIME"],
        help="Select employment classification"
    )

st.markdown("<br>", unsafe_allow_html=True)

# Action Button - LARGER
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🔮 GENERATE SALARY PREDICTION", use_container_width=True)

# Prediction Logic
if predict_button:
    # Validation
    if not agency_name.strip() or not class_title.strip():
        st.error("⚠️ **Validation Error:** All fields are required. Please complete the form.")
    else:
        # Loading State
        with st.spinner('🔄 Processing data and generating prediction...'):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.015)
                progress_bar.progress(i + 1)
            
            # Use the CORRECT field names that match your FastAPI schema
            input_data = {
                "AGENCY_NAME": agency_name.strip().upper(),
                "CLASS_TITLE": class_title.strip().upper(),
                "ETHNICITY": ethnicity.upper(),
                "GENDER": gender.upper(),
                "STATUS": status.upper()
            }
            
            try:
                # Show what we're sending
                with st.expander("🔍 Debug: Request Details", expanded=True):
                    st.write("**Sending this data to API:**")
                    st.json(input_data)
                    st.write(f"**API URL:** {API_URL}")
                
                response = requests.post(API_URL, json=input_data, timeout=15)
                
                # Show response details
                with st.expander("🔍 Debug: Response Details", expanded=True):
                    st.write(f"**Response Status Code:** {response.status_code}")
                    st.write(f"**Response Headers:** {dict(response.headers)}")
                    
                    try:
                        response_json = response.json()
                        st.write("**Response JSON:**")
                        st.json(response_json)
                    except:
                        st.write(f"**Response Text (raw):** {response.text}")
                
                if response.status_code == 200:
                    # Try multiple possible response formats
                    response_data = response.json()
                    
                    # DEBUG: Show all keys in response
                    st.info(f"📋 Response keys: {list(response_data.keys())}")
                    
                    # Try different possible keys for salary
                    estimated_salary = None
                    possible_keys = [
                        'estimated_salary', 
                        'Estimated_salary',
                        'salary',
                        'prediction',
                        'result',
                        'value'
                    ]
                    
                    for key in possible_keys:
                        if key in response_data:
                            estimated_salary = response_data[key]
                            st.success(f"✅ Found salary using key: '{key}' = ${estimated_salary:,.2f}")
                            break
                    
                    # If no key found, try to extract first numeric value
                    if estimated_salary is None:
                        st.warning("🔍 No standard salary key found. Searching for numeric values...")
                        for key, value in response_data.items():
                            if isinstance(value, (int, float)) and value > 0:
                                estimated_salary = value
                                st.success(f"✅ Found numeric value at key: '{key}' = ${estimated_salary:,.2f}")
                                break
                    
                    # If still no salary found, show error
                    if estimated_salary is None:
                        st.error("❌ Could not extract salary from API response")
                        st.info("Please check your FastAPI endpoint response format")
                        # Show the full response for debugging
                        st.write("**Full response for debugging:**")
                        st.json(response_data)
                    else:
                        # Success Animation
                        st.balloons()
                        
                        # Results Display
                        st.markdown("---")
                        
                        # Success Badge
                        col1, col2, col3 = st.columns([1, 2, 1])
                        with col2:
                            st.markdown('<div class="success-icon">✅</div>', unsafe_allow_html=True)
                            st.markdown("""
                            <div style="text-align: center;">
                                <span class="gov-badge">
                                    <span>🏛️</span> OFFICIAL PREDICTION GENERATED
                                </span>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Salary Display - NOW IN GREEN
                        st.markdown(f'<div class="salary-amount">${estimated_salary:,.2f}</div>', unsafe_allow_html=True)
                        st.markdown('<p class="result-label">Estimated Annual Compensation</p>', unsafe_allow_html=True)
                        
                        # Confidence Indicator
                        st.markdown("""
                        <div style="text-align: center;">
                            <span class="confidence-badge">
                                <span>⭐</span> High Confidence Estimate (R² = 0.832)
                            </span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Breakdown Cards
                        st.markdown('<p class="section-title">💰 Compensation Breakdown</p>', unsafe_allow_html=True)
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            monthly_salary = estimated_salary / 12
                            st.markdown(f"""
                            <div class="info-card">
                                <h3>📅 Monthly</h3>
                                <p>${monthly_salary:,.2f}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col2:
                            weekly_salary = estimated_salary / 52
                            st.markdown(f"""
                            <div class="info-card">
                                <h3>📊 Weekly</h3>
                                <p>${weekly_salary:,.2f}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col3:
                            hourly_salary = estimated_salary / 2080
                            st.markdown(f"""
                            <div class="info-card">
                                <h3>💵 Hourly</h3>
                                <p>${hourly_salary:,.2f}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Prediction Details
                        st.markdown('<p class="section-title">📋 Prediction Record</p>', unsafe_allow_html=True)
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.markdown(f"""
                            **🏢 Agency:** {agency_name}  
                            **💼 Job Title:** {class_title}  
                            **🌍 Ethnicity:** {ethnicity}
                            """)
                        
                        with col2:
                            st.markdown(f"""
                            **👤 Gender:** {gender}  
                            **⏰ Status:** {status}  
                            **📅 Date:** {datetime.now().strftime("%B %d, %Y")}
                            """)
                        
                        # Action Buttons
                        st.markdown("---")
                        col1, col2, col3 = st.columns(3)
                        
                        with col2:
                            if st.button("🔄 NEW PREDICTION", use_container_width=True):
                                st.rerun()
                
                else:
                    st.error(f"❌ **API Error:** {response.status_code}")
                    st.write(f"**Error details:** {response.text}")
                    st.info("""
                    **Common issues:**
                    1. FastAPI server not running
                    2. Model not loaded in FastAPI
                    3. Incorrect endpoint URL
                    4. Field name mismatches
                    """)
                    
            except requests.exceptions.Timeout:
                st.error("⏱️ **Connection Timeout:** API server not responding.")
                st.info("Make sure your FastAPI server is running: `uvicorn main:application --reload`")
            except requests.exceptions.ConnectionError:
                st.error("🔌 **Connection Failed:** Cannot reach API server at http://127.0.0.1:8000")
                st.info("""
                **Troubleshooting Steps:**
                1. Start FastAPI: `uvicorn main:application --reload --port 8000`
                2. Check if running: Visit http://127.0.0.1:8000/health
                3. Verify endpoint: http://127.0.0.1:8000/predict
                """)
            except Exception as e:
                st.error(f"❌ **Unexpected Error:** {str(e)}")
                st.info("Check the console for detailed error messages")

# Health Check
with st.sidebar:
    st.markdown("---")
    st.markdown("### 🔧 System Status")
    
    try:
        health_response = requests.get("http://127.0.0.1:8000/health", timeout=5)
        if health_response.status_code == 200:
            st.success("✅ API Connected")
        else:
            st.error("❌ API Error")
    except:
        st.error("❌ API Offline")

# Official Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem 0; background: #f8fafc; border-radius: 8px; margin-top: 2rem;">
    <p style="color: #000000 !important; font-weight: 800; margin-bottom: 0.5rem;">
        🏛️ Texas State Employee Salary Estimation System
    </p>
    <p style="color: #000000 !important; font-size: 0.9rem; margin-bottom: 0.5rem;">
        Developed by Pranav Gupta | Powered by Machine Learning & Data Science
    </p>
    <p style="color: #000000 !important; font-size: 0.85rem;">
        © 2024 All Rights Reserved | For Official Government Use
    </p>
</div>
""", unsafe_allow_html=True)