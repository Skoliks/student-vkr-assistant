class ChunkingService:
    def split_text(
        self,
        text: str,
        max_chunk_size: int = 1200,
    ) -> list[str]:

        if not text or not text.strip():
            return []

        paragraphs = self._split_into_paragraphs(text)

        chunks: list[str] = []
        current_chunk = ""

        for paragraph in paragraphs:
            if len(paragraph) > max_chunk_size:
                if current_chunk:
                    chunks.append(current_chunk)
                    current_chunk = ""

                chunks.extend(
                    self._split_long_paragraph(
                        paragraph=paragraph,
                        max_chunk_size=max_chunk_size,
                    )
                )
                continue

            candidate = self._join_paragraphs(current_chunk, paragraph)

            if len(candidate) <= max_chunk_size:
                current_chunk = candidate
            else:
                if current_chunk:
                    chunks.append(current_chunk)

                current_chunk = paragraph

        if current_chunk:
            chunks.append(current_chunk)

        return chunks

    def _split_into_paragraphs(self, text: str) -> list[str]:
        paragraphs = text.split("\n\n")

        return [
            paragraph.strip()
            for paragraph in paragraphs
            if paragraph.strip()
        ]

    def _join_paragraphs(self, current_chunk: str, paragraph: str) -> str:
        if not current_chunk:
            return paragraph

        return f"{current_chunk}\n\n{paragraph}"

    def _split_long_paragraph(
        self,
        paragraph: str,
        max_chunk_size: int,
    ) -> list[str]:
        chunks: list[str] = []

        for start in range(0, len(paragraph), max_chunk_size):
            chunk = paragraph[start:start + max_chunk_size].strip()

            if chunk:
                chunks.append(chunk)

        return chunks
    
    
                   
                   
