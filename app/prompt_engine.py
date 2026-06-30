from pathlib import Path


class PromptEngine:
    def __init__(self):
        self.personality_path = Path("app/config/personality.md")
        self.rules_path = Path("app/config/response_rules.md")

    def load_text(self, path):
        return path.read_text(encoding="utf-8").strip()

    def build_chat_prompt(self, user_message, memory_context="", emotion_state="calm"):
        personality = self.load_text(self.personality_path)
        rules = self.load_text(self.rules_path)

        return f"""
{personality}

{rules}

Mevcut duygu durumu: {emotion_state}

Hafıza bağlamı:
{memory_context}

Kullanıcı: {user_message}
NOVA:
""".strip()
