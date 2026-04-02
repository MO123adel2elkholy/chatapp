from math import *
from django import template

register = template.Library()


@register.simple_tag
def caculate_total_price(price, Discount):
    if Discount is None or Discount is 0:
        return price
    sell_price = price
    sell_price = price - (price*(Discount/100))
    return sell_price


@register.simple_tag
def progress_bar(total_quantity, avalabilty):
    progress = avalabilty
    progress = int(avalabilty*(total_quantity/100))
    print(progress)
    return progress
