from django import template
from django.template.defaultfilters import striptags, safe

register = template.Library()

@register.filter
def highlight_fragments(input):
    return safe(striptags(input).replace('[[[', '<em class="highlight">').replace(']]]', '</em>'))
