import streamlit as st

st.json({'data' : 'name'})

mycode = '''
def sayHello() :
    print('Hello Streamlit!')
'''

st.code(mycode, language='python')