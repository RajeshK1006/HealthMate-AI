import streamlit as st
from chat import langchainning

def user_input(user):
   
    ans = langchainning().run(user)
    return ans

st.title("HealthMate-AI")
st.caption("Hi Human, How can I help you today?")

if "messages" not in st.session_state:
    st.session_state.messages = []



q = st.chat_input("Type something here....")


if q:
    st.session_state.messages.append(("user", q))
    st.session_state.messages.append(("assistant", user_input(q)))

    for role, message in st.session_state.messages:
        if role == "user":
            st.chat_message("user")
            st.write(message)
        elif role == "assistant":
            st.chat_message("assistant")
            st.write(message)

q =  st.button("Clear Chat")
if q:
    st.session_state.messages = []

