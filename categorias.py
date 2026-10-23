from pathlib import Path

CATEGORIAS: dict[str, set[str]] = {
    "Imagens": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Documentos": {".pdf", ".docx", ".txt", ".xlsx", ".pptx"},
    "Videos": {".mp4", ".mkv", ".mov"},
    "Audio": {".mp3", ".wav", ".flac"},
    "Compactados": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Codigo": {".py", ".ino", ".js", ".c", ".cpp"},
}


def categorizar(arquivo: Path) -> str:
    """Retorna a categoria do arquivo com base na extensão."""
    extensao = arquivo.suffix.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "Outros"