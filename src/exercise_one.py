
import hashlib

# In a python file, enter and run the above code.
# Verify that if repeated the hash is accurately reproduced for the same string, 
# and that the hash changes for small changes in the string.

if __name__ == "__main__":

    def get_file_hash(file_path):

        file = file_path
        BLOCK_SIZE = 65536 # The size of each read from the file

        file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` 


        f= open(file, 'rb') # Open the file to read it's bytes

        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = f.read(BLOCK_SIZE) # Read the next block from the file

        print ("FILE HASH- " + file_hash.hexdigest()) # Get the hexadecimal digest of the hash

    get_file_hash("/Users/aesthetic/Desktop/py-blockchain/Osato Osagie - CV.pages")