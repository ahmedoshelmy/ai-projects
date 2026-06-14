# Ollama Cloud Model Testing Results

Total Models Tested: 39 | Successful: 23 | Failed: 16

## Successful Models

| Model | Latency (s) | Input Tokens | Output Tokens | Total Tokens | Sample Response |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `minimax-m3:cloud` | 3.24s | 177 | 84 | 261 | Hi there! 👋 Welcome! I'm here to help you with whatever you need. Whether it's answering questions, brainstorming ideas, writing, learning something new, or just having a conversation—I'm ready to assist.  What can I do for you today? |
| `nemotron-3-ultra:cloud` | 2.15s | 18 | 29 | 47 | Hi there! How can I help you today? |
| `gemma4:31b-cloud` | 2.64s | 14 | 10 | 24 | Hello! How can I help you today? |
| `nemotron-3-super:cloud` | 2.66s | 18 | 237 | 255 | Hello! 👋 How can I assist you today? Whether you have a question, need help with something, or just want to chat—I'm here for you! What's on your mind? |
| `glm-4.7:cloud` | 8.17s | 6 | 233 | 239 | Hi there! I'm the GLM language model trained by Z.ai. How can I assist you today? Whether you have questions, need information, or just want to chat, I'm happy to help. What would you like to discuss? |
| `minimax-m2.1:cloud` | 1.44s | 39 | 63 | 102 | Hi there! 👋  I'm here to help you with coding tasks, technical questions, or anything else you need assistance with. What can I help you with today? |
| `gpt-oss:20b-cloud` | 1.21s | 68 | 40 | 108 |  |
| `gpt-oss:120b-cloud` | 1.28s | 68 | 43 | 111 | Hello! 👋 How can I assist you today? |
| `qwen3-coder:480b-cloud` | 1.60s | 9 | 10 | 19 | Hello! How can I help you today? |
| `qwen3-vl:235b-cloud` | 4.35s | 11 | 173 | 184 | Hello! How can I assist you today? 😊 |
| `qwen3-vl:235b-instruct-cloud` | 1.51s | 9 | 34 | 43 | Hello! 👋 How can I assist you today? Whether you have a question, need advice, or just want to chat—I'm here for you. 😊 |
| `minimax-m2:cloud` | 2.23s | 40 | 71 | 111 | Hi there! How can I help you today? Whether you have questions about coding, need assistance with a project, or want to explore ideas, I'm here to help! |
| `glm-4.6:cloud` | 17.29s | 6 | 249 | 255 | Hello! I'm the GLM language model trained by Zhipu AI. How can I assist you today? Whether you have questions, need information, or just want to chat, I'm here to help. What would you like to discuss? |
| `ministral-3:3b-cloud` | 1.15s | 4 | 39 | 43 | Hi! 😊 How can I help you today? Whether you have questions, need advice, or just want to chat, I'm here for it! What’s on your mind? |
| `ministral-3:8b-cloud` | 1.06s | 4 | 42 | 46 | Hello! 😊 How can I assist you today? Whether you have a question, need help with something, or just want to chat, I'm here for you! What's on your mind? |
| `ministral-3:14b-cloud` | 1.28s | 4 | 67 | 71 | Hello! 😊 How can I assist you today? Whether you have a question, need help with something, or just want to chat—I'm here for it! Let me know what's on your mind. 🚀  (Or if you're testing me, I'm ready for that too! 😄) |
| `devstral-small-2:24b-cloud` | 0.95s | 4 | 13 | 17 | Hello! How can I assist you today? 😊 |
| `nemotron-3-nano:30b-cloud` | 0.93s | 18 | 42 | 60 | Hello! How can I assist you today? |
| `qwen3-next:80b-cloud` | 3.05s | 11 | 324 | 335 | Hello! 😊 How can I assist you today? |
| `rnj-1:8b-cloud` | 0.65s | 37 | 10 | 47 | Hello! How can I assist you today? |
| `devstral-2:123b-cloud` | 2.73s | 4 | 13 | 17 | Hello! How can I assist you today? 😊 |
| `qwen3-coder-next:cloud` | 0.84s | 9 | 12 | 21 | Hello! 👋 How can I help you today? |
| `minimax-m2.5:cloud` | 1.15s | 39 | 47 | 86 | Hi there! 👋 How can I help you today? |

## Failed Models

| Model | Reason / Error |
| :--- | :--- |
| `qwen3.5:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: b0b6687d-4df8-4da0-915c-31de66370d09) (status code: 403) |
| `qwen3.5:397b-cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: d96bcd47-c217-4973-9ebe-f44fee67cbb7) (status code: 403) |
| `glm-5.1:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: efa76612-5521-494b-ac0e-c087b4cfec4c) (status code: 403) |
| `minimax-m2.7:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: 2002b649-34f0-4bef-bf36-0a595a0d0207) (status code: 403) |
| `glm-5:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: 49dfed3b-c1a7-48ec-afe7-cfd0afbd3503) (status code: 403) |
| `kimi-k2.7-code:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: 0c61b629-e204-4767-b16e-8af85d0659ac) (status code: 403) |
| `gemini-3-flash-preview:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: 192acae5-eb8f-40a9-862e-3cc0eeff08ac) (status code: 403) |
| `kimi-k2.6:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: 9faa354f-5610-4638-b10e-304a7f7dbdd4) (status code: 403) |
| `deepseek-v4-pro:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: 7b0a59cb-57a8-4ef3-9313-eae12500240b) (status code: 403) |
| `deepseek-v4-flash:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: cae84850-6861-477e-a924-4e7f4fd8f601) (status code: 403) |
| `kimi-k2.5:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: 9c3e7da3-cfd4-411d-b888-92eb3e662799) (status code: 403) |
| `deepseek-v3.2:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: b7464e7d-f5f0-4f76-91dd-e04a7b70c5af) (status code: 403) |
| `kimi-k2-thinking:cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: cc1b0ffe-d2e4-4d48-b828-fbc252397ca0) (status code: 403) |
| `deepseek-v3.1:671b-cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: b2e95caf-8301-45b3-b2c0-054b64c6d1a9) (status code: 403) |
| `mistral-large-3:675b-cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: 71de8039-c860-49e7-bb61-2b593be86bfe) (status code: 403) |
| `kimi-k2:1t-cloud` | this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: a2a8df13-dc8e-48df-a973-e4fb3c381f9c) (status code: 403) |
