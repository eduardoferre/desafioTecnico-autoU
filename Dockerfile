FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Baixar recursos NLTK necessários para stopwords e tokenização
RUN python -m nltk.downloader stopwords punkt

EXPOSE 5000

CMD ["python", "app.py"]
