```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PeopleOrigin", layout="wide")

try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

# NAVBAR
st.markdown("### PeopleOrigin")
st.markdown("Home | Solutions | Analytics | Resources | Contact")
st.divider()

# HERO
col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
    <h1 style='font-size:60px'>
    Simplify Workforce.<br>
    <span style='color:#2563eb'>Empower People.</span>
    </h1>
    """, unsafe_allow_html=True)

    st.write("""
    Modern workforce platform for growing organizations.
    Streamline operations, analytics, collaboration,
    and employee engagement from one place.
    """)

    b1,b2 = st.columns(2)
    with b1:
        st.button("Request Demo")
    with b2:
        st.button("Explore Platform")

with col2:
    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        use_container_width=True
    )

# KPI
st.markdown("## Trusted Worldwide")

k1,k2,k3,k4 = st.columns(4)

k1.metric("Organizations","500+")
k2.metric("Users","50K+")
k3.metric("Satisfaction","98%")
k4.metric("Support","24/7")

# DASHBOARD PREVIEW
st.markdown("## Interactive Dashboard Preview")

st.image(
    "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
    use_container_width=True
)

# PLATFORM OVERVIEW
st.markdown("## Platform Overview")

left,right = st.columns([1,1.5])

with left:
    st.subheader("One Platform. Multiple Capabilities")
    st.write("""
    Manage workforce operations,
    monitor productivity,
    analyze trends and improve
    decision-making from one place.
    """)
    st.button("Explore Modules")

with right:
    df = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May","Jun"],
        "Growth":[120,220,380,520,700,920]
    })

    fig = px.area(df,x="Month",y="Growth")
    st.plotly_chart(fig,use_container_width=True)

# SOLUTIONS
st.markdown("## Core Solutions")

s1,s2,s3 = st.columns(3)

with s1:
    st.info("People Management")

with s2:
    st.success("Attendance & Scheduling")

with s3:
    st.warning("Performance Insights")

# ANALYTICS
st.markdown("## Workforce Analytics")

df2 = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Users":[200,350,450,650,800,1000]
})

fig2 = px.line(
    df2,
    x="Month",
    y="Users",
    markers=True
)

st.plotly_chart(fig2,use_container_width=True)

# PROCESS
st.markdown("## Our Process")

p1,p2,p3,p4 = st.columns(4)

p1.success("01 Assess")
p2.info("02 Plan")
p3.warning("03 Implement")
p4.success("04 Optimize")

# CLIENTS
st.markdown("## Trusted By Organizations")

c1,c2,c3,c4,c5 = st.columns(5)

for col,name in zip(
    [c1,c2,c3,c4,c5],
    ["TechNova","BrightPath","CloudPeak","NextGen","StrideUp"]
):
    with col:
        st.success(name)

# TESTIMONIALS
st.markdown("## Customer Stories")

t1,t2 = st.columns(2)

with t1:
    st.success("""
    Operational Excellence

    The platform transformed our operations.
    """)

with t2:
    st.info("""
    Better Visibility

    Analytics improved decision making.
    """)

# RESOURCES
st.markdown("## Insights & Resources")

r1,r2,r3 = st.columns(3)

titles = [
    "Future of Workforce Technology",
    "Productivity Best Practices",
    "Analytics Trends"
]

for i,(col,title) in enumerate(zip([r1,r2,r3],titles)):
    with col:
        st.image(
            "https://images.unsplash.com/photo-1552664730-d307ca884978",
            use_container_width=True
        )
        st.write(title)
        st.button("Read More",key=f"blog{i}")

# FAQ
st.markdown("## Frequently Asked Questions")

with st.expander("How does the platform help organizations?"):
    st.write("Centralizes operations and analytics.")

with st.expander("Can the platform scale with growth?"):
    st.write("Yes, it is designed for growing teams.")

with st.expander("Does it support reporting?"):
    st.write("Yes, with dashboards and analytics.")

# CTA
st.markdown("## Ready To Transform Your Workforce?")

c1,c2 = st.columns(2)

with c1:
    st.button("Book a Demo")

with c2:
    st.button("Get Started")

# CONTACT
st.markdown("## Contact Us")

st.text_input("Name")
st.text_input("Email")
st.text_area("Message")

st.button("Send Message")

# FOOTER
st.divider()

st.markdown("""
<center>
<h2>PeopleOrigin</h2>
Solutions | Features | Resources | Contact<br><br>
© 2026 PeopleOrigin. All Rights Reserved.
</center>
""", unsafe_allow_html=True)
```
