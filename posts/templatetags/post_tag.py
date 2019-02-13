from django import template
import re

register = template.Library()


@register.filter
def add_link(value):
    content = value.text
    tags = value.tags.all()
    for tag in tags:
        content = re.sub(r'\#'+tag.name+r'\b', '<a href="/explore/tags/'+tag.name+'">#'+tag.name+'</a>', content)
    return content
