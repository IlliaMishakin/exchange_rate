from flask import Flask, request, make_response

from app.currency_rates import get_usd_to_uah_exchange_rates, transform_data_for_google_sheets
from app.gsheet_manager import write_to_google_sheet, authenticate_google_sheets
from app.validate_args import validate_date_format


app = Flask(__name__)


@app.route('/exchange_rates/', methods=['GET'])
def get_exchange_rates():
    update_from = request.args.get('update_from')
    update_to = request.args.get('update_to')

    if not validate_date_format(update_to) or not validate_date_format(update_from):
        response = make_response('<html><body><h1>Invalid argument format</h1></body></html>')
        response.status_code = 404
        return response

    creds = authenticate_google_sheets()
    rates_data_raw = get_usd_to_uah_exchange_rates(update_from.replace("-", ""),
                                                   update_to.replace("-", ""))
    rates_data = transform_data_for_google_sheets(rates_data_raw)
    write_to_google_sheet(creds, rates_data)

    response = make_response('<html><body><h1>Success</h1></body></html>')
    response.status_code = 200

    return response




