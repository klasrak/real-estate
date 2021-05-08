from django.shortcuts import get_list_or_404, render
from rs.listings.models import Listing
from rs.realtors.models import Realtor


def index(request):
    listings = get_list_or_404(Listing, is_published=True)

    context = {
        "listings": listings[:3],
    }

    return render(request, "core/index.html", context)


def about(request):
    mvp_realtors = get_list_or_404(Realtor, is_mvp=True)
    all_realtors = get_list_or_404(Realtor)

    context = {
        "realtors": all_realtors,
        "mvp": mvp_realtors,
    }
    return render(request, "core/about.html", context)
