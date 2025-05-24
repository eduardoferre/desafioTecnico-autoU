# Projeto: Classificador Automático de Emails com Resposta Automática

## Descrição

Este projeto consiste em uma aplicação web para automatizar a classificação e resposta de emails recebidos por uma empresa do setor financeiro. O sistema identifica se um email é **produtivo** (requere ação ou resposta específica) ou **improdutivo** (não necessita de ação, como mensagens de agradecimento ou felicitações) e sugere respostas automáticas adequadas para cada caso.

O objetivo principal é liberar a equipe da empresa do trabalho manual de triagem e resposta, aumentando a eficiência operacional.

---

### **Acesse a aplicação online**

Acesse a aplicação de classificação de emails no seguinte link:

🔗 [**Classificador de Emails - Deploy no Render**](https://desafiotecnico-autou.onrender.com/)

---



## Funcionalidades

- Upload de emails em formato PDF ou TXT, ou inserção direta do texto do email.
- Pré-processamento do texto com técnicas básicas de NLP (tokenização, remoção de stopwords, stemming).
- Classificação automática dos emails em **Produtivo** ou **Improdutivo** usando modelo de IA.
- Geração de respostas automáticas educadas e adequadas baseadas na classificação.
- Interface web amigável com feedback visual de carregamento durante o processamento.
- Deploy em container Docker para fácil implantação e escalabilidade.

---

## Tecnologias Utilizadas

### Backend

- **Python 3.10**  
  Linguagem principal para desenvolvimento do backend.

- **Flask**  
  Microframework web para criação da API e renderização dos templates HTML.

- **NLTK**  
  Biblioteca de processamento de linguagem natural usada para pré-processamento do texto (tokenização, stopwords, stemming).

- **OpenAI API**  
  Uso do modelo `gpt-3.5-turbo` via endpoint `ChatCompletion` para:
  - Classificação inteligente dos emails.
  - Geração de respostas automáticas.

- **PyPDF2**  
  Biblioteca para extração de texto de arquivos PDF enviados.

- **python-dotenv**  
  Para carregar variáveis de ambiente sensíveis, como chaves da API e chave secreta do Flask.

### Frontend

- **HTML5 + Bootstrap 5.3**  
  Interface responsiva e estilizada com componentes prontos, incluindo spinner de carregamento.

- **JavaScript (vanilla)**  
  Validação do formulário, alternância de campos (upload/texto), controle do loader e desabilitação do botão submit para melhor UX.

### Infraestrutura

- **Docker**  
  Containerização do aplicativo para facilitar o deploy e garantir ambiente consistente.

- **Render.com (sugestão para deploy)**  
  Plataforma de nuvem que suporta deploy de containers Docker com plano gratuito, facilitando a publicação pública do serviço.

---

## Estrutura do Projeto

```
├── app.py                  # Código principal Flask backend
├── Dockerfile              # Container Docker para a aplicação
├── docker-compose.yml      # Configuração do Docker Compose
├── requirements.txt        # Dependências Python
├── .env                    # Variáveis de ambiente (não versionado)
├── static/
│   ├── css/
│   │   └── style.css       # Estilos personalizados
│   │   └── result.css      # Estilos personalizados
│   ├── js/
│   │   └── main.js      
│   │   └── result.js      
│   └── image/
│       └── icone.svg       # Icone E-mail
├── templates/
│   ├── index.html          # Página inicial/formulário
│   └── resultado.html      # Página de resultados/classificação
└── README.md               # Documentação do projeto
```

---

## Como rodar localmente

1. Clone o repositório.

2. Configure o arquivo `.env` com suas chaves:

```
OPENAI_API_KEY=your_openai_api_key_here
FLASK_SECRET_KEY=your_flask_secret_key_here
```

3. Certifique-se de ter o Docker, Python e suas dependências instaladas.

4. Execute o comando para construir e rodar o container:

```bash
docker-compose up --build
```

5. Acesse a aplicação em `http://localhost:5000`.

---

## Como fazer deploy

- Configure seu repositório com Dockerfile.
- Use plataformas como Render, Fly.io, Railway ou Google Cloud Run para deploy com Docker.
- Configure variáveis de ambiente na plataforma para as chaves secretas.
- Faça push no repositório conectado para deploy automático.

---

## Contato

Para dúvidas ou contribuições, entre em contato.

---
