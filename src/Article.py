from dataclasses import dataclass

from . import Categorie


@dataclass
class Article:
    nom: str
    prix: float
    categorie: Categorie | None = None

    def __str__(self):
        return f"{self.nom}{f" ({self.categorie})" if self.categorie else ""}"
