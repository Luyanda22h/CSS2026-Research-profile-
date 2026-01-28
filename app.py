import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Luyanda Mshengu | CV",
    page_icon="📄",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    body {
        background-color: #f7f9fc;
    }

    .main {
        padding: 2rem;
    }

    h1, h2, h3 {
        color: #1f2933;
    }

    p, li {
        font-size: 16px;
        line-height: 1.6;
    }

    .section-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    }

    .sidebar-title {
        font-size: 22px;
        font-weight: bold;
    }

    .sidebar-subtitle {
        font-size: 14px;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("<div class='sidebar-title'>Luyanda Mshengu</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-subtitle'>BSc Mathematical Sciences</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Profile",
        "Education",
        "Experience",
        "Skills",
        "Interests"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("📧 emgeeluyanda@gmail.com")
st.sidebar.write("📞 066 598 7514")

# -------- PROFILE --------
if menu == "Profile":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("Profile")
    st.write(
        """
        Final-year **BSc Mathematical Sciences** student majoring in **Mathematics, Statistics, and Computer Science**.
        Strong analytical thinker with a passion for problem-solving and data-driven decision-making.
        Seeking opportunities to gain practical experience and contribute meaningfully in quantitative and
        computational environments.
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

# -------- EDUCATION --------
elif menu == "Education":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("Education")

    st.subheader("Bachelor of Science in Mathematical Sciences")
    st.write("Sefako Makgatho Health Sciences University | 2023 – 2025")
    st.write("Majors: Mathematics, Statistics, Computer Science")

    st.write("")

    st.subheader("National Senior Certificate (NSC)")
    st.write("Matomela High School | 2021")
    st.markdown("</div>", unsafe_allow_html=True)

# -------- EXPERIENCE --------
elif menu == "Experience":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("Work Experience")

    st.subheader("Mathematical, Statistical & Computer Sciences Mentor")
    st.write("SMU | Jan 2023 – Dec 2023")
    st.markdown(
        """
        - Monitored student academic progress  
        - Provided academic and emotional support  
        - Assisted first-year students with university transition  
        - Maintained confidential academic records  
        - Participated in weekly mentoring meetings  
        """
    )

    st.subheader("BSc Mathematical Sciences Group Tutor")
    st.write("SMU | Jan 2024 – Jul 2024")
    st.markdown(
        """
        - Tutored Mathematics and Statistics  
        - Marked assessments accurately and on time  
        - Invigilated Statistics tests and exams  
        - Compiled student intake registers  
        """
    )

    st.subheader("QuantifyYourFuture (QYF) Intern")
    st.write("Virtual Internship | Jan 2025 – Feb 2025")
    st.markdown(
        """
        - Cleaned and analyzed large datasets under tight deadlines  
        - Built and validated data models  
        - Automated EDA using Python  
        - Worked with Pandas, NumPy, Matplotlib, Scikit-Learn  
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

# -------- SKILLS --------
elif menu == "Skills":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Technical Skills")
        st.markdown(
            """
            - Python (Basic)  
            - Pandas, NumPy, Matplotlib, Scikit-Learn  
            - Microsoft Excel (Intermediate)  
            - Microsoft Word (Intermediate)  
            - Power BI (Basic)  
            """
        )

    with col2:
        st.subheader("Transferable Skills")
        st.markdown(
            """
            - Analytical problem-solving  
            - Clear communication of insights  
            - Mentoring & peer support  
            - Time management under pressure  
            - Growth mindset  
            """
        )
    st.markdown("</div>", unsafe_allow_html=True)

# -------- INTERESTS --------
elif menu == "Interests":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("Interests & Hobbies")
    st.markdown(
        """
        - Learning languages  
        - Web design  
        - Reading and writing  
        - Fitness & working out  
        - Chess and sports  
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)
