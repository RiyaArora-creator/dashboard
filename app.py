import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PeopleOrigin",
    layout="wide"
)

# Load CSS
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==================================
# HERO SECTION
# ==================================

left, right = st.columns([1, 1.2])

with left:

    st.markdown("""
    <div class='hero-title'>
    Simplify Workforce.<br>
    <span class='hero-blue'>
    Empower People.
    </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='hero-text'>
    Modern workforce platform for growing organizations.
    Streamline operations, analytics, collaboration,
    and workforce engagement from one place.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.button("Request Demo")

    with col2:
        st.button("Explore Platform")

with right:

    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        use_container_width=True
    )

st.write("")

# ==================================
# KPI SECTION
# ==================================

st.markdown("<div class='section-title'>Trusted Worldwide</div>", unsafe_allow_html=True)

a, b, c, d = st.columns(4)

with a:
    st.markdown("""
    <div class='kpi-card'>
    <h2>500+</h2>
    Organizations
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class='kpi-card'>
    <h2>50K+</h2>
    Active Users
    </div>
    """, unsafe_allow_html=True)

with c:
    st.markdown("""
    <div class='kpi-card'>
    <h2>98%</h2>
    Satisfaction
    </div>
    """, unsafe_allow_html=True)

with d:
    st.markdown("""
    <div class='kpi-card'>
    <h2>24/7</h2>
    Support
    </div>
    """, unsafe_allow_html=True)

# ==================================
# PLATFORM OVERVIEW
# ==================================

st.markdown("<div class='section-title'>Platform Overview</div>", unsafe_allow_html=True)

left, right = st.columns([1, 1.5])

with left:

    st.subheader("One Platform. Multiple Capabilities")

    st.write("""
    Manage workforce operations,
    monitor productivity,
    analyze trends,
    and improve decision-making
    through a unified experience.
    """)

    st.button("Explore Modules")

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

    fig.update_layout(height=350)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==================================
# CORE SOLUTIONS
# ==================================

st.markdown("<div class='section-title'>Core Solutions</div>", unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)

with r1:
    st.info("People Management")

with r2:
    st.success("Attendance & Scheduling")

with r3:
    st.warning("Performance Insights")

r4, r5, r6 = st.columns(3)

with r4:
    st.info("Leave Administration")

with r5:
    st.success("Workforce Analytics")

with r6:
    st.warning("Reports & Compliance")

# ==================================
# ANALYTICS
# ==================================

st.markdown("<div class='section-title'>Data Driven Insights</div>", unsafe_allow_html=True)

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

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==================================
# PROCESS
# ==================================

st.markdown("<div class='section-title'>Our Process</div>", unsafe_allow_html=True)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.success("01 Assess")

with p2:
    st.info("02 Plan")

with p3:
    st.warning("03 Implement")

with p4:
    st.success("04 Optimize")

# ==================================
# TESTIMONIALS
# ==================================

st.markdown("<div class='section-title'>Customer Stories</div>", unsafe_allow_html=True)

t1, t2 = st.columns(2)

with t1:
    st.markdown("""
    <div class='solution-card'>
    <h4>Operational Excellence</h4>
    The platform transformed how our teams
    manage daily operations and reporting.
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("""
    <div class='solution-card'>
    <h4>Better Visibility</h4>
    Powerful dashboards and analytics
    helped improve decision-making.
    </div>
    """, unsafe_allow_html=True)

# ==================================
# RESOURCES
# ==================================

st.markdown("<div class='section-title'>Insights & Resources</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

cards = [
    "Future of Workforce Technology",
    "Productivity Best Practices",
    "Workforce Analytics Trends"
]

for i, (col, title) in enumerate(zip([c1, c2, c3], cards)):

    with col:

        st.image(
            "https://images.unsplash.com/photo-1552664730-d307ca884978",
            use_container_width=True
        )

        st.write(title)

        st.button(
            "Read More",
            key=f"blog_{i}"
        )

# ==================================
# CONTACT
# ==================================

st.markdown("<div class='section-title'>Contact Us</div>", unsafe_allow_html=True)

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

st.button("Send Message")

# ==================================
# FOOTER
# ==================================

st.markdown("---")

st.markdown("""
<div class='footer'>
<h3>PeopleOrigin</h3>
Modern Workforce Platform for Growing Organizations
</div>
""", unsafe_allow_html=True)
