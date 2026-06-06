# AI, RAG, and Agents Sessions Plan (University Graduates)

## Program Goal
Prepare near-graduation students to:
- Understand AI/LLM fundamentals clearly.
- Build practical RAG and Agent systems end-to-end.
- Deliver portfolio-ready mini-projects using free tools and datasets.

## Audience and Format
- Audience: Senior university students about to graduate.
- Session duration: 1 to 3 hours each.
- Recommended default: 2 hours per session.
- Delivery style per session:
  - 30% fundamentals
  - 20% instructor demo
  - 50% guided hands-on lab

## Free-Only Stack (for all sessions)
- Python, Jupyter, VS Code
- Local and free models: Ollama (Llama 3.x, Mistral), Hugging Face free models
- Embeddings: sentence-transformers (open-source), Hugging Face embeddings
- Vector stores: Chroma (local), FAISS (local)
- Agent frameworks: LangChain, LangGraph
- APIs (optional free tiers): OpenRouter free models or any available free provider
- UI: Streamlit or Gradio
- Evaluation: RAGAS (open-source), manual rubric-based eval sheets
- Data sources: Kaggle datasets, Hugging Face datasets, public PDFs/docs, GitHub repos

## Source Courses to Use (Primary Mapping)

### Udemy courses from E:\Learn\Udemy Courses\AI
Use these as the main content backbone:
1. AI Engineer Bootcamp 2026 LLMs, RAG, AI Agents & Vector DBs
2. LangChain- Agentic AI Engineering with LangChain & LangGraph
3. LangGraph- Develop LLM powered AI agents with LangGraph
4. Complete Agentic AI Bootcamp With LangGraph and Langchain
5. MCP Crash Course Complete Model Context Protocol in a Day
6. AI Engineer Agentic Track The Complete Agent & MCP Course

### DataCamp Slides (E:\Learn\DataCamp\Slides)
Primary slide decks mapped to sessions:
- Generative AI Concepts
- Large Language Models (LLMs) Concepts
- Introduction to LLMs in Python
- Understanding Prompt Engineering
- Prompt Engineering with the OpenAI API
- Introduction to Embeddings with the OpenAI API
- Vector Databases for Embeddings with Pinecone
- Retrieval Augmented Generation (RAG) with LangChain
- End-to-End RAG with Weaviate
- Graph RAG with LangChain and Neo4j
- Developing LLM Applications with LangChain
- Designing Agentic Systems with LangChain
- Introduction to AI Agents
- Introduction to Agent Skills
- Introduction to Subagents
- Multi-Agent Systems with LangGraph
- Building Scalable Agentic Systems
- LLMOps Concepts
- Working with Hugging Face
- Working with Llama 3
- Fine-Tuning with Llama 3
- Natural Language Processing (NLP) in Python
- Sentiment Analysis in Python
- Deploying AI into Production with FastAPI
- Responsible AI Practices
- AI Ethics

### DataCamp lab files (already in this repo)
Use these files for in-session coding labs:
- courses/datacamp/LLMs/Langchain/LangChain RAG.py
- courses/datacamp/LLMs/Langchain/LangChain Graph RAG.py
- courses/datacamp/LLMs/Langchain/LangChain Agents.py
- courses/datacamp/LLMs/Langchain/LangChain with Hugging Face.py
- courses/datacamp/LLMs/Langchain/LangChain Sequential Chains.py
- courses/datacamp/LLMs/Langchain/LangChain with Open AI.py
- courses/datacamp/LLMs/Vector Databases/Chroma DB.py
- courses/datacamp/LLMs/Open AI/Embeddings with Open AI.py
- courses/datacamp/LLMs/MCP/mcp_client.py
- courses/datacamp/LLMs/MCP/currency_mcp_server.py
- courses/datacamp/LLMs/MCP/mcp_tool.py
- courses/datacamp/LLMs/MCP/mcp_prompt.py
- courses/datacamp/LLMs/LLama/Intro to LLama.ipynb
- courses/datacamp/Natural Language Processing in Python/Introduction to Natural Language Processing in Python/
- courses/datacamp/Natural Language Processing in Python/Sentiment Analysis in Python/

