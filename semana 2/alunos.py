import streamlit as st
import pandas as pd

def main():
    st.image('logo.png')
    st.title('Semana 2')
    st.markdown('Botão')
    botao = st.button('Botão')
    if botao:
        st.markdown('Clicado')
    st.markdown('Checkbox')
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Clicado')
    st.markdown('Radio')
    radio = st.radio('Escolha as opções', ('Opt 1', 'Opt 2'))
    if radio == 'Opt 1':
        st.markdown('Opt 1')
    if radio == 'Opt 2':
        st.markdown('Opt 2')
    st.markdown("Selectbox")
    select = st.selectbox('Choose opt', ('Opt 1', 'Opt 2'))
    if select == 'Opt1':
        st.markdown('Opt1')
    if select == 'Opt 2':
        st.markdown('Opt 2')
    st.markdown('MultiSelect')
    multi = st.multiselect('Choose opt', ('Opt 1', 'Opt 2', 'thiago'))
    if multi == 'Opt 1':
        st.markdown('Opt 1')
    if multi == 'Opt 2':
        st.markdown('Opt 2')
    st.markdown('File Uploader')
    file= st.file_uploader('Choose your files', type = 'csv')
    if file is not None:
        st.markdown('Não está vazio')


if __name__=='__main__':
    main()
