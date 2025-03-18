import streamlit as st
from QandA import make_vars, get_chain_ans, make_vec_db

st.title("Fun Flower Facts Q&A")
question = st.text_input("Question: ", value = "Type a question regarding flowers, then press enter")
st.header("Answer: ")


if question:
    llm, embed = make_vars()
    ans = get_chain_ans(llm, embed, question)
    st.header("Answer: ")
    st.write(ans)
    