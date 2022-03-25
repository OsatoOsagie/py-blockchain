import datetime
import json
import hashlib

class Blockchain:
    def __init__(self):
        self.chain = []
        self.add_block(proof=1, previous_hash='0')

    def add_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash
        }

        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1] 

    def proof_of_work(self, previous_proof):
        mining_attempt = 1
    
        # miners proof submitted
        new_proof = 1
        # status of proof of work
        check_proof = False
        
        while check_proof is False:
            print('Mining attempt', mining_attempt)
            mining_attempt += 1
            # problem and algorithm based off the previous proof and new proof
            data_to_hash = str(new_proof ** 2 - previous_proof ** 2)
            print('checking hash of ', data_to_hash)
            
            hash_operation = hashlib.sha256(data_to_hash.encode()).hexdigest()
            
            print('hash was: ', hash_operation)
            
            # check miners solution to problem, by using miners proof in cryptographic encryption
            # if miners proof results in 4 leading zero's in the hash operation, then:
            if hash_operation[:4] == '0000':
                print('Finally! - hash is good, mining success!')
                check_proof = True
            else:
                print('hash not good, keep on mining!')
                # if miners solution is wrong, give mine another chance until correct
                new_proof += 1
        return new_proof

    # generate a hash of an entire block
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

############# CREATE CHAIN ##############

blockchain = Blockchain()

def mine_block():
    # get the data we need to create a block
    previous_block = blockchain.get_last_block()
    previous_proof = previous_block['proof']
    new_proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    block = blockchain.add_block(new_proof, previous_hash)
    return block

############# TEST ##############

print("--- Chain initially ---")
print(blockchain)
    
print("\n\n--- Mining Block ---")
mine_block()

print("\n\n--- Chain ---")
print(blockchain.chain)
