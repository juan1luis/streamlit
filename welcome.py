import streamlit as st

def bienvanida(nombre):
    mymensaje = 'Bienvenido: ' + nombre
    return mymensaje

myname = st.text_input('Nombre: ')

if (myname):
    mensaje = bienvanida(myname)
    st.write(f"mensaje: {myname}")