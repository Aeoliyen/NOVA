from memory_manager import MemoryManager

memory = MemoryManager()

memory.add_memory(
    category="project",
    content="NOVA ücretsiz, Türkçe, sesli ve ekranda yaşayan AI companion olacak.",
    importance=5
)

for item in memory.list_memories():
    print(item)