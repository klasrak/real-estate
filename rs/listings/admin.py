from django.contrib import admin

from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "is_published",
        "price",
        "list_date",
        "realtor",
    )

    list_display_links = (
        "id",
        "title",
    )

    list_filter = ("realtor",)

    list_editable = ("is_published",)

    search_fields = (
        "id",
        "title",
        "description",
        "address",
        "city",
        "state",
        "zipcode",
        "price",
        "realtor__name",
    )
