from polygon import RESTClient
import config


def main():
    key = config.api_key

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        resp = client.stocks_equities_daily_open_close("AMD", "2021-06-11")
        print(f"On: {resp.from_} AMD opened at {resp.open} and closed at {resp.close}")


if __name__ == '__main__':
    main()

