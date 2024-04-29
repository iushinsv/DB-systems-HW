import bigchaindb_driver
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb = BigchainDB('http://localhost:9984')

# Генерация ключевых пар для участников системы
alice = generate_keypair()
bob = generate_keypair()

# Создание актива (asset)
asset_data = {'message': 'Hello BlockchainDB!'}
metadata = {'description': 'My first BlockchainDB transaction'}

# Подготовка транзакции создания актива
prepared_creation_tx = bdb.transactions.prepare(
    operation='CREATE',
    signers=alice.public_key,
    asset=asset_data,
    metadata=metadata
)

# Выполнение транзакции создания актива
fulfilled_creation_tx = bdb.transactions.fulfill(
    prepared_creation_tx,
    private_keys=alice.private_key
)

# Отправка и подтверждение транзакции
sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)
print(sent_creation_tx)

# Запрос актива по его ID
asset_id = sent_creation_tx['id']
retrieved_asset = bdb.assets.get(asset_id)
print(retrieved_asset)

# Запрос транзакции по ее ID
tx_id = sent_creation_tx['id']
retrieved_tx = bdb.transactions.get(tx_id)
print(retrieved_tx)
