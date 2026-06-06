For an EXPLAIN.md, write it as if someone visiting your GitHub wants to understand what you built and what you learned.

LangGraph ReAct Agent - Learning Project

Overview

This project is part of my AI Engineering learning journey.

The goal was to understand how AI agents work instead of treating them as a black box. I started by building tools manually, then moved to LangChain, LangGraph, and LangSmith to understand how modern AI applications are built.

---

Features

- ReAct Agent
- Tool Calling
- Calculator Tool
- Uppercase Tool
- Word Count Tool
- LangGraph Agent Workflow
- LangSmith Tracing and Debugging

---

What I Learned

LangChain

LangChain provides abstractions that make it easier to build LLM-powered applications.

Instead of manually managing prompts, model calls, and outputs, LangChain provides reusable components such as:

- Prompts
- Chains
- Tools
- Agents
- Memory

---

LangGraph

LangGraph extends LangChain by introducing workflows and state management.

It allows agents to:

1. Reason about a task
2. Decide which tool to use
3. Execute the tool
4. Observe the result
5. Continue until a final answer is produced

This creates a decision loop rather than a single LLM call.

---

LangSmith

LangSmith helps monitor and debug AI applications.

It provides:

- Execution traces
- Agent step visualization
- Tool call tracking
- Evaluation and debugging support

This makes it easier to understand what an agent is doing internally.

---

ReAct Agent

The ReAct (Reason + Act) pattern allows an LLM to think about a problem and use tools when needed.

Example:

User: What is 25 × 14?

Agent Process:

1. Recognize calculation is needed
2. Call Calculator Tool
3. Receive result
4. Return final answer

Instead of relying only on model knowledge, the agent can interact with external tools.

---

Challenges Faced

While integrating Hugging Face models, I encountered provider and model availability issues.

One important lesson was:

«A model being available on Hugging Face does not necessarily mean it is available through the Hugging Face Inference API.»

This helped me better understand how model hosting and inference providers work.

---

Next Steps

- Add chat history and memory
- Integrate RAG with the agent
- Add more tools
- Explore multi-agent workflows
- Learn advanced LangGraph patterns

---

Tech Stack

- Python
- LangChain
- LangGraph
- LangSmith
- Hugging Face
- LLM Agents

---
