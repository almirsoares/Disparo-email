import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import os
import logging

# Configurar logging para exibir mensagens no terminal
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def configurar_servidor_smtp(email_remetente, senha_app):
    """Configura e retorna uma conexão com o servidor SMTP do Gmail."""
    logger.debug(f"Tentando conectar ao SMTP com email: {email_remetente}")
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(email_remetente, senha_app)
        logger.debug("Conexão SMTP estabelecida com sucesso")
        return servidor
    except smtplib.SMTPAuthenticationError as e:
        logger.error(f"Erro de autenticação SMTP: {e}")
        raise Exception(f"Erro de autenticação: Verifique a senha de aplicativo ou habilite o acesso menos seguro. Detalhes: {e}")
    except Exception as e:
        logger.error(f"Erro ao configurar servidor SMTP: {e}")
        raise Exception(f"Erro ao conectar ao SMTP: {e}")

def criar_mensagem(email_remetente, email_destinatario, nome, assunto, corpo_email, caminho_anexo):
    """Cria e retorna uma mensagem de e-mail personalizada com anexo PDF."""
    logger.debug(f"Criando mensagem para {nome} ({email_destinatario})")
    mensagem_personalizada = corpo_email.format(nome=nome)
    mensagem = MIMEMultipart()
    mensagem['From'] = email_remetente
    mensagem['To'] = email_destinatario
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(mensagem_personalizada, 'html'))

    try:
        with open(caminho_anexo, 'rb') as arquivo:
            anexo = MIMEBase('application', 'octet-stream')
            anexo.set_payload(arquivo.read())
        encoders.encode_base64(anexo)
        anexo.add_header(
            'Content-Disposition',
            f'attachment; filename={os.path.basename(caminho_anexo)}'
        )
        mensagem.attach(anexo)
        logger.debug("Anexo adicionado com sucesso")
    except Exception as e:
        logger.error(f"Erro ao anexar o arquivo {caminho_anexo}: {e}")
        raise Exception(f"Erro ao anexar o arquivo: {e}")

    return mensagem

def enviar_emails_em_massa(df, email_remetente, senha_app, assunto, corpo_email, caminho_anexo):
    """Envia e-mails com anexo para cada destinatário no DataFrame."""
    logger.debug("Iniciando envio de e-mails em massa")
    try:
        servidor = configurar_servidor_smtp(email_remetente, senha_app)
    except Exception as e:
        logger.error(f"Falha na configuração do servidor: {e}")
        yield False, str(e)
        return

    try:
        for index, row in df.iterrows():
            try:
                nome = row['nome']
                email_destinatario = row['email']
                logger.debug(f"Enviando e-mail para {nome} ({email_destinatario})")
                mensagem = criar_mensagem(email_remetente, email_destinatario, nome, assunto, corpo_email, caminho_anexo)
                servidor.sendmail(email_remetente, email_destinatario, mensagem.as_string())
                logger.debug(f"E-mail enviado com sucesso para {nome}")
                yield True, f"E-mail com anexo enviado para {nome} ({email_destinatario})"
            except Exception as e:
                logger.error(f"Erro ao enviar e-mail para {nome}: {e}")
                yield False, f"Erro ao enviar e-mail para {nome} ({email_destinatario}): {e}"
    finally:
        logger.debug("Fechando conexão SMTP")
        servidor.quit()