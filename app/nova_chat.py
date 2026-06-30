from llm_service import LLMService
from memory_manager import MemoryManager

llm = LLMService()
memory = MemoryManager()

print("NOVA hazır. Çıkmak için /bye yaz.\n")

while True:
    user_input = input("Sen: ")

    if user_input.strip().lower() == "/bye":
        print("NOVA: Görüşürüz.")
        break

    memory.add_memory(
        category="conversation",
        content=f"Kullanıcı dedi ki: {user_input}",
        importance=2
    )

    response = llm.ask(user_input)

    memory.add_memory(
        category="conversation",
        content=f"NOVA cevapladı: {response}",
        importance=2
    )

    print(f"NOVA: {response}\n")