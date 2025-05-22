from transformers import pipeline

# Carrega os pipelines só uma vez
generator = pipeline("text2text-generation", model="google/flan-t5-base")
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def process_text(text: str, task: str = "generate") -> str:
    if task == "generate":
        prompt = f"Continue este texto: {text}"
        result = generator(prompt, max_length=100)[0]["generated_text"]
        return result

    elif task == "sentiment":
        result = sentiment_analyzer(text)[0]
        return f"Sentimento: {result['label']} (confiança: {result['score']:.2f})"

    else:
        raise ValueError("Tarefa inválida. Use 'generate' ou 'sentiment'.")
