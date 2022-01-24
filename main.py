# here we use forex python library to convert the currencies
from forex_python.converter import *
from tkinter import *
from tkinter import ttk
import os
'''
# get currency rates using currencyRates()
ratesOfCurrency = CurrencyRates()

# get the currency which you want to convert
currentCurrency = input("Please enter the current currency").upper()

# get the currency in which we want to convert
convertCurrency = input("Please enter the currency in which you want to convert the currency").upper()

# amount that is converted get by user
amount = int(input("please enter the amount you have to convert!"))

# resultant amount is saved on this "result" variable
result = ratesOfCurrency.convert(currentCurrency, convertCurrency, amount)

print(result)
'''
root = Tk()
root.title("Currency Converter")
root.geometry("500x500+400+60")

# definitions -------------------------
def conversion():
    # getting all the field's values
    curCurrency = c_entry.get()
    desireCurrency = d_entry.get()
    amt = a_entry.get()
    rateOfCurrency = CurrencyRates()
    result = rateOfCurrency.convert(curCurrency, desireCurrency, amt)
    resultLabel = Label(root, text=result, font=16)
    resultLabel.place(relx=0.5, y=400, anchor=CENTER)


def close():
    exit(os)
# variables ---------------------------
c_entry = StringVar()
d_entry = StringVar()
a_entry = IntVar()

# label -------------------------------
currentLabel = Label(root, text="Select current currency code", font=16).place(relx=0.5, y=80, anchor=CENTER)
desiredLabel = Label(root, text="Select desired currency code", font=16).place(relx=0.5, y=180, anchor=CENTER)
amountLabel = Label(root, text="Enter amount", font=16).place(relx=0.5, y=280, anchor=CENTER)

