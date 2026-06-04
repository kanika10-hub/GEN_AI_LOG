from langchain_core.tools import tool
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

hug_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = InferenceClient(
    token=hug_token,
    model="meta-llama/Llama-3.1-8B-Instruct"
)

@tool
def calculator(expression: str):
    """Calculate a mathematical expression."""
    return eval(expression)

@tool
def uppercase(text: str):
    """Convert text to uppercase."""
    return text.upper()

@tool
def word_count(text: str):
    """Count words in text."""
    return len(text.split())

#create tool registry

tools = {
    "calculator": calculator,
    "uppercase": uppercase,
    "word_count": word_count
}

#tool_name = "calculator"
#tool_input = "25 * 14"

question = input("Ask something: ") 

tool_prompt = f"""
You are a tool selector.

Available tools:

1. calculator
   Use for mathematical calculations.

2. uppercase
   Use for converting text to uppercase.

3. word_count
   Use for counting words.

User Question:
{question}

Return ONLY in this format:

TOOL: tool_name
INPUT: tool_input
"""

response = llm.chat_completion(
    messages=[
        {
            "role": "user",
            "content": tool_prompt
        }
    ],
    max_tokens=100
)

decision = response.choices[0].message.content

print(decision)

lines = decision.split("\n")

tool_name = lines[0].replace("TOOL:", "").strip()
tool_input = lines[1].replace("INPUT:", "").strip()


tools = {
    "calculator": calculator,
    "uppercase": uppercase,
    "word_count": word_count
}

result = tools[tool_name].invoke(tool_input)

print(result)




result = tools[tool_name].invoke(tool_input)

print(result)

final_prompt = f"""
User Question:
{question}

Tool Used:
{tool_name}

Tool Result:
{result}

Answer the user's question using the tool result.
"""

final_response = llm.chat_completion(
    messages=[
        {
            "role": "user",
            "content": final_prompt
        }
    ],
    max_tokens=200
)
print("\n" + "=" * 50)
print("FINAL ANSWER")
print("=" * 50)

print(final_response.choices[0].message.content)