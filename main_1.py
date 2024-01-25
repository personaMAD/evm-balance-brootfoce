from web3 import Web3

from web3.middleware import geth_poa_middleware
from eth_account.signers.local import LocalAccount

from data.config import pk, seed
from eth_async.utils import utils


eth_rpc = 'https://eth.llamarpc.com'
arb_rpc = 'https://arbitrum.llamarpc.com'


def get_private_from_seed(seed: str) -> str:
    web3 = Web3(provider=Web3.HTTPProvider(endpoint_uri=arb_rpc))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    web3.eth.account.enable_unaudited_hdwallet_features()

    web3_account: LocalAccount = web3.eth.account.from_mnemonic(seed)

    private_key = web3_account._private_key.hex()
    address = web3_account.address
    return private_key


# подключение
web3 = Web3(Web3.HTTPProvider(endpoint_uri=arb_rpc)) #создаем объект класса Web3
print(f"Is connected: {web3.is_connected()}")


# получение параметров из блокчейна
print(f"gas price: {web3.eth.gas_price} WEI")
print(f"current block number: {web3.eth.block_number}")
print(f"number of current chain is {web3.eth.chain_id}")


# проверка баланса
address = web3.eth.account.from_key(private_key=pk).address
address = address.lower()
print(address)
wallet_address = Web3.to_checksum_address( #web3py работает ТОЛЬКО с чексум адресами (большие+маленькие буквы адреса)
    address
)
print(wallet_address)

balance = web3.eth.get_balance(wallet_address)
print(f"balance of {wallet_address} = {balance} WEI")

# перевод в разные системы измерения
ether_balance = Web3.from_wei(balance, 'ether')
print(ether_balance, 'ETH')
print(Web3.from_wei(balance, 'gwei'), 'GWEI')
print(Web3.to_wei(ether_balance, 'ether'), 'WEI')
