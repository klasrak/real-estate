from django.shortcuts import get_list_or_404, render

from .models import Listing


def index(request):
    listings = get_list_or_404(Listing, is_published=True)
    context = {
        "listings": listings,
    }
    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    return render(request, "listings/listing.html", {"listing_id": listing_id})


def search(request):
    return render(request, "listings/search.html")
