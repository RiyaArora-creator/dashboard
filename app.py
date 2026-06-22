import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PeopleOrigin",
    layout="wide"
)

# =========================
# CUSTOM STYLING
# =========================

st.markdown("""
<style>

.main{
    background-color:#f8fbff;
}

.hero{
    background:linear-gradient(135deg,#0f172a,#2563eb);
    padding:70px;
    border-radius:25px;
    color:white;
    margin-bottom:40px;
}

.card{
    padding:25px;
    border-radius:20px;
    color:white;
    text-align:center;
    box-shadow:0px 8px 20px rgba(0,0,0,0.1);
}

.feature-card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 6px 15px rgba(0,0,0,0.08);
}

.footer{
    text-align:center;
    color:gray;
    padding:30px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("PeopleOrigin")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "Workforce",
        "Reports"
    ]
)

st.sidebar.success("System Online")

# =========================
# HERO SECTION
# =========================

st.markdown("""
<div class="hero">
<h1 style="font-size:60px;">
Workforce Intelligence Platform
</h1>

<p style="font-size:20px;">
Manage people, productivity, analytics and operations
through one modern digital platform.
</p>
</div>
""", unsafe_allow_html=True)

left,right = st.columns([1,1])

with left:
    st.button("Request Demo")
    st.button("Explore Platform")

with right:
    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        use_container_width=True
    )

# =========================
# KPI SECTION
# =========================

st.subheader("Trusted Worldwide")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="card" style="background:#2563eb;">
    <h2>500+</h2>
    Organizations
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card" style="background:#10b981;">
    <h2>50K+</h2>
    Active Users
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card" style="background:#f59e0b;">
    <h2>98%</h2>
    Satisfaction
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card" style="background:#ef4444;">
    <h2>24/7</h2>
    Support
    </div>
    """, unsafe_allow_html=True)

# =========================
# PLATFORM MODULES
# =========================

st.subheader("Platform Modules")

m1,m2,m3 = st.columns(3)

with m1:
    st.image(
        "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40",
        use_container_width=True
    )
    st.markdown("### People Management")
    st.write("Manage workforce records and employee lifecycle.")

with m2:
    st.image(
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
        use_container_width=True
    )
    st.markdown("### Workforce Analytics")
    st.write("Gain insights through interactive reporting.")

with m3:
    st.image(
        "https://images.unsplash.com/photo-1553877522-43269d4ea984",
        use_container_width=True
    )
    st.markdown("### Performance Tracking")
    st.write("Track goals, performance and productivity.")

# =========================
# DASHBOARD PREVIEW
# =========================

st.subheader("Interactive Dashboard Preview")

st.image(
    "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
    use_container_width=True
)

# =========================
# ANALYTICS
# =========================

st.subheader("Organization Growth")

growth = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Employees":[120,250,380,550,780,1000]
})

fig = px.area(
    growth,
    x="Month",
    y="Employees",
    title="Employee Growth Trend"
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# DEPARTMENT DISTRIBUTION
# =========================

st.subheader("Department Distribution")

dept = pd.DataFrame({
    "Department":["HR","IT","Finance","Operations","Support"],
    "Employees":[45,120,35,80,50]
})

fig2 = px.pie(
    dept,
    names="Department",
    values="Employees",
    hole=0.5
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# WORKFORCE EXPLORER
# =========================

st.subheader("Workforce Explorer")

f1,f2 = st.columns(2)

with f1:
    department = st.selectbox(
        "Department",
        ["HR","IT","Finance","Operations"]
    )

with f2:
    month = st.selectbox(
        "Month",
        ["Jan","Feb","Mar","Apr","May","Jun"]
    )

st.success(
    f"Showing workforce data for {department} during {month}"
)

# =========================
# PROJECT PROGRESS
# =========================

st.subheader("Project Progress")

st.write("Recruitment Campaign")
st.progress(75)

st.write("Performance Reviews")
st.progress(90)

st.write("Training Completion")
st.progress(60)

# =========================
# TESTIMONIALS
# =========================

st.subheader("Customer Stories")

t1,t2 = st.columns(2)

with t1:
    st.info("""
    Operational Excellence

    The platform transformed our workforce operations
    and improved visibility.
    """)

with t2:
    st.success("""
    Better Decision Making

    Real-time analytics helped leadership teams
    make faster decisions.
    """)

# =========================
# FAQ
# =========================

st.subheader("Frequently Asked Questions")

with st.expander("How does the platform help organizations?"):
    st.write("Centralizes workforce operations and analytics.")

with st.expander("Can it scale with growth?"):
    st.write("Yes. Designed for growing organizations.")

with st.expander("Does it provide reporting?"):
    st.write("Yes. Interactive dashboards and reports are available.")

# =========================
# CTA SECTION
# =========================

st.markdown("""
<div style="
background:linear-gradient(135deg,#2563eb,#60a5fa);
padding:50px;
border-radius:25px;
color:white;
text-align:center;
margin-top:30px;
">

<h1>Ready To Transform Your Workforce?</h1>

<p>
Modern workforce management, analytics and reporting
in one platform.
</p>

</div>
""", unsafe_allow_html=True)

st.button("Get Started")

# =========================
# CONTACT
# =========================

st.subheader("Contact Us")

st.text_input("Name")
st.text_input("Email")
st.text_area("Message")

st.button("Send Message")

# =========================
# FOOTER
# =========================

st.markdown("---")

st.markdown("""
<div class="footer">
<h3>PeopleOrigin</h3>
Modern Workforce Platform for Growing Organizations
<br><br>
© 2026 All Rights Reserved
</div>
""", unsafe_allow_html=True)
