import json
from datetime import datetime


def read_json_file(path: str) -> list[dict]:
    with open(path, encoding='utf-8') as json_file:
        data = json.load(json_file)
        if isinstance(data, list):
            return data
        else:
            return []


def get_mask_the_bankcard(card_number: str) -> str:
    card_number = "".join(filter(str.isdigit, card_number))
    if len(card_number) != 16:
        return "Не верный номер карты"

    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"

    return masked_number


def get_mask_the_bank_account(account_number: str) -> str:
    account_number = "".join(filter(str.isdigit, account_number))
    if len(account_number) != 20:
        return "Не верный номер счета"

    masked_number = f"**{account_number[-4:]}"

    return masked_number


def get_mask_bankcard_account(number_name: str) -> str:
    split_number_name = number_name.split()

    if "Счет" in split_number_name:
        mask_bank_account = get_mask_the_bank_account(split_number_name[-1])
        return ' '.join(split_number_name[:-1]) + " " + mask_bank_account
    else:
        mask_bankcard = get_mask_the_bankcard(split_number_name[-1])
        return ' '.join(split_number_name[:-1]) + " " + mask_bankcard


def convert_date(date_string: str) -> str:
    date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date