## 12-Session Curriculum (1 to 3 Hours Each)

## Session 1 (1.5 to 2h): AI, LLM Foundations, and the AI Profession Landscape
Learning outcomes:
- Map the AI field: what AI is, key subfields, and current industry direction.
- Understand the 3 levels of engaging with AI as a professional.
- Explain LLM lifecycle: pretraining, instruction tuning, inference.
- Compare closed vs open models and local vs cloud usage.
- Build first prompt-based assistant.

### The 3 Levels of Learning and Working with AI
Use this framing throughout the entire course. Every session tells students which level they are operating at.

| Level | Role | What they do | Examples |
|-------|------|--------------|----------|
| Level 1: AI Coder | AI User / Prompt Engineer | Uses AI tools to speed up work, writes prompts, automates tasks | GitHub Copilot, ChatGPT, Claude Code |
| Level 2: AI Builder | AI Engineer / App Developer | Builds AI-powered products: RAG systems, agents, APIs, workflows | LangChain apps, RAG pipelines, MCP servers |
| Level 3: Model Builder | ML / AI Researcher | Trains, fine-tunes, or evaluates foundation models | Fine-tuning Llama, RLHF, custom embeddings |

This course focuses on Level 1 basics in Session 1, then shifts to Level 2 from Session 2 onward. Level 3 is introduced briefly in Sessions 1 and 10 for awareness.

### AI Professions Overview (discussion prompt for students)
- Prompt Engineer — crafts and evaluates prompts for business tasks
- AI/LLM Engineer — builds and integrates LLM-powered systems
- ML Engineer — trains and deploys machine learning models
- Data Scientist — analyzes data, builds predictive models
- AI Product Manager — translates AI capabilities into product roadmaps
- AI Safety/Ethics Researcher — evaluates risks and responsible deployment
- MLOps / AI Platform Engineer — manages model infrastructure and pipelines

Hands-on output:
- CLI mini assistant that answers domain questions from prompt templates.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 01_Introduction: course framing, what an AI engineer does, level landscape |
| Udemy | AI Engineer Bootcamp 2026 LLMs, RAG, AI Agents & Vector DBs | Section 1-2: LLM fundamentals, how LLMs work, closed vs open models |
| DataCamp Slides | Generative AI Concepts | Full deck: token generation, temperature, model families |
| DataCamp Slides | Large Language Models (LLMs) Concepts | Full deck: training pipeline, RLHF, inference |
| DataCamp Slides | Introduction to LLMs in Python | Chapters 1-2: calling models, system prompts, parameters |
| DataCamp Slides | Working with Llama 3 | Chapter 1: running local Llama models |
| DataCamp Slides | Artificial Intelligence (AI) Strategy | Opening slides: AI landscape and career paths |
| DataCamp Lab | courses/datacamp/LLMs/Langchain/LangChain with Open AI.py | Starter code for prompt-based assistant |

### Emerging Topics for Session 1
- **Reasoning models** — o1, o3, DeepSeek-R1: how chain-of-thought is baked in at training time, not just prompting
- **Small Language Models (SLMs)** — Phi-3, Gemma 2B, Qwen: capable models that run fully on a laptop
- **Multimodal models** — brief mention that modern LLMs accept images, audio, and video, not just text
- **Vibe coding tools** — Claude Code, Cursor, GitHub Copilot as Level 1 examples students already use

## Session 2 (2h): Prompt Engineering and Evaluation Basics
Learning outcomes:
- Apply prompt patterns (role, constraints, examples, output schema).
- Introduce lightweight evaluation rubric for response quality.

