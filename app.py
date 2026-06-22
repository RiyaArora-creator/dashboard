import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PeopleOrigin",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>
.main {
    background-color: #f5f9ff;
}

.hero {
    background: linear-gradient(135deg,#2563eb,#60a5fa);
    padding: 50px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
}

.footer {
    text-align:center;
    padding:20px;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("PeopleOrigin")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Analytics", "Workforce", "Reports"]
)

st.sidebar.success("System Online")

# ==========================
# HERO SECTION
# ==========================

st.markdown("""
<div class="hero">
<h1>PeopleOrigin</h1>
<h3>Modern Workforce Intelligence Platform</h3>
<p>Analytics • Workforce • Productivity • Insights</p>
</div>
""", unsafe_allow_html=True)

# ==========================
# KPI CARDS
# ==========================

st.subheader("Trusted Worldwide")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="card" style="background:#2563eb">
    <h2>500+</h2>
    Organizations
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card" style="background:#10b981">
    <h2>50K+</h2>
    Active Users
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card" style="background:#f59e0b">
    <h2>98%</h2>
    Satisfaction
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card" style="background:#ef4444">
    <h2>24/7</h2>
    Support
    </div>
    """, unsafe_allow_html=True)

# ==========================
# DASHBOARD PREVIEW
# ==========================

st.subheader("Interactive Dashboard Preview")

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Growth":[120,220,380,520,700,920]
})

fig = px.area(
    df,
    x="Month",
    y="Growth",
    title="Organization Growth"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================
# ANALYTICS
# ==========================

st.subheader("Workforce Analytics")

df2 = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Employees":[200,350,450,650,800,1000]
})

fig2 = px.line(
    df2,
    x="Month",
    y="Employees",
    markers=True,
    title="Employee Growth"
)

st.plotly_chart(fig2, use_container_width=True)

# ==========================
# WORKFORCE DISTRIBUTION
# ==========================

st.subheader("Workforce Distribution")

dept = pd.DataFrame({
    "Department":["HR","IT","Finance","Operations","Support"],
    "Employees":[45,120,35,80,50]
})

fig3 = px.pie(
    dept,
    names="Department",
    values="Employees",
    hole=0.5
)

st.plotly_chart(fig3, use_container_width=True)

# ==========================
# FILTERS
# ==========================

st.subheader("Workforce Explorer")

col1, col2 = st.columns(2)

with col1:
    department = st.selectbox(
        "Department",
        ["HR","IT","Finance","Operations"]
    )

with col2:
    month = st.selectbox(
        "Month",
        ["Jan","Feb","Mar","Apr","May"]
    )

st.success(f"Showing data for {department} - {month}")

# ==========================
# PROGRESS
# ==========================

st.subheader("Project Progress")

st.write("Recruitment Campaign")
st.progress(75)

st.write("Performance Reviews")
st.progress(90)

st.write("Training Completion")
st.progress(60)

# ==========================
# SOLUTIONS
# ==========================

st.subheader("Core Solutions")

s1, s2, s3 = st.columns(3)

with s1:
    st.info("People Management")

with s2:
    st.success("Attendance & Scheduling")

with s3:
    st.warning("Performance Insights")

# ==========================
# FAQ
# ==========================

st.subheader("Frequently Asked Questions")

with st.expander("How does the platform help organizations?"):
    st.write("Centralizes workforce operations and analytics.")

with st.expander("Can the platform scale with growth?"):
    st.write("Yes, it is designed for growing organizations.")

with st.expander("Does it provide reporting capabilities?"):
    st.write("Yes, advanced analytics and reporting are available.")

# ==========================
# CONTACT
# ==========================

st.subheader("Contact Us")

st.text_input("Name")
st.text_input("Email")
st.text_area("Message")

st.button("Send Message")

# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.markdown("""
<div class="footer">
<h3>PeopleOrigin</h3>
Modern Workforce Platform for Growing Organizations<br><br>
© 2026 All Rights Reserved
</div>
""", unsafe_allow_html=True)
