from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Listing


def index(request):
    listings = get_list_or_404(Listing, is_published=True)

    paginator = Paginator(listings, per_page=6)
    page_number = request.GET.get("page")
    paged_listings = paginator.get_page(page_number)

    context = {
        "listings": paged_listings,
    }

    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        "listing": listing,
    }
    return render(request, "listings/listing.html", context)


def search(request):
    return render(request, "listings/search.html")
