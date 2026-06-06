# AI, RAG & Agents — Sessions Overview

11 sessions | 1.5–3h each | Free tools only (Ollama, LangChain, Chroma, HuggingFace, OpenPipe)
Each session ends with a portfolio-ready project you can ship and put on your CV.

---

**Session 1 (1.5–2h): AI & LLM Foundations + AI Profession Landscape**
🛠 Build: **Domain Expert CLI Assistant** — a Streamlit chat app backed by a local Ollama model that answers questions in a chosen domain (medicine, law, finance). Swap the system prompt to change domain without touching code.
📌 CV line: *"Built a local LLM-powered domain assistant using Ollama and Streamlit with configurable system prompts"*

**Session 2 (2h): Prompt Engineering & Evaluation**
🛠 Build: **AI Quality Evaluator** — automated LLM-as-judge pipeline that scores 20 responses across correctness, tone, and safety, exports a CSV report, and flags regressions when a prompt changes.
📌 CV line: *"Designed an automated LLM evaluation harness using chain-of-thought prompting and structured JSON scoring"*

**Session 3 (2h): Embeddings & Vector Databases**
🛠 Build: **Semantic Job-CV Matcher** — embed a set of job descriptions and a CV, rank the best matches by cosine similarity, and highlight the skill gaps between them.
📌 CV line: *"Built a semantic job-matching engine using sentence-transformers and Chroma vector store"*

**Session 4 (2–2.5h): RAG Fundamentals**
🛠 Build: **Personal Knowledge Base Chatbot** — ingest your own PDFs/notes, chunk and embed them into Chroma, and chat with them through a Gradio UI backed by a local Llama model.
📌 CV line: *"Developed an end-to-end RAG system over private documents with LangChain, Chroma, and Llama 3"*

**Session 5 (2h): Advanced RAG & Graph RAG**
🛠 Build: **Research Assistant with Source Grounding** — advanced RAG that uses HyDE query expansion, re-ranks retrieved chunks, and returns answers with clickable source citations and confidence scores.
📌 CV line: *"Implemented advanced RAG with HyDE, cross-encoder re-ranking, and citation-grounded responses"*

**Session 6 (2h): LangChain — Orchestrating LLM Apps**
🛠 Build: **Automated Content Pipeline** — LCEL chain that takes a URL, scrapes the page, summarises it, classifies its topic, generates 3 social media posts, and writes an email draft — all in one run.
📌 CV line: *"Built a multi-step LLM content automation pipeline using LangChain LCEL with structured output validation"*

**Session 7 (2–3h): AI Agents Fundamentals**
🛠 Build: **Financial Research Agent** — ReAct agent with tools: web search (DuckDuckGo free API), Wikipedia lookup, and a calculator. Given a company name it researches, computes ratios, and writes a one-page brief.
📌 CV line: *"Built a ReAct financial research agent with live web search, Wikipedia, and calculation tools using LangChain"*

**Session 8 (2–3h): LangGraph — Multi-Agent Patterns**
🛠 Build: **AI Newsletter Generator** — LangGraph workflow with three specialised agents: Researcher (searches and summarises topics), Writer (drafts the newsletter), and Editor (critiques and rewrites until quality threshold is met).
📌 CV line: *"Engineered a LangGraph multi-agent newsletter system with supervisor routing, reflection loops, and human-in-the-loop review"*

**Session 9 (2h): MCP — Model Context Protocol**
🛠 Build: **Personal Productivity MCP Server** — MCP server exposing 3 tools: read/write local task list, query a local SQLite knowledge base, and fetch calendar events from a CSV. Any MCP-compatible client (Claude Desktop, Cursor) can use it.
📌 CV line: *"Developed an MCP server in Python exposing local productivity tools to LLM clients following the Model Context Protocol spec"*

**Session 10 (2h): Safety, Guardrails & Production Readiness**
🛠 Build: **Production-Grade Agent with Observability** — take the Session 7 or 8 agent, add: input/output guardrails (Pydantic), prompt injection detection, Langfuse tracing, fallback to a smaller model on timeout, and a live metrics dashboard.
📌 CV line: *"Hardened an LLM agent for production with guardrails, prompt injection defences, observability tracing, and graceful model fallback"*

**Session 11 (2–2.5h): Fine-Tuning LLMs with OpenPipe**
🛠 Build: **Domain-Specific Fine-Tuned Model** — collect a dataset of 50–100 prompt/response pairs for a domain (customer support, code review, or medical triage), fine-tune a base model via OpenPipe's free tier, compare its outputs against the base model, and deploy the fine-tuned endpoint inside a LangChain chain.
📌 CV line: *"Fine-tuned an LLM on a custom domain dataset using OpenPipe, achieving measurably higher accuracy than the base model on targeted tasks"*
