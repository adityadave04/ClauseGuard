import json

from rag.retriever import Retriever
from rag.reranker import Reranker
from llm.client import LLMClient


class ContractExtractor:

    def __init__(self):

        self.retriever = Retriever()
        self.reranker = Reranker()
        self.llm = LLMClient()

    def extract(self):

        chunks = self.retriever.retrieve(
            "agreement number parties payment terms SLA governing law termination fee"
        )

        chunks = self.reranker.rerank(
            "contract metadata",
            chunks,
            top_k=4
        )

        context = "\n\n".join(
            [
                f"Section {c['section_number']} - {c['section_title']}\n{c['text'][:700]}"
                for c in chunks
            ]
        )

        prompt = f"""
Extract the following fields.

Return ONLY valid JSON.

{{
  "agreement_number":"",
  "service_provider":"",
  "client":"",
  "governing_law":"",
  "payment_terms_days":0,
  "notice_period_days":0,
  "termination_fee_percent":0,
  "uptime_sla_percent":0
}}

Context:

{context}
"""

        answer = self.llm.invoke(prompt)

        answer = answer.replace("```json", "")
        answer = answer.replace("```", "").strip()

        return json.loads(answer)