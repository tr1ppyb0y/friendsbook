from django import template
from deep_translator import GoogleTranslator

register = template.Library()

@register.filter(name='hindi_translation')
def hindi_translation(value):
    return GoogleTranslator(source='auto', target='hi').translate(value)