import requests

from config import BANKGOV_ENDPOINT

def get_usd_to_uah_exchange_rates(update_from, update_to):
    params = {
        "json": True,
        "valcode": "USD",
        "start": update_from,
        "end": update_to
    }

    response = requests.get(BANKGOV_ENDPOINT, params=params)

    return response.json()

def transform_data_for_google_sheets(existing_data):
    raw_data = [{'exchangedate': rate['exchangedate'], 'rate_per_unit': rate['rate_per_unit']} for rate in existing_data]
    header_row = ["exchangedate", "rate_per_unit"]
    transformed_data = []
    transformed_data.append(header_row)

    for entry in raw_data:
        transformed_entry = [entry["exchangedate"], entry["rate_per_unit"]]
        transformed_data.append(transformed_entry)

    return transformed_data