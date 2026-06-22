import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PeopleOrigin",
    layout="wide"
)

# ======================
# CUSTOM CSS
# ======================

st.markdown("""
<style>

.main{
    background-color:#f7fbff;
}

.kpi-card{
    padding:20px;
    border-radius:15px;
    color:white;
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# ======================
# HERO SECTION
# ======================

st.markdown("""
<div style="
background:linear-gradient(135deg,#1e3a8a,#60a5fa);
padding:50px;
border-radius:20px;
color:white;
">

<h1>Workforce Intelligence Platform</h1>

<p>
Manage people, attendance, performance and analytics
through one modern workforce platform.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

left, right = st.columns([1,1])

with left:
    st.button("Request Demo")
    st.button("Explore Platform")

with right:
    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        use_container_width=True
    )

# ======================
# KPI SECTION
# ======================

st.subheader("Workforce Overview")

k1,k2,k3,k4 = st.columns(4)

with k1:
    st.metric("Employees","1,248","+12")

with k2:
    st.metric("Attendance","96%","+2%")

with k3:
    st.metric("Open Roles","18","+4")

with k4:
    st.metric("Pending Leaves","23","-3")

# ======================
# ANALYTICS
# ======================

st.subheader("Employee Growth")

growth = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Employees":[150,260,420,580,760,980]
})

fig = px.area(
    growth,
    x="Month",
    y="Employees"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ======================
# DEPARTMENT CHART
# ======================

left,right = st.columns(2)

with left:

    st.subheader("Department Distribution")

    dept = pd.DataFrame({
        "Department":[
            "HR",
            "IT",
            "Finance",
            "Operations",
            "Support"
        ],
        "Employees":[
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
        hole=0.5
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

with right:

    st.subheader("Team Performance")

    team = pd.DataFrame({
        "Team":[
            "HR",
            "IT",
            "Finance",
            "Operations"
        ],
        "Score":[
            88,
            95,
            84,
            90
        ]
    })

    fig3 = px.bar(
        team,
        x="Team",
        y="Score"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# ======================
# RECENT ACTIVITIES
# ======================

st.subheader("Recent Activities")

activities = pd.DataFrame({
    "Activity":[
        "New employee joined IT team",
        "Leave request approved",
        "Performance review completed",
        "Training program assigned"
    ]
})

st.dataframe(
    activities,
    use_container_width=True,
    hide_index=True
)

# ======================
# ANNOUNCEMENTS
# ======================

st.subheader("Announcements")

st.info(
    "Quarterly performance review cycle starts next week."
)

st.info(
    "Employee engagement survey opens on Monday."
)

st.info(
    "Leadership town hall scheduled for Friday."
)

# ======================
# QUICK ACTIONS
# ======================

st.subheader("Quick Actions")

a,b,c,d = st.columns(4)

with a:
    st.button("Add Employee")

with b:
    st.button("Approve Leave")

with c:
    st.button("Generate Report")

with d:
    st.button("View Analytics")

# ======================
# CONTACT
# ======================

st.subheader("Contact Us")

st.text_input("Name")
st.text_input("Email")
st.text_area("Message")

st.button("Send Message")

# ======================
# FOOTER
# ======================

st.markdown("---")

st.markdown("""
<div class='footer'>
<h3>PeopleOrigin</h3>
Modern Workforce Platform for Growing Organizations
<br><br>
© 2026 All Rights Reserved
</div>
""", unsafe_allow_html=True)
