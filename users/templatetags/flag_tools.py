from difflib import SequenceMatcher
from django import template

from users.constants import Country, Languages

register = template.Library()


@register.filter
def find_country_name(language):
    if language == "English":
        return Country.GB.name.lower()
    if language == "Spanish; Castilian":
        return Country.ES.name.lower()
    if language == "Chinese":
        return Country.CN.name.lower()
    if language == "French":
        return Country.FR.name.lower()
    for country in Country:
        if similar(country.value, language) > 0.8:
            return country.name.lower()
    return None


@register.filter
def get_language_name(language_code):
    return Languages[language_code].value

@register.filter
def normalize_code(value):
    return value.replace("_", "-")


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
