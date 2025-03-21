import streamlit as st
from QandA import make_vars, get_chain_ans, make_vec_db

st.title("Fun Flower Facts Q&A")

question = st.text_input("Question: ")

vdb = st.button("Create DB")

if question:
    llm, embed = make_vars()
    ans = get_chain_ans(llm, embed, question)
    st.header("Answer: ")
    st.write(ans)
    

if vdb:
    _, embed = make_vars()
    make_vec_db(embed)