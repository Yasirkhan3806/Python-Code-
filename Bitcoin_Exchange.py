import json
import requests
import sys

def main():
    calculating_result()

def getting_n():
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit()

def getting_api():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except requests.RequestException:
        print("Sorry For The Inconvienance, Try Later")

 # python Bitcoin_Exchange.py

def calculating_result():
    final_value = getting_n() * getting_api()
    print(f"${final_value}")

if __name__ == '__main__':
    main()
