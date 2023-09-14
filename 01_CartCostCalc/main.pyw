# CART _PRICE_CALCULATOR #

from assets.scripts.settings import *
import tkinter as tk

root = tk.Tk()
# all the variables used for the calculator
hardwarecost = tk.StringVar()
distycost = tk.StringVar()
distyprice = 0.0
distygrams = tk.StringVar()
terpPrice = tk.StringVar()
terpml = tk.StringVar()
terpUsed = tk.StringVar()
gramsper = tk.StringVar()
shipping_tax = tk.StringVar()
totalterpprice = 0.0
cartCost = 0.0


def buildWidgets():
    # kill me
    global shipping_entry, hardware_entry, priceperbatch_label
    global distillatecost_entry, distillategrams_entry, pricepergram_label, pricepercart_label, gramsper_entry
    global terpeneml_entry, terpeneused_entry, terpeneprice_entry, terppricepergram_label
    # Buttons n stuff
    toggle_shipping = tk.Button(root, text="Enable/Disable", bg=BG2COLOR, fg=TTCOLOR, command=toggleshipping)
    calculate_bttn = tk.Button(root, text="Calculate!", bg=BG2COLOR, fg=TTCOLOR, command=findCost)

    # Declaring Labels
    calc_label = tk.Label(root, text="Cart Cost Calculator v1.0", bg=BGCOLOR, fg=TTCOLOR)
    auth_label = tk.Label(root, text="Created by Danny_Dabs", bg=BGCOLOR, fg=TTCOLOR)

    hardware_label = tk.Label(root, text="Hardware Cost:", bg=BGCOLOR, fg=TTCOLOR)
    distillatecost_label = tk.Label(root, text="Distillate Cost:", bg=BGCOLOR, fg=TTCOLOR)
    distillategrams_label = tk.Label(root, text="Grams of Distillate:", bg=BGCOLOR, fg=TTCOLOR)
    terpeneprice_label = tk.Label(root, text="Price of Terpenes", bg=BGCOLOR, fg=TTCOLOR)
    terpeneml_label = tk.Label(root, text="Purchased Terpene ml:", bg=BGCOLOR, fg=TTCOLOR)
    terpeneused_label = tk.Label(root, text="Terpenes used in batch (ml):", bg=BGCOLOR, fg=TTCOLOR)
    gramsper_label = tk.Label(root, text="Grams per Cart:", bg=BGCOLOR, fg=TTCOLOR)
    shippingtax_label = tk.Label(root, text="Shipping & Taxes:", bg=BGCOLOR, fg=TTCOLOR)

    terppricepergram_label = tk.Label(root, text="Terpene cost/g: $" + str(terppricepergram), bg=BGCOLOR, fg=TTCOLOR)
    pricepergram_label = tk.Label(root, text="Distillate Cost/g: $" + str(distyprice), bg=BGCOLOR, fg=TTCOLOR)
    priceperbatch_label = tk.Label(root, text="Cost per batch: $" + str(totalterpprice), bg=BGCOLOR, fg=TTCOLOR)
    pricepercart_label = tk.Label(root, text="Cost per Cart: $" + str(cartCost), bg=BGCOLOR, fg=TTCOLOR)

    # Declaring entries
    hardware_entry = tk.Entry(root, bg=BG2COLOR, fg=TTCOLOR, textvariable=hardwarecost)
    distillatecost_entry = tk.Entry(root, bg=BG2COLOR, fg=TTCOLOR, textvariable=distycost)
    distillategrams_entry = tk.Entry(root, bg=BG2COLOR, fg=TTCOLOR, textvariable=distygrams)
    terpeneprice_entry = tk.Entry(root, bg=BG2COLOR, fg=TTCOLOR, textvariable=terpPrice)
    terpeneml_entry = tk.Entry(root, bg=BG2COLOR, fg=TTCOLOR, textvariable=terpml)
    terpeneused_entry = tk.Entry(root, bg=BG2COLOR, fg=TTCOLOR, textvariable=terpUsed)
    gramsper_entry = tk.Entry(root, bg=BG2COLOR, fg=TTCOLOR, textvariable=gramsper)
    shipping_entry = tk.Entry(root, bg=BG2COLOR, fg=TTCOLOR, state="disabled", textvariable=shipping_tax)

    # Builds Buttons n stuff
    toggle_shipping.grid(row=9, column=2, pady=2)
    calculate_bttn.grid(row=11, column=2, pady=2)

    # Build Labels
    calc_label.grid(row=0, column=1, pady=2)
    auth_label.grid(row=1, column=1, pady=2)
    hardware_label.grid(row=2, column=0, pady=2)
    distillatecost_label.grid(row=3, column=0, pady=2)
    distillategrams_label.grid(row=4, column=0, pady=2)
    terpeneprice_label.grid(row=5, column=0, pady=2)
    terpeneml_label.grid(row=6, column=0, pady=2)
    terpeneused_label.grid(row=7, column=0, pady=2)
    gramsper_label.grid(row=8, column=0, pady=2)
    shippingtax_label.grid(row=9, column=0, pady=2)

    terppricepergram_label.grid(row=10, column=1, pady=2)
    pricepergram_label.grid(row=11, column=1, pady=2)
    priceperbatch_label.grid(row=12, column=1, pady= 2)
    pricepercart_label.grid(row=13, column=1, pady=2)

    # Build Entries
    hardware_entry.grid(row=2, column=1, pady=2)
    distillatecost_entry.grid(row=3, column=1, pady=2)
    distillategrams_entry.grid(row=4, column=1, pady=2)
    terpeneprice_entry.grid(row=5, column=1, pady=2)
    terpeneml_entry.grid(row=6, column=1, pady=2)
    terpeneused_entry.grid(row=7, column=1, pady=2)
    gramsper_entry.grid(row=8, column=1, pady=2)
    shipping_entry.grid(row=9, column=1, pady=2)


