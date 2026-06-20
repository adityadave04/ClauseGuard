from rag.retriever import Retriever
from rag.reranker import Reranker
from llm.grok_client import GrokClient


class AskTool:

    def __init__(self):

        self.retriever = Retriever()
        self.reranker = Reranker()
        self.llm = GrokClient()

    def ask(
            self,
            question: str
    ):

        chunks = self.retriever.retrieve(
            question,
            top_k=10
        )

        ranked_chunks = self.reranker.rerank(
            question,
            chunks,
            top_k=4
        )

        context = "\n\n".join(
            [
                f"Section {chunk['section_number']} - "
                f"{chunk['section_title']}\n"
                f"{chunk['text']}"
                for chunk in ranked_chunks
            ]
        )

        prompt = f"""
Answer the question using only the provided contract context.

Context:

{context}

Question:
{question}

Provide citations like:
(Section 8.4)
"""

        answer = self.llm.invoke(prompt)

        return {
            "answer": answer,
            "sources": [
                {
                    "section_number": chunk["section_number"],
                    "section_title": chunk["section_title"]
                }
                for chunk in ranked_chunks
            ]
        }