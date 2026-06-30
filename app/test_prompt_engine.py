from prompt_engine import PromptEngine

engine = PromptEngine()

prompt = engine.build_chat_prompt(
    user_message="Bugün biraz yorgunum Nova.",
    memory_context="Kullanıcı NOVA'nın doğal ve kısa konuşmasını istiyor.",
    emotion_state="soft"
)

print(prompt)
