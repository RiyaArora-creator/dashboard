import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PeopleOrigin",
    layout="wide"
)

st.title("PeopleOrigin")
st.caption("Modern Workforce Platform")

st.divider()

# HERO

left, right = st.columns([1, 1])

with left:
    st.markdown("# Simplify Workforce")
    st.markdown("## Empower People")

    st.write(
        """
        Modern workforce platform for growing organizations.
        Streamline operations, analytics, collaboration,
        and workforce engagement from one place.
        """
    )

    st.button("Request Demo")
    st.button("Explore Platform")

with right:
    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        use_container_width=True
    )

# KPI SECTION

st.header("Trusted Worldwide")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric("Organizations", "500+")

with k2:
    st.metric("Users", "50K+")

with k3:
    st.metric("Satisfaction", "98%")

with k4:
    st.metric("Support", "24/7")

# DASHBOARD PREVIEW

st.header("Interactive Dashboard Preview")

st.image(
    "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
    use_container_width=True
)

# PLATFORM OVERVIEW

st.header("Platform Overview")

left, right = st.columns([1, 1.5])

with left:
    st.subheader("One Platform. Multiple Capabilities")

    st.write(
        """
        Manage workforce operations,
        monitor productivity,
        analyze trends,
        and improve decision-making.
        """
    )

with right:
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Growth": [120, 220, 380, 520, 700, 920]
    })

    fig = px.area(
        df,
        x="Month",
        y="Growth"
    )

    st.plotly_chart(fig, use_container_width=True)

# SOLUTIONS

st.header("Core Solutions")

s1, s2, s3 = st.columns(3)

with s1:
    st.info("People Management")

with s2:
    st.success("Attendance & Scheduling")

with s3:
    st.warning("Performance Insights")

# ANALYTICS

st.header("Workforce Analytics")

df2 = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Users": [200, 350, 450, 650, 800, 1000]
})

fig2 = px.line(
    df2,
    x="Month",
    y="Users",
    markers=True
)

st.plotly_chart(fig2, use_container_width=True)

# CLIENTS

st.header("Trusted By Organizations")

c1, c2, c3, c4, c5 = st.columns(5)

c1.success("TechNova")
c2.success("BrightPath")
c3.success("CloudPeak")
c4.success("NextGen")
c5.success("StrideUp")

# TESTIMONIALS

st.header("Customer Stories")

t1, t2 = st.columns(2)

with t1:
    st.success(
        """
        Operational Excellence

        The platform transformed our operations.
        """
    )

with t2:
    st.info(
        """
        Better Visibility

        Analytics improved decision making.
        """
    )

# FAQ

st.header("Frequently Asked Questions")

with st.expander("How does the platform help organizations?"):
    st.write("Centralizes operations and analytics.")

with st.expander("Can the platform scale with growth?"):
    st.write("Yes, it is designed for growing organizations.")

with st.expander("Does it provide reporting capabilities?"):
    st.write("Yes, advanced analytics and reporting are available.")

# CONTACT

st.header("Contact Us")

st.text_input("Name")
st.text_input("Email")
st.text_area("Message")

st.button("Send Message")

st.divider()

st.markdown(
    """
    ### PeopleOrigin

    Modern Workforce Platform for Growing Organizations

    © 2026 All Rights Reserved
    """
)
