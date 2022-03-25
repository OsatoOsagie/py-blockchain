import datetime
import json
import hashlib

class Blockchain:

    def __init__(self):
        self.chain = []
        self.mine_block('genesis')

    
    def add_block(self, previous_hash, data, nonce):

        block = {
            'index': len(self.chain) + 1,
            'nonce': nonce,
            'timestamp': str(datetime.datetime.now()),
            'data': data,
            'previous_hash': previous_hash
        }

        self.chain.append(block)
        return block

    def hash(self, block):
        encoded_block = json.dumps(block).encode()
        digest = hashlib.sha256(encoded_block).hexdigest()

        print("new digest: ", digest)
    
        return digest

    def mine_block(self, data):
        MAX_TRIES = 2000

        if len(self.chain) == 0:
            prev_hash = '0'
        else:
            prev_hash = self.hash(self.chain[-1])
        
        # picking a random starting nonce
        self.add_block(prev_hash, data, 9999)

        new_block = self.chain[-1]

        for i in range(MAX_TRIES):
            new_block['nonce'] = new_block['nonce']+1
            new_hash = self.hash(new_block)

            if new_hash[0] == '0':
                print('found good hash:', new_hash, 'after', i, 'attempts')
                return True

        print('failed to find good hash after max tries: ', MAX_TRIES)
        return False


blockchain = Blockchain()

print("-- chain ---")
print(blockchain.chain)

blockchain.mine_block("hello world")
blockchain.mine_block("another block")
blockchain.mine_block("more transactions")
blockchain.mine_block("even more transactions")

print("-- chain ---")
print(blockchain.chain)
