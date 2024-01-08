from dataclasses import dataclass

from . import Article, Coupon, Categorie


@dataclass
class ArticleDansPanier:
    article: Article
    quantite: int = 1
    coupon_applique: Coupon | None = None

    @property
    def prix(self) -> float:
        return self.article.prix * self.quantite

    def __str__(self):
        return f"{self.article} x{self.quantite}"

    def __repr__(self):
        return f"{self.article} x{self.quantite}"

    def __iter__(self) -> iter:
        return iter(self.article)


@dataclass
class Panier:
    articles: list[ArticleDansPanier]
    coupons: list[Coupon]

    def __str__(self):
        return f"{self.articles}"

    def __iter__(self) -> iter:
        return iter(self.articles)

    def ajouter_article(self, article: Article, quantite: int = 1) -> None:
        self.articles.append(ArticleDansPanier(article, quantite))

    def retirer_article(self, article: Article) -> None:
        self.articles.remove(ArticleDansPanier(article))

    def calculer_prix(self) -> float:
        return sum(article.prix for article in self.articles)

    def _appliquer_coupon(self, coupon: Coupon) -> None:
        for coupon in self.coupons:
            for reduction in coupon.reductions:
                if isinstance(reduction.application, Article):
                    for article in self.articles:
                        if article.article == reduction.application:
                            article.coupon_applique = coupon
                elif isinstance(reduction.application, Categorie):
                    for article in self.articles:
                        if article.article.categorie == reduction.application:
                            article.coupon_applique = coupon
