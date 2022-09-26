#package delivery cost base on location and total amount.

total = int(input('Enter the amont for the item: '))
state = input('Enter the state in the USA: ').capitalize()
if state == 'Texas':
    if total<= 150:
        print('Shippng cost in teexas is $30')
    elif total > 150 and total <=250:
        print('shipping cost in texas $20')
    else:
        print('Shipping cost in texas is $5')
elif state == 'Verginai':
    if total<= 150:
        print('Shippng cost in verginia is $45')
    elif total > 150 and total <=250:
        print('shipping cost in verginia $25')
    else:
        print('Shipping cost in vergina is $10')
elif state == 'Florida':
    if total<= 150:
        print('Shippng cost in lforida is $23')
    elif total > 150 and total <=250:
        print('shipping cost in flforida is $15')
    else:
        print('Shipping cost in florida is $5')
elif state == 'New jersy':
    if total<= 150:
        print('Shippng cost in New jersy is $23')
    elif total > 150 and total <=250:
        print('shipping cost in New jersy is $15')
    else:
        print('Shipping cost  is free')
else:
    print("Invalid state name")