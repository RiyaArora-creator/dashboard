import streamlit as st

st.set_page_config(
    page_title="WorkforcePro",
    layout="wide"
)

# HERO SECTION

st.title("Build Better Teams. Work Smarter.")
st.subheader(
    "A modern workforce management platform designed to simplify operations, improve productivity, and streamline collaboration."
)

col1, col2 = st.columns(2)

with col1:
    st.button("Get Started")

with col2:
    st.button("Sign In")

st.divider()

# FEATURES

st.header("Key Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
    ### People Management

    Manage workforce information from a centralized platform.
    """)

with c2:
    st.success("""
    ### Smart Analytics

    Transform operational data into actionable insights.
    """)

with c3:
    st.warning("""
    ### Workflow Automation

    Reduce manual effort through intelligent workflows.
    """)

st.divider()

# STATS

st.header("Platform Insights")

a, b, c, d = st.columns(4)

a.metric("Organizations", "500+")
b.metric("Users", "25K+")
c.metric("Tasks Managed", "1M+")
d.metric("Satisfaction", "98%")

st.divider()

# PROCESS

st.header("How It Works")

st.markdown("""
1. Create your workspace  
2. Invite team members  
3. Configure workflows  
4. Track performance  
5. Generate insights and reports
""")

st.divider()

# TESTIMONIALS

st.header("What Clients Say")

st.success("""
"The platform helped us improve operational efficiency and team visibility."
""")

st.info("""
"Easy to use, modern design, and excellent reporting capabilities."
""")

st.divider()

# FOOTER

st.caption("© 2026 WorkforcePro. All rights reserved.")