# entries -----------------------------
currentEntry = ttk.Combobox(root, width=30, textvariable=c_entry)
currentEntry.place(relx=0.5, y=110, anchor=CENTER)
currentEntry['values'] = CURRENCIES = (	("AFN", "Afghani"), ("DZD", "Algerian Dinar"),
                                         ("ARS", "Argentine Peso"), ("AMD", "Armenian Dram"),
                                         ("AWG", "Aruban Guilder"), ("AUD", "Australian Dollar"),
                                         ("AZN", "Azerbaijanian Manat"), ("BSD", "Bahamian Dollar"),
                                         ("BHD", "Bahraini Dinar"), ("THB", "Baht"),("PAB", "Balboa"),
                                         ("BBD", "Barbados Dollar"), ("BYR", "Belarussian Ruble"),
                                         ("BZD", "Belize Dollar"), ("BMD", "Bermudian Dollar"),
                                         ("VEF", "Bolivar Fuerte"), ("BOB", "Boliviano"),
                                         ("BRL", "Brazilian Real"), ("BND", "Brunei Dollar"),
                                         ("BGN", "Bulgarian Lev"), ("BIF", "Burundi Franc"),
                                         ("CAD", "Canadian Dollar"), ("CVE", "Cape Verde Escudo"),
                                         ("KYD", "Cayman Islands Dollar"), ("GHS", "Cedi"),
                                         ("CLP", "Chilean Peso"), ("COP", "Colombian Peso"),
                                         ("KMF", "Comoro Franc"), ("CDF", "Congolese Franc"),
                                         ("BAM", "Convertible Mark"), ("NIO", "Cordoba Oro"),
                                         ("CRC", "Costa Rican Colon"), ("HRK", "Croatian Kuna"),
                                         ("CUP", "Cuban Peso"), ("CZK", "Czech Koruna"),("GMD", "Dalasi"),
                                         ("DKK", "Danish Krone"), ("MKD", "Denar"), ("DJF", "Djibouti Franc"),
                                         ("STD", "Dobra"), ("DOP", "Dominican Peso"), ("VND", "Dong"),
                                         ("XCD", "East Caribbean Dollar"), ("EGP", "Egyptian Pound"),
                                         ("SVC", "El Salvador Colon"), ("ETB", "Ethiopian Birr"), ("EUR", "Euro"),
                                         ("FKP", "Falkland Islands Pound"), ("FJD", "Fiji Dollar"), ("HUF", "Forint"),
                                         ("GIP", "Gibraltar Pound"), ("XAU", "Gold"), ("HTG", "Gourde"),
                                         ("PYG", "Guarani"), ("GNF", "Guinea Franc"), ("GYD", "Guyana Dollar"),
                                         ("HKD", "Hong Kong Dollar"), ("UAH", "Hryvnia"), ("ISK", "Iceland Krona"),
                                         ("INR", "Indian Rupee"), ("IRR", "Iranian Rial"), ("IQD", "Iraqi Dinar"),
                                         ("JMD", "Jamaican Dollar"), ("JOD", "Jordanian Dinar"),
                                         ("KES", "Kenyan Shilling"), ("PGK", "Kina"), ("LAK", "Kip"),
                                         ("KWD", "Kuwaiti Dinar"), ("MWK", "Kwacha"), ("AOA", "Kwanza"),
                                         ("MMK", "Kyat"), ("GEL", "Lari"), ("LVL", "Latvian Lats"),
                                         ("LBP", "Lebanese Pound"), ("ALL", "Lek"), ("HNL", "Lempira"),
                                         ("SLL", "Leone"), ("RON", "Leu"), ("LRD", "Liberian Dollar"),
                                         ("LYD", "Libyan Dinar"), ("SZL", "Lilangeni"), ("LTL", "Lithuanian Litas"),
                                         ("LSL", "Loti"), ("MGA", "Malagasy Ariary"), ("MYR", "Malaysian Ringgit"),
                                         ("MUR", "Mauritius Rupee"), ("MZN", "Metical"), ("MXN", "Mexican Peso"),
                                         ("MDL", "Moldovan Leu"), ("MAD", "Moroccan Dirham"), ("BOV", "Mvdol"),
                                         ("NGN", "Naira"), ("ERN", "Nakfa"), ("NAD", "Namibia Dollar"),
                                         ("NPR", "Nepalese Rupee"), ("ANG", "Netherlands Antillean Guilder"),
                                         ("ILS", "New Israeli Sheqel"), ("TMT", "New Manat"),
                                         ("TWD", "New Taiwan Dollar"), ("NZD", "New Zealand Dollar"),
                                         ("BTN", "Ngultrum"), ("KPW", "North Korean Won"), ("NOK", "Norwegian Krone"),
                                         ("PEN", "Nuevo Sol"), ("MRO", "Ouguiya"), ("PKR", "Pakistan Rupee"),
                                         ("XPD", "Palladium"), ("MOP", "Pataca"), ("TOP", "Pa’anga"),
                                         ("CUC", "Peso Convertible"), ("UYU", "Peso Uruguayo"),
                                         ("PHP", "Philippine Peso"), ("XPT", "Platinum"), ("GBP", "Pound Sterling"),
                                         ("BWP", "Pula"), ("QAR", "Qatari Rial"), ("GTQ", "Quetzal"), ("ZAR", "Rand"),
                                         ("OMR", "Rial Omani"), ("KHR", "Riel"), ("MVR", "Rufiyaa"), ("IDR", "Rupiah"),
                                         ("RUB", "Russian Ruble"), ("RWF", "Rwanda Franc"), ("SHP", "Saint Helena Pound"),
                                         ("SAR", "Saudi Riyal"), ("RSD", "Serbian Dinar"), ("SCR", "Seychelles Rupee"),
                                         ("XAG", "Silver"), ("SGD", "Singapore Dollar"),
                                         ("SBD", "Solomon Islands Dollar"), ("KGS", "Som"), ("SOS", "Somali Shilling"),
                                         ("TJS", "Somoni"), 	("ZAR", "South African Rand"), ("LKR", "Sri Lanka Rupee"),
                                         ("XSU", "Sucre"), ("SDG", "Sudanese Pound"), ("SRD", "Surinam Dollar"),
                                         ("SEK", "Swedish Krona"), ("CHF", "Swiss Franc"), ("SYP", "Syrian Pound"),
                                         ("BDT", "Taka"), ("WST", "Tala"), ("TZS", "Tanzanian Shilling"),
                                         ("KZT", "Tenge"), ("TTD", "Trinidad and Tobago Dollar"), ("MNT", "Tugrik"),
                                         ("TND", "Tunisian Dinar"), ("TRY", "Turkish Lira"), ("AED", "UAE Dirham"),
                                         ("USD", "US Dollar"), ("UGX", "Uganda Shilling"),
                                         ("COU", "Unidad de Valor Real"), ("CLF", "Unidades de fomento"),
                                         ("UYI", "Uruguay Peso en Unidades Indexadas (URUIURUI)"),
                                         ("UZS", "Uzbekistan Sum"), ("VUV", "Vatu"), ("KRW", "Won"),
                                         ("YER", "Yemeni Rial"), ("JPY", "Yen"), ("CNY", "Yuan Renminbi"),
                                         ("ZMK", "Zambian Kwacha"), ("ZWL", "Zimbabwe Dollar"), ("PLN", "Zloty"),
                                         )
