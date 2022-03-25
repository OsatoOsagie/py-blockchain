# Python Hashlib Exercise

## Objective
The object of this exercise is to explore the concept of a hash, and gain some familiarity with python hashlib.

---

## Level 1 - Get the SHA256 hash of a random string

```
import hashlib

hash = hashlib.sha256("hello world".encode('utf-8')).hexdigest()

print(hash)
```

In a python file, enter and run the above code.

Verify that if repeated the hash is accurately reproduced for the same string, and that the hash changes for small changes in the string.

---

## Level 2 - Get the hash of a file

```
import hashlib

file = "<insert-file-path>' # Location of the file
BLOCK_SIZE = 65536 # The size of each read from the file

file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
with open(file, 'rb') as f: # Open the file to read it's bytes
    fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
    while len(fb) > 0: # While there is still data being read from the file
        file_hash.update(fb) # Update the hash
        fb = f.read(BLOCK_SIZE) # Read the next block from the file

print (file_hash.hexdigest()) # Get the hexadecimal digest of the hash
```

Read and understand the above code.

In a python file, enter and run the above code, setting the file varible to the path to a file on your system.

Verify that if repeated the hash is accurately reproduced for the same file.

---

## Level 3 - Re-organise to a function
Reorganise the above code into a python function that takes a file path and returns the hex digest of that file.

```
def get_file_hash(file_path):
    ... YOUR CODE HERE ...
```

Optionally add an ```if __name__ == '__main__':``` section so that this function is called when your file is run as a script.

Verify that for a given file the hash is reproduced accurately.

Verify that a small change in a file causes the hash to change.
