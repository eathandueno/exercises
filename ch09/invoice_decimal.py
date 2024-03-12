#!/usr/bin/env python3

from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale
from decimal import Decimal, ROUND_HALF_UP

# set the locale to 'en_US.UTF-8'
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# format specifications
currency_format = "{:,.2f}"
width_format = "{:<20}"
# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
    invoice_total = subtotal + sales_tax
    shipping_cost = subtotal * Decimal("0.085")
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)

     # display the results
    print(f"{width_format.format('Order total:')} {locale.currency(order_total, grouping=True)}")
    print(f"{width_format.format('Discount amount:')} {locale.currency(discount, grouping=True)}")
    print(f"{width_format.format('Subtotal:')} {locale.currency(subtotal, grouping=True)}")
    print(f"{width_format.format('Sales tax:')} {locale.currency(sales_tax, grouping=True)}")
    print(f"{width_format.format('Shipping cost:')} {locale.currency(shipping_cost, grouping=True)}")
    print(f"{width_format.format('Invoice total:')} {locale.currency(invoice_total, grouping=True)}")
    print()


    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")
