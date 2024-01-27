from utils import convert_date, get_mask_bankcard_account


def show_last_five_operations(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]:

    executed_transactions = [transaction for transaction in transactions if transaction.get('state') == state]

    sorted_transaction = sorted(executed_transactions, key=lambda x: x.get('date', ''), reverse=True)

    last_five_operations = []
    for transaction in sorted_transaction[:5]:
        transaction['date'] = convert_date(transaction['date'])
        if transaction.get('from'):
            transaction['from'] = get_mask_bankcard_account(transaction['from'])
        transaction['to'] = get_mask_bankcard_account(transaction['to'])
        last_five_operations.append(transaction)

    return last_five_operations
