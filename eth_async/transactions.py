# По аналогии с классами Contracts и Wallet создать класс "Transactions"
# и добавить в него СТАТИЧЕСКИЙ метод "gas_price",
# который принимает в себя объект (экземпляр класса) w3 и возвращает текущий газ в сети в TokenAmount

from __future__ import annotations
from typing import TYPE_CHECKING

from web3 import Web3

from .models import TokenAmount

if TYPE_CHECKING:
    from .client import Client


class Transactions:
    w3: Web3

    def __init__(self, client: Client) -> None:
        self.client = client

    #СТАТИЧЕСКИЙ МЕТОД
    @staticmethod
    async def gas_price(w3: Web3) -> TokenAmount:
        return TokenAmount(amount=await w3.eth.gas_price, wei=True)

    # ЧЕРЕЗ НЕ СТАТИЧЕСКИЙ МЕТОД
    async def gas_price2(self) -> TokenAmount:
        return TokenAmount(amount=await self.client.w3.eth.gas_price, wei=True)
