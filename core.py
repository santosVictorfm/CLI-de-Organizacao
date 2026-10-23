from dataclasses import dataclass
from pathlib import Path


@dataclass
class Movimento:
    origem: Path
    destino: Path


def planejar(pasta: Path) -> list[Movimento]:
    ...