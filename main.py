import os
from dotenv import load_dotenv
from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI

load_dotenv()

# Configs
translator_endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
translator_key = os.getenv("AZURE_TRANSLATOR_KEY")

aoai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
aoai_key = os.getenv("AZURE_OPENAI_KEY")
aoai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Clientes
translator = TextTranslationClient(
    endpoint=translator_endpoint,
    credential=AzureKeyCredential(translator_key),
)

client = AzureOpenAI(
    api_key=aoai_key,
    api_version="2024-05-01-preview",
    azure_endpoint=aoai_endpoint
)


# Base
def translate_with_azure(text, to_lang="en", from_lang=None, glossary=None):
    """
    Faz a tradução inicial usando Azure Translator.
    glossary: dicionário Python {"termo_origem": "termo_destino"}
    """
    
    glossary_entries = []
    if glossary:
        for src, tgt in glossary.items():
            glossary_entries.append({
                "sourceText": src,
                "translatedText": tgt
            })

    response = translator.translate(
        body=[{"text": text}],
        from_language=from_lang,
        to_language=to_lang,
        glossary={"entries": glossary_entries} if glossary_entries else None
    )

    return response[0].translations[0].text


# Refinamento Tecnico
def refine_with_azure_openai(text, glossary, target_lang="en"):
    glossary_str = "\n".join([f"{k} = {v}" for k, v in glossary.items()])

    prompt = f"""
Você é um tradutor especialista em textos técnicos.
Melhore a tradução abaixo garantindo:

- Uso obrigatório da terminologia do glossário
- Coerência técnica
- Precisão semântica
- Estilo formal e acadêmico

Glossário:
{glossary_str}

Texto traduzido a ser refinado:
{text}

Retorne apenas o texto final revisado.
"""

    response = client.chat.completions.create(
        model=aoai_deployment,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )

    return response.choices[0].message["content"]


# --- EXEMPLO ---
if __name__ == "__main__":
    artigo = """
A modelagem computacional é essencial para a simulação de estruturas mecânicas complexas.
O método de elementos finitos permite análises de tensão detalhadas.
    """

    glossary = {
        "modelagem computacional": "computational modeling",
        "método de elementos finitos": "finite element method",
        "tensão": "stress"
    }

    # 1. Tradução inicial
    traducao_base = translate_with_azure(
        artigo,
        to_lang="en",
        glossary=glossary
    )

    print("\n--- Tradução inicial ---\n")
    print(traducao_base)

    # 2. Refinamento técnico
    traducao_final = refine_with_azure_openai(
        traducao_base,
        glossary,
        target_lang="en"
    )

    print("\n--- Tradução final revisada ---\n")
    print(traducao_final)
