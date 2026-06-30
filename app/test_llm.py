from llm_service import LLMService

nova = LLMService()

cevap = nova.ask("Merhaba NOVA, beni duyuyor musun?")

print(cevap)