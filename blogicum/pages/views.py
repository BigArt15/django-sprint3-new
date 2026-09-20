from django.shortcuts import render


def about(request):
    """Страница «О проекте»."""
    context = {
        "title": "О проекте",
        "description": "Это блог о путешествиях и кулинарии.",
    }
    return render(request, "pages/about.html", context)


def rules(request):
    """Страница с правилами сообщества."""
    context = {
        "title": "Правила сообщества",
        "rules_list": [
            "Будьте вежливы друг с другом.",
            "Не публикуйте оскорбительный контент.",
            "Соблюдайте авторские права.",
        ],
    }
    return render(request, "pages/rules.html", context)
