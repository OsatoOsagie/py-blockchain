import datetime
import json
import hashlib
from tkinter import W
from tkinter.tix import Tree
from random import randint

class Blockchain:

    def __init__(self):
        self.chain = []
        self.add_block(1,0)

    def add_block(self, proof, previous_hash):
        block = {
        'index': len(self.chain) + 1,
        'timestamp': str(datetime.datetime.now()),
        'previous_hash': previous_hash,
         'proof': proof}
        self.chain.append(block)
        return block

    def hash(self, block):
      
        encoded_block = json.dumps(block,sort_keys=True).encode()
        digest = hashlib.sha256(encoded_block).hexdigest()
    
        return digest

    def proof_of_work(self, previous_proof):
        MAX_TRIES = 2000
        new_proof = randint(10, 1000)
        
        new_hash= self.hash(new_proof ** 2 - previous_proof ** 2)
        while new_hash.startswith('0000') !=True:
            new_proof+=1
            new_hash= self.hash(new_proof ** 2 - previous_proof ** 2)
        

        return new_proof 

blockchain = Blockchain()
def mine_block():
    new_proof=blockchain.proof_of_work(blockchain.chain[-1]['proof'])
    print(new_proof)
    previous_hash= blockchain.hash(blockchain.chain[-1])
    print(previous_hash)
    blockchain.add_block(new_proof,previous_hash)
    print(blockchain.chain[-1])

mine_block()



		