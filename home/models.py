from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, RichTextField, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel



class HomePage(Page):
    templates = 'home/home_page.html'
    #this only allows for a single home page
    # max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    #here we can append to the existing content panels or even overriding (i.e get rid of title)
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta")
    ]

class Meta:

    verbose_name = "Home Page"
    verbose_name_plural = "Home Pages"