Hands-on output:
- Prompt test harness with 10 benchmark prompts and scoring sheet.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| Udemy | AI Engineer Bootcamp 2026 LLMs, RAG, AI Agents & Vector DBs | Prompt engineering module: zero-shot, few-shot, chain-of-thought |
| DataCamp Slides | Understanding Prompt Engineering | Full deck: prompt structure, hallucination, output formatting |
| DataCamp Slides | Prompt Engineering with the OpenAI API | Full deck: system vs user messages, structured outputs, JSON mode |
| DataCamp Slides | Introduction to LLMs in Python | Chapter 3: output parsing and evaluation |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 11_Prompt Engineering Theory: prompt anatomy, few-shot templates, CoT |
| DataCamp Lab | courses/datacamp/LLMs/Langchain/LangChain with Open AI.py | Adapt prompt templates for harness |

### Emerging Topics for Session 2
- **LLM-as-judge evaluation** — use a second LLM call to score response quality instead of manual rubrics
- **Structured outputs / JSON mode** — enforce schema-valid responses using Pydantic and tool-calling APIs
- **Prompt injection awareness** — show a live example of a prompt injection attack and discuss defenses

## Session 3 (2h): Embeddings and Vector Databases
Learning outcomes:
- Explain embeddings and semantic similarity.
- Use Chroma or FAISS for local semantic search.

Hands-on output:
- Semantic search app over public documents.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| Udemy | AI Engineer Bootcamp 2026 LLMs, RAG, AI Agents & Vector DBs | Vector DB section: embeddings, cosine similarity, Chroma/FAISS |
| DataCamp Slides | Introduction to Embeddings with the OpenAI API | Full deck: embedding vectors, distance metrics, use cases |
| DataCamp Slides | Vector Databases for Embeddings with Pinecone | Full deck: indexing, upsert, query workflows |
| DataCamp Lab | courses/datacamp/LLMs/Vector Databases/Chroma DB.py | Lab file: index docs, query by similarity |
| DataCamp Lab | courses/datacamp/LLMs/Open AI/Embeddings with Open AI.py | Embedding generation with free models adapter |

### Emerging Topics for Session 3
- **Hybrid search** — combine dense (embedding) and sparse (BM25 keyword) retrieval for better recall; supported by Weaviate and Qdrant
- **Late interaction models** — ColBERT: token-level similarity instead of single-vector comparison
- **Matryoshka embeddings** — embeddings that can be truncated to save storage with minimal quality loss

## Session 4 (2 to 2.5h): RAG Fundamentals (Classic RAG)
Learning outcomes:
- Build ingestion pipeline: load, split, embed, store, retrieve.
- Tune chunk size, overlap, and top-k retrieval.

Hands-on output:
- End-to-end local RAG chatbot for a chosen public dataset.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| Udemy | AI Engineer Bootcamp 2026 LLMs, RAG, AI Agents & Vector DBs | RAG section: document loaders, text splitters, retrieval chain |
| DataCamp Slides | Retrieval Augmented Generation (RAG) with LangChain | Full deck: ingestion pipeline, RetrievalQA, prompt with context |
| DataCamp Slides | End-to-End RAG with Weaviate | Chapters 1-3: chunking strategies, retrieval quality, evaluation |
| DataCamp Lab | courses/datacamp/LLMs/Langchain/LangChain RAG.py | Core lab: full RAG pipeline from scratch |
| DataCamp Lab | courses/datacamp/LLMs/Vector Databases/Chroma DB.py | Vector store setup for RAG |

### Emerging Topics for Session 4
- **Contextual retrieval** — Anthropic's technique: prepend a chunk-level summary generated by an LLM before embedding to improve retrieval accuracy
- **Long-context models and RAG** — Gemini 1.5 / GPT-4o 128k: when is RAG still needed vs. just stuffing the full document?
- **Streaming responses** — stream LLM output token-by-token for better perceived latency in real apps

## Session 5 (2h): Advanced RAG and Graph RAG Concepts
Learning outcomes:
- Explain limitations of classic RAG.
- Introduce Graph RAG idea, citation grounding, and retrieval strategies.

