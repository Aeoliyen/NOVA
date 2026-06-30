from pathlib import Path
from langchain_ollama import OllamaLLM


class LLMService:
    def __init__(self, model_name="qwen3:14b"):
        self.model = OllamaLLM(
            model=model_name,
            temperature=0.7,
            num_predict=120,
            keep_alive="30m"
        )

        self.personality = Path("app/config/nova_personality.txt").read_text(
            encoding="utf-8"
        )

    def ask(self, message):
        prompt = f"""
/no_think

{self.personality}

Kurallar:
- Türkçe cevap ver.
- En fazla 1-2 kısa cümle.
- Boş cevap verme.
- Asistan gibi konuşma.
- Doğal, sıcak ve samimi ol.

Kullanıcı: {message}
NOVA:
"""
        response = self.model.invoke(prompt).strip()

        if not response:
            return "Buradayım. Sadece biraz düşüncelere dalmışım."

        return response