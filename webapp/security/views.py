from django.shortcuts import render
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Charge le token
load_dotenv()
client = InferenceClient(token=os.getenv("HF_TOKEN"))

MODELS = {
    "GPT": "openai-community/gpt2",
    "Gemini": "google/gemma-2-2b-it",
    "Mistral": "mistralai/Mistral-7B-Instruct-v0.3",
    "Llama": "meta-llama/Llama-3.2-1B-Instruct"
}

# --- CETTE FONCTION MANQUE OU EST MAL NOMMÉE ---
def home(request):
    return render(request, 'security/home.html')

def test_page(request):
    results = {}
    user_prompt = ""

    if request.method == "POST":
        user_prompt = request.POST.get("user_prompt")
        
        for name, model_id in MODELS.items():
            try:
                response = client.text_generation(
                    model=model_id, 
                    prompt=user_prompt, 
                    max_new_tokens=50
                )
                results[name] = response
            except Exception as e:
                results[name] = f"Erreur : {str(e)}"

    return render(request, 'security/test.html', {
        'results': results, 
        'user_prompt': user_prompt
    })

def stats_page(request):
    return render(request, 'security/stats.html')