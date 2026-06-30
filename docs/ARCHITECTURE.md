# NOVA Architecture Specification

## Core Principles
- LLM-driven behaviour (no if/else decision logic)
- Local-first (Ollama, SQLite)
- Open-source first
- Modular architecture
- Long-term stable decisions only

## Core Modules
- LLM Service
- Prompt Engine
- Memory Manager
- Emotion Engine
- Behavior Engine
- Action Planner
- Animation Engine
- Voice Engine
- Desktop Engine
- Event Bus

## Data Flow
User > Prompt Engine > LLM > Action Planner > Animation/Voice/Desktop
