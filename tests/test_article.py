from src import Article, Categorie


litterature = Categorie("Littérature")


def test_creation_article_1():
    article = Article("Pomme", 0.5)
    assert article.nom == "Pomme"
    assert article.prix == 0.5
    assert article.categorie is None


def test_creation_article_2():
    article = Article("Livre", 15.99, litterature)
    assert article.nom == "Livre"
    assert article.prix == 15.99
    assert article.categorie == litterature


def test_str_article_1():
    article = Article("Livre", 15.99)
    assert str(article) == "Livre"


def test_str_article_2():
    article = Article("Livre", 15.99, litterature)
    assert str(article) == "Livre (Littérature)"
