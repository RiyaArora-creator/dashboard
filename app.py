import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="PeopleOrigin",
    layout="wide"
)

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# HERO

left,right = st.columns([1,1.2])

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
    Streamline operations, analytics and engagement.
    </div>
    """, unsafe_allow_html=True)

    col1,col2 = st.columns(2)

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

# KPI SECTION

a,b,c,d = st.columns(4)

a.metric("Organizations","500+")
b.metric("Users","50K+")
c.metric("Satisfaction","98%")
d.metric("Support","24/7")

# CHART

df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Users":[200,350,450,650,800,1000]
})

fig = px.line(
    df,
    x="Month",
    y="Users",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.subheader("Solutions")

c1,c2,c3 = st.columns(3)

with c1:
    st.info("People Management")

with c2:
    st.success("Workforce Analytics")

with c3:
    st.warning("Performance Insights")

st.markdown("---")

st.subheader("Contact")

st.text_input("Name")
st.text_input("Email")
st.text_area("Message")

st.button("Send")
