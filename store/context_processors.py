from .models import Category


def categories(request):
    # level = 0 only get top parent element
    return {"categories": Category.objects.filter(level=0)}
