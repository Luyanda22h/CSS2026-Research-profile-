import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Luyanda Mshengu | CV",
    page_icon="📄",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("Luyanda Samkelo Mshengu")
st.subheader("BSc Mathematical Sciences Student")

st.write(
    """
📍 Sefako Makgatho Health Sciences University  
📧 **emgeeluyanda@gmail.com**  
📞 **066 598 7514**
"""
)

st.markdown("---")

# ---------------- PROFILE ----------------
st.header("Profile")

st.write(
    """
Final-year **BSc Mathematical Sciences** student majoring in **Mathematics, Statistics, and Computer Science**.
Highly motivated and analytical, with strong problem-solving skills and a keen interest in applying
quantitative and computational techniques to real-world problems.
Eager to gain practical experience, grow professionally, and contribute meaningfully in data-driven environments.
"""
)

# ---------------- EDUCATION ----------------
st.header("Education")

st.write("**Bachelor of Science in Mathematical Sciences**")
st.write("Sefako Makgatho Health Sciences University | 2023 – 2025")
st.write("Majors: Mathematics, Statistics, Computer Science")

st.write("")
st.write("**National Senior Certificate (NSC)**")
st.write("Matomela High School | 2021")

# ---------------- EXPERIENCE ----------------
st.header("Work Experience")

st.subheader("Mathematical, Statistical & Computer Sciences Mentor")
st.write("Sefako Makgatho Health Sciences University | Jan 2023 – Dec 2023")

st.markdown(
    """
- Monitored and assessed students’ academic progress  
- Provided academic and emotional support to fellow students  
- Assisted first-year students with transition into university life  
- Maintained accurate and confidential student records  
- Participated in weekly mentoring team meetings  
"""
)

st.subheader("BSc Mathematical Sciences Group Tutor")
st.write("Sefako Makgatho Health Sciences University | Jan 2024 – Jul 2024")

st.markdown(
    """
- Tutored Mathematics and Statistics to small groups of students  
- Marked assessments with accuracy and met strict deadlines  
- Invigilated first-year Statistics tests and examinations  
- Compiled and maintained student intake registers using Microsoft Word  
"""
)

st.subheader("QuantifyYourFuture (QYF) Intern")
st.write("Virtual Internship | Jan 2025 – Feb 2025")

st.markdown(
    """
- Extracted, cleaned, and prepared large datasets under tight deadlines  
- Collaborated with a virtual team to meet a 48-hour delivery window  
- Built and validated data models for accurate analysis  
- Used **Python (Pandas, NumPy, Matplotlib, Scikit-Learn)** for EDA and automation  
- Applied Microsoft Excel as a data analysis and programming tool  
"""
)

# ---------------- SKILLS ----------------
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
- PowerPoint (Intermediate)  
- Power BI (Basic)  
"""
    )

with col2:
    st.subheader("Transferable Skills")
    st.markdown(
        """
- Strong analytical and problem-solving skills  
- Clear communication and presentation of insights  
- Mentoring and peer-support experience  
- Ability to work under pressure and tight deadlines  
- Growth mindset and eagerness to learn  
"""
    )

# ---------------- HOBBIES ----------------
st.header("Interests & Hobbies")

st.markdown(
    """
- Learning languages  
- Web design  
- Reading and writing  
- Fitness and working out  
- Chess and sports  
"""
)
