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
    background-color:#f7f9fc;
}

.block-container{
    padding-top:0rem;
    max-width:1400px;
}

.navbar{
    background:white;
    padding:20px 40px;
    border-radius:15px;
    margin-bottom:20px;
}

.hero-title{
    font-size:60px;
    font-weight:700;
    color:#0d1b4c;
    line-height:1.1;
}

.hero-blue{
    color:#2563eb;
}

.hero-text{
    color:#555;
    font-size:18px;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:16px;
    text-align:center;
    box-shadow:0 2px 10px rgba(0,0,0,.05);
}

.section-title{
    text-align:center;
    font-size:36px;
    font-weight:700;
    color:#1e293b;
    margin-top:40px;
}

.solution-card{
    background:white;
    padding:25px;
    border-radius:20px;
    min-height:220px;
    box-shadow:0 2px 10px rgba(0,0,0,.05);
}

.footer{
    background:white;
    padding:30px;
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# NAVIGATION
# ==========================

st.markdown("""
<div class='navbar'>
<b>PeopleOrigin</b>
&nbsp;&nbsp;&nbsp;&nbsp; Home
&nbsp;&nbsp;&nbsp;&nbsp; Solutions
&nbsp;&nbsp;&nbsp;&nbsp; Features
&nbsp;&nbsp;&nbsp;&nbsp; Industries
&nbsp;&nbsp;&nbsp;&nbsp; Resources
&nbsp;&nbsp;&nbsp;&nbsp; About Us
&nbsp;&nbsp;&nbsp;&nbsp; Contact
</div>
""", unsafe_allow_html=True)

# ==========================
# HERO SECTION
# ==========================

left,right = st.columns([1,1.3])

with left:

    st.markdown("""
    <div class='hero-title'>
    Simplify HR.<br>
    <span class='hero-blue'>
    Empower People.
    </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='hero-text'>
    A modern workforce platform helping organizations
    manage people, attendance, performance and workforce
    analytics from one place.
    </div>
    """, unsafe_allow_html=True)

    col1,col2 = st.columns(2)

    with col1:
        st.button("Request Demo")

    with col2:
        st.button("Explore Solutions")

with right:

    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        use_container_width=True
    )

st.write("")

# ==========================
# KPI SECTION
# ==========================

a,b,c,d,e = st.columns(5)

with a:
    st.markdown("""
    <div class='metric-card'>
    <h2>500+</h2>
    Organizations
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class='metric-card'>
    <h2>50K+</h2>
    Active Users
    </div>
    """, unsafe_allow_html=True)

with c:
    st.markdown("""
    <div class='metric-card'>
    <h2>98%</h2>
    Satisfaction
    </div>
    """, unsafe_allow_html=True)

with d:
    st.markdown("""
    <div class='metric-card'>
    <h2>1M+</h2>
    Tasks Processed
    </div>
    """, unsafe_allow_html=True)

with e:
    st.markdown("""
    <div class='metric-card'>
    <h2>24/7</h2>
    Support
    </div>
    """, unsafe_allow_html=True)

# ==========================
# SOLUTIONS
# ==========================

st.markdown(
"<div class='section-title'>Comprehensive Workforce Solutions</div>",
unsafe_allow_html=True
)

c1,c2,c3,c4,c5,c6 = st.columns(6)

cards = [
"Employee Management",
"Attendance Tracking",
"Leave Management",
"Performance",
"Payroll",
"Reports & Analytics"
]

for col,title in zip(
[c1,c2,c3,c4,c5,c6],
cards
):
    with col:
        st.markdown(f"""
        <div class='solution-card'>
        <h4>{title}</h4>
        <p>
        Modern tools designed to simplify
        workforce operations.
        </p>
        </div>
        """, unsafe_allow_html=True)

# ==========================
# ANALYTICS SECTION
# ==========================

st.markdown(
"<div class='section-title'>Data Driven Insights</div>",
unsafe_allow_html=True
)

left,right = st.columns([1,2])

with left:

    st.metric("Productivity", "87%", "+10%")
    st.metric("Engagement", "92%", "+16%")

with right:

    df = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
        "Employees":[400,520,610,720,830,900,1040,1150]
    })

    fig = px.line(
        df,
        x="Month",
        y="Employees",
        markers=True
    )

    fig.update_layout(height=350)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================
# PROCESS
# ==========================

st.markdown(
"<div class='section-title'>Our Proven Process</div>",
unsafe_allow_html=True
)

a,b,c,d = st.columns(4)

a.info("01 Assess")
b.info("02 Plan")
c.info("03 Implement")
d.info("04 Optimize")

# ==========================
# CLIENTS
# ==========================

st.markdown(
"<div class='section-title'>Trusted By Organizations</div>",
unsafe_allow_html=True
)

st.write(
"TechNova • BrightPath • Apex Solutions • CloudPeak • NextGen • StrideUp"
)

# ==========================
# BLOG SECTION
# ==========================

st.markdown(
"<div class='section-title'>Insights & Resources</div>",
unsafe_allow_html=True
)

x,y,z,w = st.columns(4)

for card in [x,y,z,w]:

    with card:
        st.image(
        "https://images.unsplash.com/photo-1552664730-d307ca884978",
        use_container_width=True
        )
        st.write("Future of Workforce Management")
        st.button("Read More")

# ==========================
# CONTACT
# ==========================

st.markdown(
"<div class='section-title'>Ready To Transform Operations?</div>",
unsafe_allow_html=True
)

left,right = st.columns([1,1])

with left:
    st.write(
        "Join organizations using modern workforce technology."
    )

with right:

    name = st.text_input("Full Name")
    email = st.text_input("Work Email")
    company = st.text_input("Company")
    msg = st.text_area("Message")

    st.button("Send Message")

# ==========================
# FOOTER
# ==========================

st.markdown("""
<div class='footer'>
<b>PeopleOrigin</b><br>
Workforce Platform for Modern Organizations
</div>
""", unsafe_allow_html=True)
