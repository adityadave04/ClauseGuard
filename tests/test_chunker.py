from rag.chunker import ContractChunker


def test_chunker():

    pdf_path = r"C:\Users\adity\Downloads\Sample_contract_doc.pdf"

    chunker = ContractChunker(pdf_path)

    chunks = chunker.create_chunks()

    # Basic assertions
    assert chunks is not None
    assert len(chunks) > 0

    # Print stats
    print(f"\nTotal chunks created: {len(chunks)}")

    # Show first 5 chunks
    for i, chunk in enumerate(chunks[:5]):
        print("\n------------------------")
        print(f"Chunk {i+1}")
        print("Section:", chunk.section_number)
        print("Title:", chunk.section_title)
        print("Page:", chunk.page_number)
        print("Text preview:")
        print(chunk.text[:200])