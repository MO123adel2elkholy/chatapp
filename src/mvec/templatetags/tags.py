from math import *
from django import template

register = template.Library()


@register.simple_tag
def caculate_total_price(price, Discount):
    if Discount is None or Discount == 0:
        return price
    sell_price = price - (price * (Discount / 100))
    return sell_price


@register.simple_tag
def progress_bar(total_quantity, avalabilty):
    try:
        return int(float(avalabilty) * (float(total_quantity) / 100))
    except (TypeError, ValueError):
        return 0


# add multiply filter used in templates
from decimal import Decimal, InvalidOperation

@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return Decimal(str(value)) * Decimal(str(arg))
    except (InvalidOperation, TypeError, ValueError):
        return ''
