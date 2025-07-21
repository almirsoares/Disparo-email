import streamlit as st
import pandas as pd
import os
import sys
import requests

# Adicionar o diretório src ao caminho de busca
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.send_email import send

# Configurações iniciais
st.set_page_config(
    page_title='Disparo de email',
    page_icon="📧",
    layout='centered',
    menu_items={
        'Get Help': 'https://wa.me/5581997293669',
        'Report a bug': 'https://wa.me/5581997293669',
    },
)

API_URL = "http://localhost:8001"

def login(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f"{API_URL}/login", data=data)
    if response.status_code == 200:
        return response.json()['access_token']
    return None

def main():

    if 'token' not in st.session_state:
        st.session_state.token = None

    if st.session_state.token is None:
        st.title("Login")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            token = login(username, password)
            if token:
                st.session_state.token = token
                st.success(f"Bem-vindo, {username}!")
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos.")
    else:
        if st.button("Sair"):
            st.session_state.token = None
            st.rerun()

    
        st.title("Envio de E-mails em Massa com Anexo PDF")
        st.write("Preencha os campos abaixo para enviar e-mails com anexo para uma lista de contatos. Use HTML para links (ex.: <a href='https://example.com'>clique aqui</a>).")

        with st.form("email_form"):
            email_remetente = st.text_input("E-mail remetente", placeholder="seu_email@gmail.com")
            senha_app = st.text_input("Senha de aplicativo", type="password")
            assunto = st.text_input("Assunto do e-mail")
            corpo_email = st.text_area("Corpo do e-mail (HTML)")
            csv_file = st.file_uploader("Carregar arquivo CSV com contatos (colunas: nome, email)", type="csv")
            pdf_file = st.file_uploader("Carregar arquivo PDF para anexo", type="pdf")
            submit_button = st.form_submit_button("Enviar E-mails")

        if submit_button:
            if not all([email_remetente, senha_app, assunto, corpo_email, csv_file, pdf_file]):
                st.error("Por favor, preencha todos os campos e faça upload dos arquivos.")
                return

            # Salvar o arquivo PDF temporariamente
            caminho_anexo = "DTEL - COMUNICADO AJUSTE DE PRECO.pdf"
            try:
                with open(caminho_anexo, "wb") as f:
                    f.write(pdf_file.read())
            except Exception as e:
                st.error(f"Erro ao salvar o arquivo PDF temporário: {e}")
                return

            # Ler o CSV como DataFrame
            try:
                df = pd.read_csv(csv_file)
                if 'nome' not in df.columns or 'email' not in df.columns:
                    st.error("O arquivo CSV deve conter as colunas 'nome' e 'email'.")
                    return
            except Exception as e:
                st.error(f"Erro ao ler o arquivo CSV: {e}")
                return

            # Enviar os e-mails
            with st.spinner("Enviando e-mails..."):
                try:
                    for success, message in send.enviar_emails_em_massa(df, email_remetente, senha_app, assunto, corpo_email, caminho_anexo):
                        if success:
                            st.success(message)
                        else:
                            st.warning(message)
                except Exception as e:
                    st.error(f"Erro durante o envio dos e-mails: {e}")
                    import traceback
                    st.text(traceback.format_exc())  # Mostra o stack trace no Streamlit

            # Remover o arquivo PDF temporário
            if os.path.exists(caminho_anexo):
                try:
                    os.remove(caminho_anexo)
                except Exception as e:
                    st.error(f"Erro ao remover o arquivo temporário: {e}")

if __name__ == "__main__":
    main()