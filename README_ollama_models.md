# Ollama Cloud Model Connectivity & Pricing Guide

This documentation details the results of verifying 39 Ollama Cloud models (names ending with `:cloud`), their support status on the default/free tier, and Ollama Cloud's subscription-based pricing.

---

## 💳 Ollama Cloud Pricing

Ollama Cloud runs on a flat-rate monthly subscription model, not pay-per-token:
- **Free Plan ($0/month):** Basic access to cloud models.
- **Pro Plan ($20/month or $200/year):** Up to 3 concurrent cloud models, 50x usage allowance of the Free tier, and the ability to upload/share private models.
- **Max Plan ($100/month):** Up to 10 concurrent cloud models and 5x usage allowance of the Pro tier.

---

## 📋 Connectivity Test Results

A connectivity test was executed for 39 models using a minimal prompt (`"Hi"`) to check support on the default/free tier.

- **Total Models Tested:** 39
- **Supported/Succeeded (Free Tier):** 23
- **Failed (Requires Subscription Upgrade / 403 Forbidden):** 16

### 🟢 Supported Models (Free Tier)

These models succeeded with the default free/default credentials:

| Model | Latency (s) | Input Tokens | Output Tokens | Total Tokens |
| :--- | :--- | :--- | :--- | :--- |
| `minimax-m3:cloud` | 3.24 | 177 | 84 | 261 |
| `nemotron-3-ultra:cloud` | 2.15 | 18 | 29 | 47 |
| `gemma4:31b-cloud` | 2.64 | 14 | 10 | 24 |
| `nemotron-3-super:cloud` | 2.66 | 18 | 237 | 255 |
| `glm-4.7:cloud` | 8.17 | 6 | 233 | 239 |
| `minimax-m2.1:cloud` | 1.44 | 39 | 63 | 102 |
| `gpt-oss:20b-cloud` | 1.21 | 68 | 40 | 108 |
| `gpt-oss:120b-cloud` | 1.28 | 68 | 43 | 111 |
| `qwen3-coder:480b-cloud` | 1.60 | 9 | 10 | 19 |
| `qwen3-vl:235b-cloud` | 4.35 | 11 | 173 | 184 |
| `qwen3-vl:235b-instruct-cloud` | 1.51 | 9 | 34 | 43 |
| `minimax-m2:cloud` | 2.23 | 40 | 71 | 111 |
| `glm-4.6:cloud` | 17.29 | 6 | 249 | 255 |
| `ministral-3:3b-cloud` | 1.15 | 4 | 39 | 43 |
| `ministral-3:8b-cloud` | 1.06 | 4 | 42 | 46 |
| `ministral-3:14b-cloud` | 1.28 | 4 | 67 | 71 |
| `devstral-small-2:24b-cloud` | 0.95 | 4 | 13 | 17 |
| `nemotron-3-nano:30b-cloud` | 0.93 | 18 | 42 | 60 |
| `qwen3-next:80b-cloud` | 3.05 | 11 | 324 | 335 |
| `rnj-1:8b-cloud` | 0.65 | 37 | 10 | 47 |
| `devstral-2:123b-cloud` | 2.73 | 4 | 13 | 17 |
| `qwen3-coder-next:cloud` | 0.84 | 9 | 12 | 21 |
| `minimax-m2.5:cloud` | 1.15 | 39 | 47 | 86 |

### 🔴 Subscription-Only Models (Failed with 403)

The following models failed because they require upgrading to a paid Ollama Cloud subscription plan (Pro or Max):

*   `qwen3.5:cloud`
*   `qwen3.5:397b-cloud`
*   `glm-5.1:cloud`
*   `minimax-m2.7:cloud`
*   `glm-5:cloud`
*   `kimi-k2.7-code:cloud`
*   `gemini-3-flash-preview:cloud`
*   `kimi-k2.6:cloud`
*   `deepseek-v4-pro:cloud`
*   `deepseek-v4-flash:cloud`
*   `kimi-k2.5:cloud`
*   `deepseek-v3.2:cloud`
*   `kimi-k2-thinking:cloud`
*   `deepseek-v3.1:671b-cloud`
*   `mistral-large-3:675b-cloud`
*   `kimi-k2:1t-cloud`

---

## 🚀 How to Run the Tests

To run the model testing script locally:

1. Configure your environment variables in `.env`:
   ```env
   OLLAMA_API_KEY=your_key_here
   ```
2. Run the script:
   ```bash
   python test_models.py
   ```
3. The script will output console logs, verify all models sequentially, and save two files:
   - `model_test_results.json`: Full detailed JSON metrics.
   - `model_test_results.md`: A clean Markdown report of the results.

---

## 🛠️ Code Files Reference

- **Testing Script:** [test_models.py](file:///c:/code/Personal/ai-projects/test_models.py)
- **Supported Models module:** [supported_models.py](file:///c:/code/Personal/ai-projects/supported_models.py)
