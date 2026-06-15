import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    print(app.invoke(input={"question": "Who is Ahmed Osama Helmy ?"}))