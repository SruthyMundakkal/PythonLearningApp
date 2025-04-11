from django import template
import re

register = template.Library()

@register.filter
def sentence_break(value):
    if not isinstance(value, str):
        return value

    print("Original Content:", value)

    # This handles full stops followed by any whitespace (space, tab, newline, etc.)
    sentences = re.split(r'(?<=[.!?])\s+', value)

    print("Split Sentences:", sentences)

    return '<br>'.join(sentences)
