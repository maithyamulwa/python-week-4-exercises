from typing import Dict, Tuple, List, Generator, Set

def parse_txid(txid: str) -> tuple:
    """
    Converts a hexadecimal txid string into a tuple of byte pairs.
    Example: 'deadbeef' -> ('de', 'ad', 'be', 'ef')
    """
    return tuple(txid[i:i+2] for i in range(0, len(txid), 2))

def create_utxo(txid: str, vout: int, amount: int) -> dict:
    """
    Creates a dictionary representing a UTXO with the given txid, vout, and amount.
    """
    return {
        'txid': txid,
        'vout': vout,
        'amount': amount
    }

def update_utxo(utxo: dict, new_amount: int) -> None:
    """
    Updates the 'amount' field in a UTXO dictionary to a new value.
    """
    utxo.update({'amount': new_amount})

def unpack_utxo(utxo: dict) -> str:
    """
    Unpacks a UTXO dictionary and returns a formatted string representation.
    """
    txid, vout, amount = utxo['txid'], utxo['vout'], utxo['amount']
    return f"TXID: {txid}, VOUT: {vout}, Amount: {amount} satoshis"

def swap_addresses(addr1: str, addr2: str) -> tuple:
    """
    Swaps two Bitcoin addresses and returns them in reversed order.
    """
    return addr2, addr1

def unique_addresses(addresses: list) -> set:
    """
    Returns a set of unique Bitcoin addresses from the provided list.
    """
    return set(addresses)

class BitcoinWallet:
    def __init__(self):
        """
        Initializes the wallet with an empty UTXO set.
        """
        self.utxos: Dict[str, dict] = {}
    
    def add_utxo(self, utxo: Dict) -> None:
        """
        Adds a UTXO to the wallet using a unique txid:vout key.
        """
        key = f"{utxo['txid']}:{utxo['vout']}"
        self.utxos[key] = utxo
    
    def get_balance(self) -> float:
        """
        Returns the total balance of all UTXOs in the wallet.
        """
        return sum(utxo['amount'] for utxo in self.utxos.values())

class TransactionPool:
    def __init__(self):
        """
        Initializes an empty transaction pool.
        """
        self.tx_pool: Set[str] = set()
    
    def add_transaction(self, txid: str) -> bool:
        """
        Adds a txid to the transaction pool.
        Returns True if it was not already present, False otherwise.
        """
        if txid in self.tx_pool:
            return False
        self.tx_pool.add(txid)
        return True
    
    def get_pool_size(self) -> int:
        """
        Returns the total number of unique transactions in the pool.
        """
        return len(self.tx_pool)

def block_height_generator(start: int, end: int) -> Generator[int, None, None]:
    """
    Yields block heights from start to end (exclusive).
    """
    for height in range(start, end):
        yield height