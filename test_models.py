import os
import sys
import time
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

MODELS = [
    "minimax-m3:cloud",
    "nemotron-3-ultra:cloud",
    "gemma4:31b-cloud",
    "qwen3.5:cloud",
    "qwen3.5:397b-cloud",
    "glm-5.1:cloud",
    "minimax-m2.7:cloud",
    "nemotron-3-super:cloud",
    "glm-5:cloud",
    "kimi-k2.7-code:cloud",
    "glm-4.7:cloud",
    "gemini-3-flash-preview:cloud",
    "minimax-m2.1:cloud",
    "kimi-k2.6:cloud",
    "deepseek-v4-pro:cloud",
    "deepseek-v4-flash:cloud",
    "kimi-k2.5:cloud",
    "gpt-oss:20b-cloud",
    "gpt-oss:120b-cloud",
    "qwen3-coder:480b-cloud",
    "qwen3-vl:235b-cloud",
    "qwen3-vl:235b-instruct-cloud",
    "deepseek-v3.2:cloud",
    "kimi-k2-thinking:cloud",
    "minimax-m2:cloud",
    "glm-4.6:cloud",
    "ministral-3:3b-cloud",
    "ministral-3:8b-cloud",
    "ministral-3:14b-cloud",
    "devstral-small-2:24b-cloud",
    "nemotron-3-nano:30b-cloud",
    "qwen3-next:80b-cloud",
    "rnj-1:8b-cloud",
    "deepseek-v3.1:671b-cloud",
    "devstral-2:123b-cloud",
    "mistral-large-3:675b-cloud",
    "kimi-k2:1t-cloud",
    "qwen3-coder-next:cloud",
    "minimax-m2.5:cloud",
]

def test_model(model_name):
    prompt = "Hi"
    
    print(f"Testing model: {model_name}...", flush=True)
    try:
        headers = {}
        api_key = os.environ.get("OLLAMA_API_KEY", "")
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
            
        llm = ChatOllama(
            model=model_name,
            temperature=0,
            base_url="https://ollama.com",
            client_kwargs={"headers": headers} if headers else None,
            timeout=15.0
        )
        
        start_time = time.time()
        response = llm.invoke([HumanMessage(content=prompt)])
        latency = time.time() - start_time
        
        input_tokens = 0
        output_tokens = 0
        total_tokens = 0
        
        if hasattr(response, 'usage_metadata') and response.usage_metadata:
            input_tokens = response.usage_metadata.get('input_tokens', 0)
            output_tokens = response.usage_metadata.get('output_tokens', 0)
            total_tokens = response.usage_metadata.get('total_tokens', 0)
        elif response.response_metadata:
            input_tokens = response.response_metadata.get('prompt_eval_count', 0)
            output_tokens = response.response_metadata.get('eval_count', 0)
            total_tokens = input_tokens + output_tokens
            
        print(f"  SUCCESS! Latency: {latency:.2f}s | Tokens: In={input_tokens}, Out={output_tokens}, Total={total_tokens}", flush=True)
        return {
            "model": model_name,
            "status": "success",
            "response": response.content.strip(),
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "latency": latency,
            "error": None
        }
    except Exception as e:
        error_msg = str(e)
        if "HTTPError" in error_msg:
             error_msg = error_msg.split("\n")[0]
        print(f"  FAILED: {error_msg}", flush=True)
        return {
            "model": model_name,
            "status": "failed",
            "response": None,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "latency": 0,
            "error": error_msg
        }

def main():
    # Reconfigure stdout to use UTF-8 to prevent UnicodeEncodeError on Windows
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    results = []
    print(f"Starting ChatOllama test for {len(MODELS)} models...", flush=True)
    for model in MODELS:
        res = test_model(model)
        results.append(res)
        time.sleep(0.5)
        
    # Write full results to JSON
    import json
    try:
        with open("model_test_results.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print("\nSaved full results to model_test_results.json", flush=True)
    except Exception as e:
        print(f"\nFailed to save JSON results: {e}", flush=True)

    print("\n" + "="*50)
    print("TEST RESULTS SUMMARY")
    print("="*50)
    
    success_count = 0
    for res in results:
        if res["status"] == "success":
            success_count += 1
            print(f"[{res['model']}] SUCCESS")
            # Safe print handling for terminal
            safe_resp = res['response'].replace('\n', ' ')
            print(f"  Response: {safe_resp}")
            print(f"  Tokens Used: Input={res['input_tokens']}, Output={res['output_tokens']}, Total={res['total_tokens']}")
            print(f"  Latency: {res['latency']:.2f}s")
        else:
            print(f"[{res['model']}] FAILED — Error: {res['error']}")
            
    print("="*50)
    print(f"Total: {len(MODELS)} | Success: {success_count} | Failed: {len(MODELS) - success_count}")
    print("="*50)

    # Generate Markdown Table Report
    try:
        with open("model_test_results.md", "w", encoding="utf-8") as f:
            f.write("# Ollama Cloud Model Testing Results\n\n")
            f.write(f"Total Models Tested: {len(MODELS)} | Successful: {success_count} | Failed: {len(MODELS) - success_count}\n\n")
            f.write("## Successful Models\n\n")
            f.write("| Model | Latency (s) | Input Tokens | Output Tokens | Total Tokens | Sample Response |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
            for res in results:
                if res["status"] == "success":
                    safe_resp = res['response'].replace('\n', ' ').replace('|', '\\|')
                    f.write(f"| `{res['model']}` | {res['latency']:.2f}s | {res['input_tokens']} | {res['output_tokens']} | {res['total_tokens']} | {safe_resp} |\n")
            
            f.write("\n## Failed Models\n\n")
            f.write("| Model | Reason / Error |\n")
            f.write("| :--- | :--- |\n")
            for res in results:
                if res["status"] != "success":
                    f.write(f"| `{res['model']}` | {res['error']} |\n")
        print("Saved markdown report to model_test_results.md", flush=True)
    except Exception as e:
        print(f"Failed to save Markdown report: {e}", flush=True)

if __name__ == "__main__":
    main()
