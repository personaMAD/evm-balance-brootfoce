import asyncio

from eth_async.client import Client
from eth_async.models import Networks
from eth_async.transactions import Transactions

from data.config import pk, seed


async def main():
    client = Client(private_key=pk, network=Networks.Ethereum)
    # contract = await client.contracts.default_token(contract_address='0xaf88d065e77c8cc2239327c5edb3a432268e5831')
    # print(type(contract))
    # print(await contract.functions.decimals().call())

    print((await client.wallet.balance()).Wei)
    # print((await client.wallet.balance(token_address='0xaf88d065e77c8cc2239327c5edb3a432268e5831')).Ether)
    #
    # print('nonce:', await client.wallet.nonce())


    # print(await client.w3.eth.gas_price)
    # print('= = = = =')
    # # gas_price = await Tran
    # gas_price = await Transactions.gas_price(w3=client.w3)
    # print(await gas_price)
    # print('= = = = =')
    # w3ekz = client.w3
    # ЧЕРЕЗ transactions (экземпляр класса Transactions)
    # gas_price = await client.transactions.gas_price(w3=w3ekz)
    # print(await gas_price)
    # print('= = = = =')

    # НАПРЯМУЮ ЧЕРЕЗ КЛАСС TRANSACTIONS
    gas_price = await Transactions.gas_price(w3=client.w3)
    print(gas_price.Wei)

    # ЧЕРЕЗ экземпляр класса Client без передачи объекта Web3 в метод gas_price2() из класса Transactions
    gas_price2 = await client.transactions.gas_price2()
    print(gas_price2.Wei)


if __name__ == '__main__':
    asyncio.run(main())
