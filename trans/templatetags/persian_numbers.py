from django import template

register = template.Library()


@register.filter
def persian_numbers(value):
    value = str(value)
    persian_numbers = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    return value.translate(persian_numbers)
