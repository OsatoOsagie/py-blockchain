# Python Blockchain

## Objective
The object of this exercise is to write a very simple Python blockchain implementation.

---

## Data Structures:

We will create a class called ```Blockchain``` that will encapsulate our chain.

This class will have a python as a class variable to represent the chain of blocks.

Each block will be represented by a python dictionary (for now no data in the block):
```
    block = {
        'index': # the integer position of this block in the chain,
        'timestamp': # when this block was created,
        'proof': # proof of work for this block,
        'previous hash': # hash of the prev block
    }
```

---

## Methods

### 1. ```__init__```
Initialise the blockchain

We'll add an ```__init__``` method to initialise the chain.

```self.chain = []```

---

### 2. ```def add_block(self, proof, previous_hash)```
Create a function to create a new block, add it to the chain and return the new block:


```proof```: a number needed to get an acceptable hash for this block

```previous_hash```: The hash of the last block in the chain.

Add a call to this function from the ```__init__``` function setting proof=1 and previous_hash='0'. This is our "genesis" block.

---

### 3. ```def hash(self, block)```
Add a class method that hashes the json dump of a block.

We will need to make sure the keys of the block dictionary are kept in the same order (why?).

e.g. ```json.dumps(block, sort_keys=True).encode()```

---

### 4. ```proof_of_work(self, previous_proof)```
Add a proof of work function. This will run a loop trying to find an acceptable hash of a combination of two numbers:

* a piece of the last block ("previous_proof")
* a random number ("new_proof")

In our case we will combine these two numbers as:
```str(new_proof ** 2 - previous_proof ** 2)```

So this function will run a loop incrementing ```new_proof``` each time.

In the loop body it will calculate:
```hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2))```

If the above hash starts with four zeros we say the block is mined i.e. work has been done and proven to be done.

At this point ```new_proof``` is returned.


### 5. OUTSIDE OF THE CLASS: create a block chain object
``` blockchain = Blockchain()```

### 6. OUTSIDE OF THE CLASS: ```def mine_block()```
A method that will mine a new block for our chain:
1. Call ```blockchain.proof_of_work``` with the ```proof``` variable from the last block in the chain. This gives us the next ```proof``` variable. We'll call this ```new_proof```.
2. Get the hash of the last block in the chain. We'll call this ```previous_hash```
3. Add a block with ```new_proof``` and ```previous_hash```

### 7. Test
Add some lines printing the contents of the chain and calling ```mine_block```

Verify that you understand what's happening.

### 8. Add flask
Try running the enhanced version ```flask_blockchain.py```. This allows you to interact with the chain a little easier in a web browser.