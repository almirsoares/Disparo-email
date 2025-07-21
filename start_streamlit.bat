@echo off
echo Iniciando FastAPI (uvicorn)...
cd /d C:\Users\central\Desktop\streamlit\Disparo-email
call C:\Python39\Scripts\activate

start uvicorn src.streamlit.auth_api:app --reload --port 8001

timeout /t 5 /nobreak > nul

echo Iniciando Streamlit...
streamlit run src/streamlit/app.py --server.port 8505