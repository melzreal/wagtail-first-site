from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add your title')
    cards = blocks.ListBlock(
      blocks.StructBlock(
        [
          ("image", ImageChooserBlock(required=True)),
          ("title", blocks.CharBlock(required=True, max_length=40)),
          ("text", blocks.TextBlock(required=True, max_length=200)),
          ("button_page", blocks.PageChooserBlock(required=False)),
          ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
        ]
      )
    )
    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Cards"

class RichtextBlock(blocks.RichTextBlock):

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"

class SimpleRichtextBlock(blocks.RichTextBlock):
    def __init__(self, required=True, help_text=None, editor='default', features=None, **kwargs):
        super().__init__(**kwargs)
        self.features = [
          "bold",
          "italic",
          "link"
        ]

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"

# the LinkStructValue class is just a way of moving logic away from the templates
# instead of having the if else within the template, we define that here
# so then we can just call self.url within the ButtonBlock html
# the reason we call self instead of the url is because the value belongs to Struct

class LinkStructValue(blocks.StructValue):
    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url
        return None

class ButtonBlock(blocks.StructBlock):
    button_page = blocks.PageChooserBlock(required=False, help_text="If selected, this url will be used first")
    button_url = blocks.URLBlock(required=False)

    class Meta:
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Single Button"
        value_class = LinkStructValue

class CTABlock(blocks.StructBlock):
# call to action block
    title = blocks.CharBlock()
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False, help_text="If selected, this url will be used first")
    button_url = blocks.URLBlock(required=False)

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"
        value_class = LinkStructValue
