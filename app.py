# В файле app.py написать код, который сам генерирует приватный ключ и адрес к нему
# и после этого проверяет баланс эфира в сети эфира (брутфорсим кошельки).
# Код должен работать асинхронно.

import asyncio
import time

from eth_async.models import Networks
from eth_async.client import Client

async def brootforce():
    while True:
        client = Client(network=Networks.Ethereum)
        balance = await client.wallet.balance()
        print(f'EVM address: {client.account.address}; | '
              f'EVM PK: {client.account._private_key.hex()}; | '
              f'Balance in {client.network.name} : {balance}')

        if balance.Wei != 0:
            with open('lucky_wallets.txt', 'a') as f:
                f.write(f'EVM address: {client.account.address}; | EVM PK: {client.account._private_key.hex()}; | Balance in {client.network.name} : {balance}')


async def main(count):
    tasks = []
    threads = count
    while threads > 0:
        tasks.append(asyncio.create_task(brootforce()))
        threads -= 1

    print(len(tasks))
    time.sleep(10)

    # await asyncio.wait(tasks)
    # 2ой вариант
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main(10))
