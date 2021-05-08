from django.shortcuts import get_list_or_404, render
from rs.listings.models import Listing


def index(request):
    listings = get_list_or_404(Listing, is_published=True)

    context = {
        "listings": listings[:3],
    }

    return render(request, "core/index.html", context)


def about(request):
    return render(request, "core/about.html")
