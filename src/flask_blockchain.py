import datetime
import json
import hashlib
from flask import Flask, jsonify


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

    # check if the blockchain is valid
    def is_chain_valid(self, chain):
        # get the first block in the chain and it serves as the previous block
        previous_block = chain[0]
        # an index of the blocks in the chain for iteration
        block_index = 1
        while block_index < len(chain):
            # get the current block
            block = chain[block_index]
            # check if the current block link to previous block has is the same as the hash of the previous block
            if block["previous_hash"] != self.hash(previous_block):
                return False

            # get the previous proof from the previous block
            previous_proof = previous_block['proof']

            # get the current proof from the current block
            current_proof = block['proof']

            # run the proof data through the algorithm
            hash_operation = hashlib.sha256(str(current_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            # check if hash operation is invalid
            if hash_operation[:4] != '0000':
                return False
            # set the previous block to the current block after running validation on current block
            previous_block = block
            block_index += 1
        return True


app = Flask(__name__)

blockchain = Blockchain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    # get the data we need to create a block
    previous_block = blockchain.get_last_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    block = blockchain.add_block(proof, previous_hash)
    response = {'message': 'Block mined!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


app.run(host='0.0.0.0', port=5000)