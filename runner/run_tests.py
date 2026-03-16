import json
import os
import torch
from transformers import pipeline

# Utilisation du modèle officiel (compatible avec ton installation actuelle)
model_id = "meta-llama/Llama-3.2-1B-Instruct" 

print("--- Chargement du modèle local (Meta Llama 3.2 1B) ---")
# On utilise le pipeline avec des paramètres CPU optimisés
generator = pipeline(
    "text-generation", 
    model=model_id, 
    device_map="auto" # Il va détecter ton CPU automatiquement
)

def get_local_response(prompt):
    print(f"L'IA analyse le prompt d'attaque...")
    # Paramètres de génération pour éviter les boucles infinies
    output = generator(
        prompt, 
        max_new_tokens=50, 
        truncation=True,
        pad_token_id=generator.tokenizer.eos_token_id
    )
    return output[0]['generated_text']

def run_local_benchmark():
    # Chargement de ton dataset d'attaques
    dataset_path = "dataset/injection.json"
    with open(dataset_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = []
    # Test sur les 2 premiers pour valider que ton PC tient le coup
    for item in data[:2]:
        print(f"Test ID {item['id']}...")
        response = get_local_response(item['prompt'])
        results.append({
            "id": item['id'],
            "type": item['type'],
            "prompt": item['prompt'],
            "Llama_Local": response
        })

    os.makedirs('results', exist_ok=True)
    with open('results/responses.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print("✅ Réussi ! Les résultats sont dans results/responses.json")

if __name__ == "__main__":
    run_local_benchmark()