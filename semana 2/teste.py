import streamlit as st
import pandas as pd

def main():
    st.title('AceleraDev Data Science - Semana 2')
    st.image('logo.png')
    file = st.file_uploader('Uploader your file', type = 'csv')
    if file is not None:
        slider = st.slider('Valores', 1,100)
        df = pd.read_csv(file)
        st.markdown('Data Frame')
        st.dataframe(df.head(slider))
        st.markdown('Table')
        st.table(df.head(slider))
        st.write(df.columns)
        st.write(df.info(verbose=True))
        st.table(df.groupby('species')['petal_width'].mean())



if __name__=='__main__':
    main()