Hands-on output:
- Improved RAG with metadata filtering and citation display.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | Advanced RAG module: HyDE, re-ranking, parent-child chunking |
| Udemy | AI Engineer Bootcamp 2026 LLMs, RAG, AI Agents & Vector DBs | Advanced RAG: multi-query retriever, contextual compression |
| DataCamp Slides | Graph RAG with LangChain and Neo4j | Full deck: knowledge graph construction, entity linking, Cypher queries |
| DataCamp Slides | End-to-End RAG with Weaviate | Chapter 4: evaluation and hallucination mitigation |
| DataCamp Lab | courses/datacamp/LLMs/Langchain/LangChain Graph RAG.py | Lab: Graph RAG pipeline with citation |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 16_Agentic RAG: combining retrieval with agent decision-making |
| External reference | courses/knowledge-graphs-deeplearningai/ | Deep Learning.ai knowledge graph notebooks for visual explanation |

### Emerging Topics for Session 5
- **Multimodal RAG** — retrieve and reason over images alongside text (e.g., product images + descriptions)
- **RAPTOR** — recursive abstractive processing: build a tree of summaries for hierarchical retrieval
- **Corrective RAG (CRAG)** — agent decides whether retrieved docs are good enough or triggers a web search fallback

## Session 6 (2h): LangChain for Orchestrating LLM Apps
Learning outcomes:
- Use chains, prompt templates, memory, and output parsers.
- Build multi-step workflows.

Hands-on output:
- Multi-step pipeline: summarize -> classify -> actionable recommendations.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | Core LangChain: LCEL, RunnableSequence, memory, output parsers |
| DataCamp Slides | Developing LLM Applications with LangChain | Full deck: chains, prompt templates, memory types, parsers |
| DataCamp Slides | Designing Agentic Systems with LangChain | Chapters 1-2: routing chains, conditional logic |
| DataCamp Lab | courses/datacamp/LLMs/Langchain/LangChain Sequential Chains.py | Lab: multi-step chain pipeline |
| DataCamp Lab | courses/datacamp/LLMs/Langchain/LangChain with Hugging Face.py | Swap OpenAI for free HF models in the pipeline |

### Emerging Topics for Session 6
- **LangChain Expression Language (LCEL)** — modern declarative pipeline syntax replacing legacy chain classes
- **Pydantic output parsers** — enforce typed, validated structured output from any LLM response
- **Observability with Langfuse** — free open-source tracing for LLM calls, latency, and cost tracking

## Session 7 (2 to 3h): AI Agents Fundamentals
Learning outcomes:
- Understand tools, planning, action loops, and guardrails.
- Compare workflows vs autonomous agents.

Hands-on output:
- Tool-using agent with web/file/calculator tools (free APIs only).

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| Udemy | Complete Agentic AI Bootcamp With LangGraph and Langchain | Agent intro: ReAct pattern, tool calling, action-observation loop |
| Udemy | AI Engineer Agentic Track The Complete Agent & MCP Course | Chapter 1-3: agent anatomy, tool design, stopping conditions |
| DataCamp Slides | Introduction to AI Agents | Full deck: agent types, planning, tool use, memory |
| DataCamp Slides | Introduction to Agent Skills | Full deck: skill design, tool schemas, error handling |
| DataCamp Slides | Designing Agentic Systems with LangChain | Full deck: agent executor, tool binding, guardrails |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 03_THE GIST Of AI Agents: mental model for agents, planning, action loop |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 04_Agents Under The Hood: internals, trace walkthrough, debugging |
| DataCamp Lab | courses/datacamp/LLMs/Langchain/LangChain Agents.py | Core lab: build a tool-calling agent from scratch |

### Emerging Topics for Session 7
- **Computer use / browser agents** — agents that control a browser or desktop UI (Anthropic Computer Use, Playwright-based agents)
- **Multimodal tool use** — agents that can read screenshots or diagrams as part of their decision loop
- **OpenAI Responses API** — new stateful API that manages conversation context and tool calls server-side

## Session 8 (2 to 3h): LangGraph Multi-Agent Patterns
Learning outcomes:
- Build stateful graph-based agent workflows.
- Implement retry, branching, and human-in-the-loop checkpoints.

