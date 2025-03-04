from dataclasses import dataclass, field
from typing import List, Set

@dataclass
class ItemQuant:
    item: str
    quant: int

@dataclass
class Recipe:
    input: List[ItemQuant] = field(default_factory=list)
    output: List[ItemQuant] = field(default_factory=list)
    tempo: int = 0
    feito_em: Set[str] = field(default_factory=set)