# AzureAITranslator

🧠✨ Tradução Automática de Artigos Técnicos com Azure AI
Tradução neural + pós-edição com LLM para máxima precisão terminológica
<p align="center"> <img src="https://img.shields.io/badge/Azure%20AI-Translator-blue?logo=microsoftazure" /> <img src="https://img.shields.io/badge/Azure%20OpenAI-GPT--4o-5b5?logo=openai" /> <img src="https://img.shields.io/badge/Python-3.10+-yellow?logo=python" /> <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-green" /> </p>
📌 Sobre o Projeto

Este projeto implementa uma solução profissional de tradução automática de artigos técnicos, combinando:

Azure Translator — tradução neural de alta qualidade

Azure OpenAI (GPT-4o) — refinamento técnico e consistência terminológica

Glossário customizado — controle sobre termos críticos do domínio

O resultado é uma tradução de alta precisão, ideal para:

✔ Engenharia • ✔ Tecnologia • ✔ Medicina • ✔ Documentação Técnica
✔ Pesquisa Científica • ✔ Conteúdo Multidisciplinar

Arquitetura da Solução:

         ┌─────────────────────────┐         ┌─────────────────────────┐
         
         Artigo Técnico  --->   Azure Translator  --->  Azure OpenAI (GPT-4o)
                                • Tradução inicial     • Pós-edição 
                                • Glossário aplicado   • Terminologia precisa 
                       
                                                                 ▼
                                                       Tradução Técnica Final


🚀 Funcionalidades Principais
🔹 Tradução Neural com Azure Translator

Suporte nativo a glossários técnicos

Detecção automática de idioma

🔹 Pós-Edição com GPT-4o

Refinamento contextual

Correção de termos técnicos

Uniformização de vocabulário

🔹 Suporte a Glossários Customizados

Inclua seu próprio dicionário técnico no formato Python:

```
glossario = {
    "modelagem computacional": "computational modeling",
    "método de elementos finitos": "finite element method",
    "tensão": "stress"
}
```
📦 Instalação
1. Clone o repositório
   
```
git clone https://github.com/LPMLarica/AzureAITranslator.git
cd AzureAITranslator
```

3. Instale as dependências
pip install -r requirements.txt

4. Configure as variáveis de ambiente

Crie um arquivo .env:
```
AZURE_TRANSLATOR_ENDPOINT=https://<sua-instancia>.cognitiveservices.azure.com/
AZURE_TRANSLATOR_KEY=<sua-chave>

AZURE_OPENAI_ENDPOINT=https://<sua-instancia>.openai.azure.com/
AZURE_OPENAI_KEY=<sua-chave>
AZURE_OPENAI_DEPLOYMENT=gpt-4o
```
🧪 Como Usar
🔹 Execução simples
python main.py

🔹 No seu código Python
```
from translator_pipeline import translate_with_azure, refine_with_azure_openai

texto = "A modelagem computacional é essencial para simulações avançadas."

glossario = {
    "modelagem computacional": "computational modeling",
    "simulações": "simulations"
}

traducao_base = translate_with_azure(texto, to_lang="en", glossary=glossario)
traducao_final = refine_with_azure_openai(traducao_base, glossary=glossario)

print(traducao_final)
```
📁 Estrutura do Projeto
📦 azure-technical-translation
├── main.py
├── translator_pipeline.py
├── README.md
├── requirements.txt
└── .env.example

Tecnologias Utilizadas:

| Tecnologia               | Uso                              |
| ------------------------ | -------------------------------- |
| **Azure Translator**     | Tradução neural com glossário    |
| **Azure OpenAI GPT-4o**  | Pós-edição e refinamento técnico |
| **Python**               | Backend                          |
| **dotenv**               | Configuração segura              |
| **Azure SDK for Python** | Integração com serviços          |


Roadmap

 Tradução + refinamento técnico

 Interface Web com Streamlit

 Detectar automaticamente termos técnicos

 Validar consistência terminológica via embeddings

 Suporte a arquivos PDF e DOCX

 Deploy como API (FastAPI)

🤝 Contribuições

Contribuições são bem-vindas!
Sinta-se à vontade para abrir Issues e Pull Requests.

Distribuído sob a licença MIT.

Se este repositório te ajudou, deixe uma estrela ⭐ para apoiar!
