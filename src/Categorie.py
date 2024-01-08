from dataclasses import dataclass


@dataclass
class Categorie:
    nom: str
    description: str = ""

    def __str__(self):
        return (f"{self.nom}"
                f"{f" - {self.description}" if self.description else ""}")
