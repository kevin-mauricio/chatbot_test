from click import prompt
import streamlit as st
from Roles import Roles
from chatbot import *

st.set_page_config(page_title='Asistente virtual')
st.title('Asistente virtual');

#roles
roles = Roles()
user = roles.USER
assistant = roles.ASSISTANT

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'first_message' not in st.session_state:
    st.session_state.first_message = True

# recorrer el historico de mensajes
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# verificar si es el primer mensaje y dar la bienvenida 
if st.session_state.first_message:
    temp_message = 'Hola, ¿cómo puedo ayudarte?' 
    with st.chat_message(assistant):
        st.markdown(temp_message)
    
    st.session_state.messages.append({
        'role': assistant,
        'content': temp_message
    })
    st.session_state.first_message = False
    
    
if prompt := st.chat_input('¿Cómo puedo ayudarte?'):
    predicted_class, confidence = predict_class(prompt)
    response = get_response(predicted_class, intents)
    with st.chat_message(user):
        st.markdown(prompt)
    st.session_state.messages.append({
        'role': user,
        'content': response
    })

    with st.chat_message(assistant):
        st.markdown(response)

    st.session_state.messages.append({
        'role': assistant,
        'content': response
    })        
    
    print(f"Respuesta: {response}, Categoría: {predicted_class}, Tasa de Confianza: {confidence}")
    
        
        
