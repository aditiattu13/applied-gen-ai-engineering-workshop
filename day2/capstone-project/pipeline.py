from retriever import SimpleVectorStore
from agent_layer import agent_reasoning
from evaluation import evaluate

def load_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def chunk_text(text, chunk_size=800, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def run_pipeline(paper_path, user_query):

    print("Loading paper...")
    text = load_text_file(paper_path)

    print("Chunking...")
    chunks = chunk_text(text)

    print("Building vector store...")
    store = SimpleVectorStore()
    store.add_documents(chunks)

    print("Agent reasoning...")
    answer = agent_reasoning(store, user_query)

    print("Evaluating...")
    context = "\n".join(store.retrieve(user_query))
    evaluation_result = evaluate(context, user_query, answer)

    print("\n==============================")
    print("📘 FINAL ANSWER:\n")
    print(answer)
    print("\n📊 EVALUATION:\n")
    print(evaluation_result)
    print("==============================")

if __name__ == "__main__":
    query = input("Ask your question: ")
    run_pipeline("paper.txt", query)