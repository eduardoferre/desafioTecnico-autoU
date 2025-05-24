from flask import Flask, request, render_template, redirect, url_for, session
import PyPDF2 # type: ignore
import nltk # type: ignore
from nltk.corpus import stopwords # type: ignore
from nltk.stem import PorterStemmer # type: ignore
import openai # type: ignore
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer # type: ignore
import io
from dotenv import load_dotenv
import os

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')


app = Flask(__name__)


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
app.secret_key = os.getenv('FLASK_SECRET_KEY')


stop_words = set(stopwords.words('portuguese'))  
stemmer = PorterStemmer()

def preProcessText(text):
    """Tokeniza, remove stopwords e aplica stemming no texto."""
    tokens = nltk.word_tokenize(text.lower())
    filtered = [stemmer.stem(w) for w in tokens if w.isalpha() and w not in stop_words]
    return " ".join(filtered)

def extractTextFile(file):
    """Extrai texto de arquivos PDF ou TXT."""
    if file.filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    elif file.filename.endswith('.txt'):
        return file.read().decode('utf-8', errors='ignore')
    else:
        raise ValueError("Formato de arquivo não suportado. Use .pdf ou .txt.")


def classifyEmail(text):
    messages = [
        {
            "role": "system",
            "content": (
                "Você é um classificador inteligente de emails que analisa o conteúdo e "
                "classifica em duas categorias: 'Produtivo' e 'Improdutivo'. "
                "Emails produtivos são aqueles que solicitam uma ação, uma resposta específica "
                "ou apresentam dúvidas técnicas, pedidos ou problemas. "
                "Emails improdutivos são mensagens de agradecimento, felicitações, "
                "informações gerais ou marketing que não requerem resposta."
            )
        },
        {
            "role": "user",
            "content": (
                "Aqui estão alguns exemplos para você entender:\n\n"
                "Email: \"Olá, gostaria de saber o status atual do meu pedido #12345. Aguardo retorno urgente.\"\n"
                "Resposta: Produtivo\n\n"
                "Email: \"Feliz Natal a todos da equipe!\"\n"
                "Resposta: Improdutivo\n\n"
                f"Agora classifique este email:\n\nEmail: \"{text}\"\nResposta:"
            )
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=5,
        n=1,
        stop=["\n"]
    )
    return response.choices[0].message['content'].strip()


def generateResponse(text, category):
    messages = [
        {"role": "system", "content": "Você é um assistente que gera respostas automáticas educadas."},
        {"role": "user", "content": f"""Gere uma resposta automática educada para um email classificado como {category}:
Email: \"\"\"{text}\"\"\"
Resposta:
Se o email for "Produtivo", forneça uma resposta direta e útil. Se for "Improdutivo", informe que não é necessário responder."""}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        temperature=0
    )
    return response.choices[0].message['content'].strip()




@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        file = request.files.get('fileUpload')
        text = request.form.get('textInput')

        email_text = ""

        if file and file.filename != '':
            email_text = extractTextFile(file)
        elif text:
            email_text = text

        if not email_text.strip():
            return render_template("index.html", error="Por favor, informe o texto do email.")

        processed_text = preProcessText(email_text)
        classification = classifyEmail(processed_text)
        response_text = generateResponse(classification, email_text)

        session['original_text'] = email_text
        session['classification'] = classification
        session['response_suggestion'] = response_text

        return render_template('resultado.html',
                               original_text=email_text,
                               classification=classification,
                               response_suggestion=response_text)

    else:  
        original_text = session.get('original_text')
        classification = session.get('classification')
        response_suggestion = session.get('response_suggestion')

        if not original_text:
            return redirect(url_for('index'))

        return render_template('resultado.html',
                               original_text=original_text,
                               classification=classification,
                               response_suggestion=response_suggestion)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)