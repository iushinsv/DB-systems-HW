
## Step 1: Now let’s open up a new Python file and import the necessary modules.
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit

#Step 2: Register Mike and Sarah as users by generating their public/private key pair.

mike, sarah = generate_keypair(), generate_keypair()
# Step 3: Set up the root URL. If you are running the node on your local device, then it can be localhost.

bdb_root_url = ‘https://localhost:8080’
#Step 4: Now let us create the painting as an asset and generate it under Mike’s ownership.

bdb = BigchainDB(bdb_root_url)
painting_asset = {
    ‘data’: {
        ‘painting’: {
            ‘name’: ‘New Mona Lisa’,
            ‘painter’: ‘Mike’
        },
    },
}
 
painting_asset_metadata = {
    ‘date_started’: ‘10/1/2021’
    ‘date_completed’: ‘12/3/2021’
}
prepared_creation_tx = bdb.transactions.prepare(
    operation=’CREATE’,
    signers=mike.public_key,
    asset=painting_asset,
    metadata=painting_asset_metadata
)
 
fulfilled_creation_tx = bdb.transactions.fulfill(
    prepared_creation_tx,
    private_keys=mike.private_key
)
#Step 5: Finally, we upload the asset as a node into the database.

sent_creation_tx = bdb.transactions.send_commit(fulfilled_creation_tx)
#Step 6: Now we will prepare the transfer of the asset ownership from Mike to Sarah.

txid = fulfilled_creation_tx[‘id’] 
asset_id = txid
transfer_asset = {
    ‘id’: asset_id
}
output_index = 0
output = fulfilled_creation_tx[‘outputs’][output_index]
transfer_input = {
    ‘fulfillment’: output[‘condition’][‘details’],
    ‘fulfills’: {
        ‘output_index’: output_index,
        ‘transaction_id’: fulfilled_creation_tx[‘id’]
    },
    ‘owners_before’: output[‘public_keys’]
}
prepared_transfer_tx = bdb.transactions.prepare(
    operation=’TRANSFER’,
    asset=transfer_asset,
    inputs=transfer_input,
    recipients=sarah.public_key,
)
fulfilled_transfer_tx = bdb.transactions.fulfill(
    prepared_transfer_tx,
    private_keys=mike.private_key,
)
#Step 7: Finally, we send the commit to the database to complete the TRANSFER transaction.

sent_transfer_tx = bdb.transactions.send_commit(fulfilled_transfer_tx)
#Step 8: Let us confirm that the transactions went through as planned and the ownership has been assigned correctly from Mike to Sarah.

print(“Is Sarah the owner of the painting?”,
    sent_transfer_tx[‘outputs’][0][‘public_keys’][0] == sarah.public_key)
print(“Was Mike the previous owner of the painting?”,
    fulfilled_transfer_tx[‘inputs’][0][‘owners_before’][0] == mike.public_key)