import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PeopleOrigin",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main {
    background-color: #F8FBFF;
}

.hero {
    background: linear-gradient(135deg,#0F172A,#2563EB);
    padding: 60px;
    border-radius: 25px;
    color: white;
}

.navbar {
    background: #0F172A;
    padding: 15px;
    border-radius: 15px;
    color: white;
    margin-bottom: 20px;
}

.kpi-card {
    background: #2563EB;
    color: white;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
}

.module-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #2563EB;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

.footer {
    text-align: center;
    color: gray;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# NAVBAR
# ==================================================

st.markdown("""
<div class="navbar">
<h3>PeopleOrigin</h3>
</div>
""", unsafe_allow_html=True)

# ==================================================
# HERO SECTION
# ==================================================

st.markdown("""
<div class="hero">
<h1>Workforce Intelligence Platform</h1>

<p style="font-size:18px;">
Manage people, attendance, performance,
analytics and workforce operations through
one modern digital platform.
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

left, right = st.columns([1,1])

with left:

    c1, c2, c3 = st.columns(3)

    with c1:
        st.button("Login")

    with c2:
        st.button("Request Demo")

    with c3:
        st.button("Explore Platform")

with right:
    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        use_container_width=True
    )

# ==================================================
# DASHBOARD PREVIEW
# ==================================================

st.markdown("## Platform Snapshot")

st.image(
    "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
    use_container_width=True
)

# ==================================================
# KPI SECTION
# ==================================================

st.markdown("## Workforce Overview")

k1, k2, k3, k4 = st.columns(4)

cards = [
    ("1,248", "Employees"),
    ("96%", "Attendance"),
    ("18", "Open Roles"),
    ("23", "Pending Leaves")
]

for col, (value, label) in zip([k1, k2, k3, k4], cards):

    with col:

        st.markdown(f"""
        <div class="kpi-card">
        <h2>{value}</h2>
        <p>{label}</p>
        </div>
        """, unsafe_allow_html=True)

# ==================================================
# GROWTH CHART
# ==================================================

st.markdown("## Employee Growth")

growth = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "Employees": [150,260,420,580,760,980]
})

fig = px.area(
    growth,
    x="Month",
    y="Employees"
)

fig.update_layout(
    paper_bgcolor="white",
    plot_bgcolor="white"
)

st.plotly_chart(fig, use_container_width=True)

# ==================================================
# ANALYTICS SECTION
# ==================================================

left, right = st.columns(2)

with left:

    st.markdown("### Department Distribution")

    dept = pd.DataFrame({
        "Department": [
            "HR",
            "IT",
            "Finance",
            "Operations",
            "Support"
        ],
        "Employees": [
            45,
            120,
            35,
            80,
            50
        ]
    })

    fig2 = px.pie(
        dept,
        names="Department",
        values="Employees",
        hole=0.5,
        color_discrete_sequence=px.colors.sequential.Blues_r
    )

    st.plotly_chart(fig2, use_container_width=True)

with right:

    st.markdown("### Team Performance")

    team = pd.DataFrame({
        "Team": [
            "HR",
            "IT",
            "Finance",
            "Operations"
        ],
        "Score": [
            88,
            95,
            84,
            90
        ]
    })

    fig3 = px.bar(
        team,
        x="Team",
        y="Score",
        color="Score",
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig3, use_container_width=True)

# ==================================================
# CORE MODULES
# ==================================================

st.markdown("## Core Modules")

m1, m2, m3, m4 = st.columns(4)

modules = [
    "Employee Management",
    "Attendance Tracking",
    "Performance Reviews",
    "Workforce Analytics"
]

for col, module in zip([m1, m2, m3, m4], modules):

    with col:

        st.markdown(f"""
        <div class="module-card">
        <h4>{module}</h4>
        </div>
        """, unsafe_allow_html=True)

# ==================================================
# RECENT ACTIVITIES
# ==================================================

st.markdown("## Recent Activities")

activities = pd.DataFrame({
    "Activity": [
        "New employee joined IT team",
        "Leave request approved",
        "Performance review completed",
        "Training assigned",
        "Attendance report generated"
    ]
})

st.dataframe(
    activities,
    use_container_width=True,
    hide_index=True
)

# ==================================================
# ANNOUNCEMENTS
# ==================================================

st.markdown("## Announcements")

st.info("Quarterly performance review cycle starts next week.")
st.info("Employee engagement survey opens on Monday.")
st.info("Leadership town hall scheduled for Friday.")

# ==================================================
# QUICK ACTIONS
# ==================================================

st.markdown("## Quick Actions")

q1, q2, q3, q4 = st.columns(4)

with q1:
    st.button("Add Employee")

with q2:
    st.button("Approve Leave")

with q3:
    st.button("Generate Report")

with q4:
    st.button("View Analytics")

# ==================================================
# CONTACT
# ==================================================

st.markdown("## Contact Us")

st.text_input("Name")
st.text_input("Email")
st.text_area("Message")

st.button("Send Message")

# ==================================================
# CTA SECTION
# ==================================================

st.markdown("""
<div style="
background:linear-gradient(135deg,#0F172A,#2563EB);
padding:50px;
border-radius:25px;
text-align:center;
color:white;
margin-top:30px;
">

<h1>Transform Workforce Operations</h1>

<p>
Manage people, performance, attendance and
analytics through one modern platform.
</p>

</div>
""", unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.markdown("""
<div class="footer">
<h3>PeopleOrigin</h3>
Modern Workforce Platform for Growing Organizations
<br><br>
© 2026 All Rights Reserved
</div>
""", unsafe_allow_html=True)
