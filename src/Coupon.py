from dataclasses import dataclass
from array import array

from . import Categorie
from . import Article


@dataclass
class Reduction:
    application: Article | Categorie
    reduction: float

    def __init__(self, reduction):
        self.reduction = reduction

    def __repr__(self) -> tuple[Article | Categorie, float]:
        return self.application, self.reduction

    def __str__(self):
        return f"{self.reduction}%"


@dataclass
class Coupon:
    nom: str
    reductions: array[Reduction]

    def __str__(self):
        return f"{self.nom}\n{self.reductions}"
