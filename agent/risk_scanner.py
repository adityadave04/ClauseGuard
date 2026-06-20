import json

from rag.retriever import Retriever
from rag.reranker import Reranker
from llm.grok_client import GrokClient


class RiskScanner:

    def __init__(self):
        self.retriever = Retriever()
        self.reranker = Reranker()
        self.llm = GrokClient()

    def scan(self):

        chunks = self.retriever.retrieve(
            "termination liability indemnity confidentiality payment SLA"
        )

        chunks = self.reranker.rerank(
            "contract risks",
            chunks,
            top_k=3
        )

        context = "\n\n".join(
            [
                f"Section {c['section_number']} - {c['section_title']}\n{c['text'][:500]}"
                for c in chunks
            ]
        )

        prompt = f"""
Analyze these contract clauses.

Return exactly 3 risks.

Prioritize HIGH severity risks.

Return ONLY valid JSON.

[
 {{
   "severity":"",
   "section_number":"",
   "title":"",
   "issue":"",
   "recommendation":""
 }}
]

No markdown.
No explanations.

Context:

{context}
"""

        answer = self.llm.invoke(prompt)

        # cleanup
        answer = answer.replace("```json", "")
        answer = answer.replace("```", "")
        answer = answer.strip()

        print("\nRAW RESPONSE:\n")
        print(answer)

        try:
            return json.loads(answer)

        except Exception as e:
            print("\nJSON PARSE FAILED\n")
            print(answer)
            raise e