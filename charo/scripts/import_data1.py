from charo.models import Article,category # de charo.models nous importons la classe article n'oublions pas que tout est objet

def run():
    for i in range(5,15):
        article=Article()
        h=category.objects.get(id=1)
        article.titre="article n` #%d" %i
        article.Category=h
        article.description="description article n` #%d" %i
        article.image="http://default" # ça sera notre image par defaut
        article.save()

    print("operation reussie")  # une fois finis on ouvre le terminal et on tape python manage.py runscript import_data      