def findCost():
    global distycost, distygrams, distyprice, hardwarecost, gramsper
    global terpPrice, terpml, terpUsed, terppricepergram, cartCost, totalterpprice
    global shippingToggled, shipping_tax
    hardwarecost = float(hardware_entry.get())
    distycost = float(distillatecost_entry.get())
    distygrams = float(distillategrams_entry.get())
    terpUsed = float(terpeneused_entry.get())
    terpml = float(terpeneml_entry.get())
    terpPrice = float(terpeneprice_entry.get())
    gramsper = float(gramsper_entry.get())
    if not len(shipping_entry.get()) == 0:
        shipping_tax = float(shipping_entry.get())
    else:
        shipping_tax = 0.0

    distyprice = distycost / distygrams
    totalterpprice = (terpPrice / terpml) * terpUsed
    terppricepergram = totalterpprice / distygrams

    if shippingToggled:
        cartCost = (terppricepergram + distyprice) * gramsper + hardwarecost + (shipping_tax / distygrams)
    else:
        cartCost = (terppricepergram + distyprice) * gramsper + hardwarecost

    terppricepergram_label['text'] = "Terpene cost/g: $" + str(round(terppricepergram, 2))
    priceperbatch_label['text'] = "Flavored Batch cost: $" + str(distycost + round(totalterpprice, 2))
    pricepergram_label['text'] = "Distillate cost/g: $" + str(round(distyprice, 2))
    pricepercart_label['text'] = "Cost per Cart: $" + str(round(cartCost, 2))


def toggleshipping():
    global shippingToggled
    if shippingToggled:
        shipping_entry['state'] = tk.DISABLED
        shippingToggled = False
    else:
        shipping_entry['state'] = tk.NORMAL
        shippingToggled = True


def main():
    root.title(TITLE)
    root.geometry(geoString)
    root.resizable(False, False)
    root.configure(bg=BGCOLOR)
    root.iconbitmap(ICONDIR)
    buildWidgets()


main()
root.mainloop()

