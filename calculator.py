sale_price = 800000
tax = 0

bracket1 = 55000
bracket1_tax = .005

bracket2 = 250000 - 55000
bracket2_tax = .01

bracket3 = 368333 - 250000
bracket3_tax = .015

bracket4 = 400000 -368334
bracket4_tax = .015

bracket5 = 2000000 - 400000
bracket5_tax = .02

bracket6 = 2000000
bracket6_tax = .025

if sale_price <= bracket1:
    tax = tax + (sale_price * bracket1_tax)
else:
    sale_price > bracket1
    tax = tax + (bracket1 * bracket1_tax)
    sale_price = sale_price - bracket1

    if sale_price <= bracket2:
        tax = tax + (sale_price * bracket2_tax)
    else:
        sale_price > bracket2
        tax = tax + (bracket2 * bracket2_tax)
        sale_price = sale_price - bracket2

        if sale_price <= bracket3:
            tax = tax + (sale_price * bracket3_tax)
        else:
            sale_price > bracket3
            tax = tax + (bracket3 * bracket3_tax)
            sale_price = sale_price - bracket3

            if sale_price <= bracket4:
                tax = tax + (sale_price * bracket4_tax)
            else:
                sale_price > bracket4
                tax = tax + (bracket4 * bracket4_tax)
                sale_price = sale_price - bracket4

                if sale_price <= bracket5:
                    tax = tax + (sale_price * bracket5_tax)
                else:
                    sale_price > bracket5
                    tax = tax + (bracket5 * bracket5_tax)
                    sale_price = sale_price - bracket5

                    if sale_price >= 0:
                        tax = tax + (sale_price * bracket6_tax)
                    




print(sale_price)
print(tax)


