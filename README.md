# Sistema de Envio de E-mails em Massa com Anexos PDF

Bem-vindo ao projeto **Sistema de Envio de E-mails em Massa com Anexos PDF**, uma solução desenvolvida em Python que utiliza a biblioteca Streamlit para oferecer uma interface web intuitiva. Este sistema permite o envio de e-mails em massa com anexos em formato PDF para uma lista de contatos a partir de um arquivo CSV, com suporte a personalização e formatação avançada.

## Visão Geral

O Sistema de Envio de E-mails em Massa com Anexos PDF foi projetado para facilitar a comunicação em massa de maneira eficiente e personalizada. Ele suporta a inclusão de anexos PDF, a personalização do corpo do e-mail com base nos nomes dos destinatários e a utilização de formatação HTML para links e outros elementos.

## Funcionalidades Principais

- Envio de e-mails em massa com personalização por destinatário utilizando o campo `nome`.
- Adição automática de arquivos PDF como anexos.
- Suporte a formatação HTML no corpo do e-mail, permitindo a inclusão de hiperlinks clicáveis.
- Interface web interativa com feedback em tempo real sobre o status do envio.
- Registro de logs no terminal para monitoramento e depuração.

## Requisitos

Antes de utilizar o projeto, verifique se os seguintes pré-requisitos estão atendidos:

- **Python 3.6 ou superior** instalado no sistema.
- Recomenda-se o uso de um ambiente virtual para gerenciar dependências.

## Instalação

Siga os passos abaixo para configurar o ambiente e instalar as dependências:

1. Clone o repositório ou baixe os arquivos do projeto:
   ```bash
   git clone https://github.com/seu-usuario/Sistema-Envio-Emails.git
   cd Sistema-Envio-Emails
   ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure sua conta Gmail:
   - Ative a Verificação em duas etapas em [Conta Google > Segurança > Verificação em duas etapas](https://myaccount.google.com/security) e gere uma senha de aplicativo em [Senhas de aplicativo](https://myaccount.google.com/security).
   - Alternativamente, desative a Verificação em duas etapas e ative a opção "Acesso de aplicativos menos seguros" (se disponível).

## Uso

1. Inicie a aplicação Streamlit:
   ```bash
   streamlit run src/streamlit/app.py
   ```
2. Acesse a interface no navegador (geralmente em `http://localhost:8501`).
3. Preencha os campos da interface:
   - **E-mail remetente**: Insira seu endereço de e-mail Gmail.
   - **Senha**: Utilize a senha de aplicativo ou a senha normal da conta (conforme configurado).
   - **Assunto**: Defina o título do e-mail.
   - **Corpo do e-mail (HTML)**: Insira o texto com `{nome}` para personalização e utilize tags HTML (ex.: `<a href="https://example.com">link</a>`).
   - **Arquivo CSV**: Faça o upload de um arquivo contendo as colunas `nome` e `email`.
   - **Arquivo PDF**: Anexe o documento PDF a ser enviado.
4. Clique em "Enviar E-mails" para iniciar o processo.

## Exemplo de Arquivo `contatos.csv`

O arquivo CSV deve seguir o formato abaixo:

```csv
nome,email
João,joao@example.com
Maria,maria@example.com
Pedro,pedro@example.com
```

## Recomendações

- **Personalização com HTML**: Utilize tags como `<b>`, `<i>` ou `<a href="...">` para formatar o corpo do e-mail.
- **Testes iniciais**: Realize envios de teste para um único destinatário antes de processar listas grandes.
- **Limitações do Gmail**: O serviço impõe um limite de aproximadamente 500 e-mails por dia. Respeite essa restrição para evitar bloqueios temporários.

## Solução de Problemas

Caso o envio de e-mails falhe, consulte os logs exibidos no terminal para identificar o problema. Erros comuns incluem:
- Falha na autenticação (verifique a senha ou as configurações de segurança do Gmail).
- Problemas de permissão ao salvar o arquivo PDF temporário.

Para suporte adicional, abra uma issue no repositório ou entre em contato via [X](https://x.com/seu-usuario) com os detalhes do erro, incluindo o stack trace, se disponível.

## Contribuições

Contribuições são bem-vindas. Para colaborar:
1. Faça um fork do repositório.
2. Adicione novas funcionalidades ou corrija bugs.
3. Envie um pull request com uma descrição clara das alterações.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE). Você pode utilizá-lo, modificá-lo e distribuí-lo, desde que respeite os termos da licença.

## Agradecimentos

Agradecemos à comunidade xAI por inspirar soluções como esta e aos desenvolvedores que contribuíram com as bibliotecas utilizadas.

---

### Instruções
- **Salve o arquivo**: Copie o conteúdo acima e salve como `README.md` na raiz do seu projeto.
- **Personalização**: Substitua `https://github.com/seu-usuario/Sistema-Envio-Emails.git` e `https://x.com/seu-usuario` pelos seus links reais, se aplicável.
- **Licença**: Adicione um arquivo `LICENSE` com o texto da Licença MIT, se ainda não o tiver.

Se precisar de mais ajustes ou adicionar seções (ex.: capturas de tela, changelog), é só me avisar!