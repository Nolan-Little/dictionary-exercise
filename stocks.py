stock_dict = {
    'GM': 'General Motors',
    'CAT': 'Caterpillar',
    'EK': 'Eastman Kodak'
}

purchases = [
    ('GM', 27, '10-oct-2018', 120),
    ('GM', 49, '14-oct-2018', 101),
    ('CAT', 12, '10-oct-2018', 78),
    ('EK', 84, '10-oct-2018', 17),
]


def calculate_purchase_history(purchases, stock_dict):

    '''Convert a dictionary of stock ticker abbreviations
        and a stock purchase history  in to a portfolio report.

    Keyword arguments:
    purchases -- a list of purchases as a tuple with following format:
                    at index[0]: stock abbreviation
                    at index[1]: quantity of stocks purchased
                    at index[2]: date of purchase
                    at index[3]: stock price at time of purchase
    stock_dict-- a dictionary of stock abbreviations as keys
                 with the stocks full name as the value

    Returns: none, prints formatted report to console.

    '''
    grouped_purchases_report = {}
    for purchase in purchases:
        stock_abbrev = purchase[0]
        purchase_quantity = purchase[1]
        purchase_date = purchase[2]
        purchase_price = purchase[3]
        stock_full_name = stock_dict[stock_abbrev]
        print(
            f'On {purchase_date}, I purchased ${purchase_quantity * purchase_price} of {stock_full_name} stock.')

        try:
            grouped_purchases_report[stock_abbrev].append(purchase)

        except:
            grouped_purchases_report[stock_abbrev] = list()
            grouped_purchases_report[stock_abbrev].append(purchase)

    for stock_abbrev, purchase_list in grouped_purchases_report.items():
        print(f'\n*--------{stock_abbrev}---------*')
        total_portfolio_value = 0
        for purchase in purchase_list:
            purchase_quantity = purchase[1]
            purchase_price = purchase[3]
            total_portfolio_value = purchase_price * purchase_quantity
            print(f'       {purchase}')
        print(f'Total value of {stock_abbrev} in portfolio: ${total_portfolio_value}\n')


calculate_purchase_history(purchases, stock_dict)