currentEntry.current()

desiredEntry = ttk.Combobox(root, width=30, textvariable=d_entry)
desiredEntry.place(relx=0.5, y=210, anchor=CENTER)
desiredEntry['values'] = CURRENCIES = (	("AFN", "Afghani"), ("DZD", "Algerian Dinar"),
                                         ("ARS", "Argentine Peso"), ("AMD", "Armenian Dram"),
                                         ("AWG", "Aruban Guilder"), ("AUD", "Australian Dollar"),
                                         ("AZN", "Azerbaijanian Manat"), ("BSD", "Bahamian Dollar"),
                                         ("BHD", "Bahraini Dinar"), ("THB", "Baht"),("PAB", "Balboa"),
                                         ("BBD", "Barbados Dollar"), ("BYR", "Belarussian Ruble"),
                                         ("BZD", "Belize Dollar"), ("BMD", "Bermudian Dollar"),
                                         ("VEF", "Bolivar Fuerte"), ("BOB", "Boliviano"),
                                         ("BRL", "Brazilian Real"), ("BND", "Brunei Dollar"),
                                         ("BGN", "Bulgarian Lev"), ("BIF", "Burundi Franc"),
                                         ("CAD", "Canadian Dollar"), ("CVE", "Cape Verde Escudo"),
                                         ("KYD", "Cayman Islands Dollar"), ("GHS", "Cedi"),
                                         ("CLP", "Chilean Peso"), ("COP", "Colombian Peso"),
                                         ("KMF", "Comoro Franc"), ("CDF", "Congolese Franc"),
                                         ("BAM", "Convertible Mark"), ("NIO", "Cordoba Oro"),
                                         ("CRC", "Costa Rican Colon"), ("HRK", "Croatian Kuna"),
                                         ("CUP", "Cuban Peso"), ("CZK", "Czech Koruna"),("GMD", "Dalasi"),
                                         ("DKK", "Danish Krone"), ("MKD", "Denar"), ("DJF", "Djibouti Franc"),
                                         ("STD", "Dobra"), ("DOP", "Dominican Peso"), ("VND", "Dong"),
                                         ("XCD", "East Caribbean Dollar"), ("EGP", "Egyptian Pound"),
                                         ("SVC", "El Salvador Colon"), ("ETB", "Ethiopian Birr"), ("EUR", "Euro"),
                                         ("FKP", "Falkland Islands Pound"), ("FJD", "Fiji Dollar"), ("HUF", "Forint"),
                                         ("GIP", "Gibraltar Pound"), ("XAU", "Gold"), ("HTG", "Gourde"),
                                         ("PYG", "Guarani"), ("GNF", "Guinea Franc"), ("GYD", "Guyana Dollar"),
                                         ("HKD", "Hong Kong Dollar"), ("UAH", "Hryvnia"), ("ISK", "Iceland Krona"),
                                         ("INR", "Indian Rupee"), ("IRR", "Iranian Rial"), ("IQD", "Iraqi Dinar"),
                                         ("JMD", "Jamaican Dollar"), ("JOD", "Jordanian Dinar"),
                                         ("KES", "Kenyan Shilling"), ("PGK", "Kina"), ("LAK", "Kip"),
                                         ("KWD", "Kuwaiti Dinar"), ("MWK", "Kwacha"), ("AOA", "Kwanza"),
                                         ("MMK", "Kyat"), ("GEL", "Lari"), ("LVL", "Latvian Lats"),
                                         ("LBP", "Lebanese Pound"), ("ALL", "Lek"), ("HNL", "Lempira"),
                                         ("SLL", "Leone"), ("RON", "Leu"), ("LRD", "Liberian Dollar"),
                                         ("LYD", "Libyan Dinar"), ("SZL", "Lilangeni"), ("LTL", "Lithuanian Litas"),
                                         ("LSL", "Loti"), ("MGA", "Malagasy Ariary"), ("MYR", "Malaysian Ringgit"),
                                         ("MUR", "Mauritius Rupee"), ("MZN", "Metical"), ("MXN", "Mexican Peso"),
                                         ("MDL", "Moldovan Leu"), ("MAD", "Moroccan Dirham"), ("BOV", "Mvdol"),
                                         ("NGN", "Naira"), ("ERN", "Nakfa"), ("NAD", "Namibia Dollar"),
                                         ("NPR", "Nepalese Rupee"), ("ANG", "Netherlands Antillean Guilder"),
                                         ("ILS", "New Israeli Sheqel"), ("TMT", "New Manat"),
                                         ("TWD", "New Taiwan Dollar"), ("NZD", "New Zealand Dollar"),
                                         ("BTN", "Ngultrum"), ("KPW", "North Korean Won"), ("NOK", "Norwegian Krone"),
                                         ("PEN", "Nuevo Sol"), ("MRO", "Ouguiya"), ("PKR", "Pakistan Rupee"),
                                         ("XPD", "Palladium"), ("MOP", "Pataca"), ("TOP", "Pa’anga"),
                                         ("CUC", "Peso Convertible"), ("UYU", "Peso Uruguayo"),
                                         ("PHP", "Philippine Peso"), ("XPT", "Platinum"), ("GBP", "Pound Sterling"),
                                         ("BWP", "Pula"), ("QAR", "Qatari Rial"), ("GTQ", "Quetzal"), ("ZAR", "Rand"),
                                         ("OMR", "Rial Omani"), ("KHR", "Riel"), ("MVR", "Rufiyaa"), ("IDR", "Rupiah"),
                                         ("RUB", "Russian Ruble"), ("RWF", "Rwanda Franc"), ("SHP", "Saint Helena Pound"),
                                         ("SAR", "Saudi Riyal"), ("RSD", "Serbian Dinar"), ("SCR", "Seychelles Rupee"),
                                         ("XAG", "Silver"), ("SGD", "Singapore Dollar"),
                                         ("SBD", "Solomon Islands Dollar"), ("KGS", "Som"), ("SOS", "Somali Shilling"),
                                         ("TJS", "Somoni"), 	("ZAR", "South African Rand"), ("LKR", "Sri Lanka Rupee"),
                                         ("XSU", "Sucre"), ("SDG", "Sudanese Pound"), ("SRD", "Surinam Dollar"),
                                         ("SEK", "Swedish Krona"), ("CHF", "Swiss Franc"), ("SYP", "Syrian Pound"),
                                         ("BDT", "Taka"), ("WST", "Tala"), ("TZS", "Tanzanian Shilling"),
                                         ("KZT", "Tenge"), ("TTD", "Trinidad and Tobago Dollar"), ("MNT", "Tugrik"),
                                         ("TND", "Tunisian Dinar"), ("TRY", "Turkish Lira"), ("AED", "UAE Dirham"),
                                         ("USD", "US Dollar"), ("UGX", "Uganda Shilling"),
                                         ("COU", "Unidad de Valor Real"), ("CLF", "Unidades de fomento"),
                                         ("UYI", "Uruguay Peso en Unidades Indexadas (URUIURUI)"),
                                         ("UZS", "Uzbekistan Sum"), ("VUV", "Vatu"), ("KRW", "Won"),
                                         ("YER", "Yemeni Rial"), ("JPY", "Yen"), ("CNY", "Yuan Renminbi"),
                                         ("ZMK", "Zambian Kwacha"), ("ZWL", "Zimbabwe Dollar"), ("PLN", "Zloty"),
                                         )
desiredEntry.current()

amountEntry = Entry(root, width=30, relief=GROOVE, bd=3, textvariable=a_entry)
amountEntry.place(relx=0.5, y=310, anchor=CENTER)

# buttons -----------------------------
convertButton = Button(root, text="CONVERT", relief=RAISED, bd=5, bg="violetRed3", fg="white", command=conversion)
convertButton.place(relx=0.40, y=350, anchor=CENTER)

closeButton = Button(root, text="CLOSE", relief=RAISED, bd=5, bg="brown3", fg="white", command=close)
closeButton.place(relx=0.60, y=350, anchor=CENTER)


root.mainloop()
