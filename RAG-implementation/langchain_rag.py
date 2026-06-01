from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

#for langchain rag chain 
load_dotenv()

hug_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = InferenceClient(
    token=hug_token,
    model="meta-llama/Llama-3.1-8B-Instruct"
)
loader = PyPDFLoader("document.pdf")

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)
#print("Total Chunks:", len(chunks))
#for i, chunk in enumerate(chunks):
   # print(f"\nChunk {i+1}")
  #  print(chunk.page_content)



embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)


vector = embeddings.embed_query(
    "What is Python?"
)



query = input("Ask a question: ")

results = retriever.invoke(query)

context = "\n\n".join(
    [doc.page_content for doc in results]
)

prompt = f"""
Answer the question using ONLY the provided context.

Context:
{context}

Question:
{query}

If the answer is not present in the context, say:
"I don't know."

Answer:
"""
for doc in results:
    print("-" * 50)
    print(doc.page_content)

for doc in results:
    print(doc.metadata)

response = llm.chat_completion(
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    max_tokens=300
)
print("\n" + "=" * 50)
print("ANSWER")
print("=" * 50)

print(response.choices[0].message.content)