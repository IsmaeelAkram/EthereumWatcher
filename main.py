from dotenv import load_dotenv

load_dotenv()
import coinbasepro as cbp
import chalk
import os
import sys
import decimal
import time

client = cbp.AuthenticatedClient(
    secret=os.getenv("COINBASE_SECRET"),
    passphrase=os.getenv("COINBASE_API_PASSPHRASE"),
    key=os.getenv("COINBASE_API_KEY"),
)
while True:
    target_price = decimal.Decimal(sys.argv[1])

    eth = client.get_product_ticker("ETH-USD")
    eth_price = eth.get("price")
    if eth_price >= target_price:
        sell_amount = float(sys.argv[2])
        client.place_market_order(product_id="ETH-USD", side="sell", size=sell_amount)
        print(chalk.green("Sold!"))
        os.system(f"say Sold at {eth_price} dollars!")
        sys.exit()
    else:
        print(chalk.yellow("Not enough: " + str(eth_price)))
    time.sleep(2)