from django import template
from persiantools.jdatetime import JalaliDate

register = template.Library()


@register.filter
def jalali_date(value):
    return JalaliDate(value).strftime('%Y-%m-%d')