Hands-on output:
- Two-agent workflow (researcher + writer) with review loop.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| Udemy | LangGraph- Develop LLM powered AI agents with LangGraph | Full course: StateGraph, nodes, edges, conditional routing, checkpointers |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | LangGraph module: supervisor pattern, human-in-the-loop |
| Udemy | Complete Agentic AI Bootcamp With LangGraph and Langchain | Multi-agent orchestration sections |
| DataCamp Slides | Multi-Agent Systems with LangGraph | Full deck: graph topology, agent communication, state sharing |
| DataCamp Slides | Building Scalable Agentic Systems | Chapters 1-2: fault tolerance, retry logic, scalability patterns |
| DataCamp Slides | Introduction to Subagents | Full deck: subagent invocation, delegation, result aggregation |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 14_Reflection Agent: self-critique loop pattern |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 15_Reflexion Agent: memory + reflection combined pattern |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 21_Deep Agents: advanced multi-agent architectures and patterns |

### Emerging Topics for Session 8
- **Long-term agent memory** — mem0, Zep, or custom vector-based memory stores that persist across sessions
- **Agent checkpointing** — save and resume graph state so long tasks survive failures or user interruptions
- **Mixture-of-Agents** — route sub-tasks to specialised models rather than one general-purpose LLM

## Session 9 (2h): MCP for Tool Integration
Learning outcomes:
- Understand MCP architecture (client, server, tools, resources).
- Expose local tools safely to LLM applications.

Hands-on output:
- Minimal MCP server + MCP client that calls one custom tool.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| Udemy | MCP Crash Course Complete Model Context Protocol in a Day | Full course: MCP spec, server setup, tool registration, client calls |
| Udemy | AI Engineer Agentic Track The Complete Agent & MCP Course | MCP chapters: resources, prompts, transport layers |
| DataCamp Lab | courses/datacamp/LLMs/MCP/currency_mcp_server.py | Example MCP server to dissect and extend |
| DataCamp Lab | courses/datacamp/LLMs/MCP/mcp_client.py | Example MCP client to test against the server |
| DataCamp Lab | courses/datacamp/LLMs/MCP/mcp_tool.py | Tool registration pattern |
| DataCamp Lab | courses/datacamp/LLMs/MCP/mcp_prompt.py | Prompt resource pattern |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 17_Introduction to MCP: spec overview, transport, message flow |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 19_Building MCP Servers and Clients with LangChain: end-to-end build |

### Emerging Topics for Session 9
- **MCP ecosystem growth** — 1000+ public MCP servers (GitHub, Postgres, browser, email); show the registry
- **Agent-to-agent (A2A) protocol** — Google's emerging standard for agents calling other agents across systems
- **Tool sandboxing** — running tool code in isolated environments (Docker, e2b) to prevent side effects

## Session 10 (2h): Safety, Guardrails, and Cost/Latency Optimization
Learning outcomes:
- Apply prompt and tool guardrails.
- Track latency and token usage.
- Add fallback models and caching.

Hands-on output:
- Safer agent pipeline with basic monitoring metrics.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| Udemy | AI Engineer Bootcamp 2026 LLMs, RAG, AI Agents & Vector DBs | Production section: rate limits, fallbacks, caching, streaming |
| Udemy | Complete Agentic AI Bootcamp With LangGraph and Langchain | Safety module: output validation, guardrails, error handling |
| DataCamp Slides | LLMOps Concepts | Full deck: model lifecycle, monitoring, drift, incident response |

### Emerging Topics for Session 10
- **Prompt injection defences** — input sanitisation, privilege separation, and output validation patterns
- **LLM observability tools** — Langfuse (free/open-source), Phoenix by Arize, LangSmith free tier: tracing, span cost, error rates
- **EU AI Act awareness** — brief intro to which AI systems are high-risk and what compliance looks like for builders
- **Model distillation** — compress a large teacher model into a smaller student for cheaper inference in production
| DataCamp Slides | Responsible AI Practices | Full deck: bias, fairness, safety patterns |
| DataCamp Slides | AI Ethics | Chapters on responsible deployment and student discussion prompts |
| DataCamp Slides | Building Scalable Agentic Systems | Chapter 3: cost control, latency profiling, batching |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 12_LLM Applications In Production: reliability, retries, observability |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 26_Agent Security: prompt injection, tool misuse, sandboxing |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 27_The Dark Side of Vibe Coding: AI-generated code vulnerabilities |

| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 27_The Dark Side of Vibe Coding: AI-generated code vulnerabilities |

## Session 11 (2 to 2.5h): Fine-Tuning LLMs with OpenPipe
Learning outcomes:
- Understand when fine-tuning beats prompt engineering and RAG.
- Collect, clean, and format a fine-tuning dataset (JSONL chat format).
- Fine-tune a model using OpenPipe's free tier and evaluate the result.
- Swap the fine-tuned endpoint into an existing LangChain chain.

### When to Fine-Tune vs RAG vs Prompting

| Technique | Best for | Cost | Effort |
|-----------|----------|------|--------|
| Prompt engineering | Style, tone, general tasks | Low | Low |
| RAG | Grounding answers in fresh/private docs | Medium | Medium |
| Fine-tuning | Consistent format, domain jargon, task specialisation | Medium | High |
| Fine-tuning + RAG | Production domain apps needing both accuracy and freshness | Higher | High |

### What is OpenPipe?
- OpenPipe (openpipe.ai) is a platform for collecting LLM call logs, curating datasets from them, and fine-tuning smaller open-source models.
- Free tier: log up to 1000 requests/month, fine-tune Mistral or Llama-based models.
- Drop-in OpenAI-compatible API endpoint — swap the base URL in any existing LangChain app.
- Key advantage over raw Hugging Face fine-tuning: no GPU required, dataset curation UI included.

Hands-on output:
- Fine-tuned model on a 50–100 pair domain dataset deployed behind an OpenAI-compatible endpoint, integrated into a LangChain chain with before/after comparison.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| DataCamp Slides | Fine-Tuning with Llama 3 | Full deck: fine-tuning concepts, LoRA/QLoRA, dataset format, evaluation |
| DataCamp Slides | Working with Llama 3 | Chapter 3: model variants and when to use each size |
| DataCamp Slides | LLMOps Concepts | Dataset versioning, model registry, deployment lifecycle |
| External | openpipe.ai docs | Dataset upload (JSONL), fine-tune job, endpoint usage |
| DataCamp Lab | courses/datacamp/LLMs/LLama/Intro to LLama.ipynb | Base Llama usage to compare against fine-tuned version |

### Lab Steps
1. Pick a domain: customer support, code review, or medical FAQ.
2. Generate or collect 50–100 (prompt, ideal_response) pairs — use ChatGPT/Claude to speed this up.
3. Format as JSONL with `{"messages": [{"role": "user", ...}, {"role": "assistant", ...}]}`.
4. Upload to OpenPipe, launch a fine-tune job on Mistral-7B or similar.
5. Call the fine-tuned endpoint via the OpenAI-compatible URL in LangChain.
6. Run both base and fine-tuned models on 10 held-out prompts, score with LLM-as-judge.
7. Present a comparison table: base vs fine-tuned on accuracy, format adherence, and latency.

### Emerging Topics for Session 11
- **LoRA / QLoRA** — parameter-efficient fine-tuning methods that reduce GPU memory by training only low-rank adapter weights
- **Direct Preference Optimisation (DPO)** — fine-tune on preference pairs (preferred vs rejected) instead of pure supervised data; OpenPipe supports this
- **Distillation via fine-tuning** — use a large teacher model (GPT-4o) to generate the training labels, then fine-tune a smaller cheap model to replicate its behaviour
- **Function-calling fine-tuning** — teach a model to reliably emit structured tool-call JSON; critical for reliable agent tool use

## Session 12 (1.5 to 2h): Demo Day and Career Readiness
Learning outcomes:
- Design and implement a complete AI app in teams.
- Prepare technical demo and architecture explanation.

