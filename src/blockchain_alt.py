import datetime
import json
import hashlib

class Blockchain:

    def __init__(self):
        self.chain = []
        self.mine_block("genesis")

    
    def add_block(self, data, nonce):

        last_hash = '0'
        if len(self.chain) > 0:
            last_hash = self.hash_last_block()

        block = {
            'index': len(self.chain) + 1,
            'nonce': nonce,
            'timestamp': str(datetime.datetime.now()),
            'data': data,
            'previous_hash': last_hash
        }

        self.chain.append(block)

        return block


    def hash_last_block(self):
        new_hash = hashlib.sha256( json.dumps(self.chain[-1] ).encode('utf-8') )

        return new_hash.hexdigest()


    def mine_block(self, data):
        self.add_block(data, 9999)

        # calculate correct nonce for the just added block

        MAX_TRIES = 100000
        for i in range(MAX_TRIES):
            new_hash = self.hash_last_block()

            if new_hash.startswith('00'):
                print('found good hash after', i, 'attempts')
                return    

            self.chain[-1]['nonce'] = self.chain[-1]['nonce'] + 1

        print('unable to find hash after', MAX_TRIES,  'attempts')



blockchain = Blockchain()

print('--- chain ---')
print(blockchain.chain)


blockchain.mine_block("second block!")
blockchain.mine_block("third block!")


print('--- chain ---')
print(blockchain.chain)

