from dataclasses import dataclass
from typing import List, Set

@dataclass
class item_quant:
    item: str
    quant: int


@dataclass
class Recipe:
    input: List[item_quant] = None
    output: List[item_quant] = None
    tempo: int = 0
    feito_em: Set[str] = None