Hands-on output (team project):
- One of the capstones listed below, with README and demo script.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| Udemy | Any previously covered course | Revisit relevant sections for the chosen capstone track |
| DataCamp Slides | Deploying AI into Production with FastAPI | Full deck: serving models, REST endpoints, async handling |
| DataCamp Slides | Building Scalable Agentic Systems | Architecture patterns for the build sprint |
| DataCamp Lab | Any repo lab file | Use as starter template and adapt for capstone |
| Existing projects | projects/agents/ecommerce-agent/, projects/agents/ai-job-search/ | Reference implementations in this repo for inspiration and code patterns |

## Session 12 (1.5 to 2h): Demo Day and Career Readiness
Learning outcomes:
- Present project architecture and trade-offs.
- Explain model, retrieval, and agent design decisions.
- Position project for portfolio and interviews.

Hands-on output:
- Final demo, short technical report, and CV-ready project bullets.

Sources:

| Type | Course | Sections to use |
|------|--------|-----------------|
| DataCamp Slides | LLMOps Concepts | Monitoring and lifecycle slides as talking points |
| DataCamp Slides | Responsible AI Practices | Safety and ethics slide for demo discussion |
| Udemy | AI Engineer Bootcamp 2026 LLMs, RAG, AI Agents & Vector DBs | Final project walkthroughs as demo structure reference |
| DataCamp Slides | AI Security and Risk Management | Slides to prompt students to address risk in their presentations |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 24_Industry Insights: Building Production Agents with Assaf Elovic |
| Udemy | LangChain- Agentic AI Engineering with LangChain & LangGraph | 25_Industry Insights: Building Production Agents with Roy Miara |

## Capstone Project Ideas (Free Resources)
1. University Knowledge Assistant
- RAG over university policies, course guides, and FAQs.
- Stretch goal: add agent that routes to relevant documents and cites sources.

2. Graduate Job Search Agent
- Multi-agent flow: role analyzer, CV bullet improver, company researcher.
- Data from public job posts and company pages.

3. Research Paper Companion
- Upload public papers, summarize sections, answer citation-grounded questions.
- Add evaluation checklist for hallucination risk.

4. Local Business Intelligence Copilot
- Ingest open CSV datasets, generate insights and charts.
- Agent suggests next analysis questions.

5. MCP Tool Hub Demo
- Build custom MCP server exposing calculator, CSV query, and FAQ lookup tools.
- Client agent decides which tool to call per user query.

## Weekly Schedule Options

Option A (6 weeks, 2 sessions/week)
- Week 1: Sessions 1-2
- Week 2: Sessions 3-4
- Week 3: Sessions 5-6
- Week 4: Sessions 7-8
- Week 5: Sessions 9-10
- Week 6: Sessions 11-12

Option B (12 weeks, 1 session/week)
- One session each week with homework mini-lab.

## Session Template (Use Every Time)
- 0:00 to 0:10: Recap and outcomes
- 0:10 to 0:35: Core concepts
- 0:35 to 0:55: Live demo
- 0:55 to 1:35: Guided lab
- 1:35 to 1:50: Team challenge
- 1:50 to 2:00: Debrief and assignment

(Extend or compress proportionally for 1h or 3h slots.)

## Assessment and Deliverables
- 40% hands-on labs (individual)
- 40% capstone project (team)
- 20% technical presentation and reflection

Required artifacts:
- Working code repository
- README with architecture diagram
- Evaluation notes (quality, latency, failure cases)
- Short demo video (3 to 5 minutes)

## Instructor Preparation Checklist
- Pre-download open-source models (or verify free API alternatives)
- Prepare datasets and starter notebooks
- Validate all demos run on low-resource machines
- Keep fallback path: CPU-only + smaller model + reduced chunk sizes
- Prepare grading rubric and demo-day scoring sheet

## Recommended Immediate Start
If you want a fast launch, start with this 4-session pilot:
1. Session 1 (Foundations)
2. Session 3 (Embeddings + Vector DB)
3. Session 4 (RAG)
4. Session 7 (Agents)

This pilot gives students a complete arc from fundamentals to working AI systems quickly.
