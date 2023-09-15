# Exchange Rates Web Application

This web application fetches exchange rate data from the National Bank of Ukraine and writes it to a Google Sheet.
## Requirements

To run this application, make sure you have the following Python libraries installed:

- Flask==2.2.5
- google-api-python-client==2.99.0
- google-auth-oauthlib==1.1.0
- requests==2.31.0
- gunicorn==20.0.4

## Usage

You can use the API by making a GET request to the following URL:
```commandline
https://exchangerates1-68bbdcfca525.herokuapp.com/exchange_rates/?update_from=YYYY-MM-DD&update_to=YYYY-MM-DD
```

Replace `YYYY-MM-DD` with the desired date range. Two arguments are required:

- `update_from`: The start date in the format `YYYY-MM-DD`.
- `update_to`: The end date in the format `YYYY-MM-DD`.


