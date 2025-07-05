# app.py
import streamlit as st
import pandas as pd
from chatbot import generate_reply_for_user
from analytics import store_user_data

#Background-color and font
st.markdown(
    """
    <style>
    body{
        background-color:#f9f9f9;
    }
    .stApp{
        font-family:'comic Sans MS',cursive;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Start of app ui
st.set_page_config(page_title="Analytics Chat Bot", page_icon="🤖")
st.title("🤖 Hello! I'm your friendly chatbot")
st.subheader("🧠 Ask me anything,and I'll try my best to help!")

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712107.png",width=100)
    st.header("🧭 Choose what you want")
    menu = st.selectbox("💡 Pick a featur:",["💬 Chatbot","📊 Analytics"])

if menu == "💬 Chatbot":
    st.subheader("Ask a Question:")
    st.markdown("### 👧 What would you like to ask?")
    if "last_rating" not in st.session_state:
        st.session_state.last_rating = 0
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    user_question = st.text_input("Type your question below:",key="input",placeholder="e.g.,What is java?")
    if st.button("Send"):
        response, topic = generate_reply_for_user(user_question)
        st.session_state.user_question = user_question
        st.session_state.response = response
        st.session_state.topic = topic
        st.success(f"🤖 chatbot says: {response}")
        st.session_state.submitted = True
        
    if st.session_state.submitted:
        rating = st.slider("🧡 How happy are you with my answer? (1-5)", 1, 5, key="rating_slider")

        # Automatically store only if rating is changed
        if rating != st.session_state.last_rating:
            st.session_state.last_rating = rating
            store_user_data(
                st.session_state.user_question,
                st.session_state.response,
                st.session_state.topic,
                rating
            )


    

elif menu == "📊 Analytics":
    st.subheader("📊 Here's how users are using the bot:")
    df = pd.read_csv("data/log.csv")

    st.metric("Total question asked", len(df))

    if not df.empty:
        st.bar_chart(df["topic"].value_counts())

        st.write("Average Satisfaction:")
        st.metric("Rating", round(df["rating"].mean(), 2))
