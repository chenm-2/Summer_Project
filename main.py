#Testing Code
import datetime as d
import hashlib as h
from unicodedata import name 
import random



class Block: # create a class called Block
    def __init__(self,index,timestamp,data ,prevhash): # declare an initial method that defines a block, a block contains the following information
        self.index = index # a block contains an ID
        self.timestamp =timestamp # a block contains a timestamp
        self.data = data # a block contains some transactions
        self.prevhash =prevhash # a block contains a hash of the previous block
        self.hash =self.hashblock() # a block contains a hash, the hash is obtained by hashing all the data contained in the block

    def hashblock (self): # define a method for data encryption, this method will retain a hash of the block
        block_encryption=h.sha256(str(random.getrandbits(256)).encode('utf-8')) # We need a sha256 function to hash the content of the block, so let's declare it here
        block_encryption.update(bytes(str(self.index), 'utf-8')+bytes(str(self.timestamp),'utf-8')+bytes(str(self.data), 'utf-8')+bytes(str(self.prevhash), 'utf-8')) # to encrypt the data in the block, We need just to sum everything and apply the hash function on it
        return block_encryption.hexdigest() # let's return that hash result 

    def genesisblock(): # this method is for generating the first block named genesis block
        return Block(0,d.datetime.now(),"genesis block transaction"," ") # return the genesis block

    def newblock(lastblock): # get the next block, the block that comes after the previous block (prevblock+1)
        index = lastblock.index+1 # the id of this block will be equals to the previous block + 1, which is logic
        timestamp = d.datetime.now() # The timestamp of the next block
        hashblock = lastblock.hash # the hash of this block
        data = "Transaction " +str(index) # The data or transactions containing in that block
        return Block(index,timestamp,data,hashblock)# return the entire block


def main():
        
    blockchain = [Block.genesisblock()] # now it's time to initialize our blockchain with a genesis block in it
    prevblock = blockchain[0] # the previous block is the genesis block itself since there is no block that comes before it at the indice 0 
    
    for i in range (0,5): # the loop starts from here, we will print 5 blocks, this number can be increased if needed
        addblock = Block.newblock(prevblock) #  the block to be added to our chain 
        blockchain.append(addblock) # we add that block to our chain of blocks
        prevblock =addblock #now the previous block becomes the last block so we can add another one if needed

        print("Block ID #{} ".format(addblock.index)) # show the block id
        print("Timestamp:{}".format(addblock.timestamp))# show the block timestamp
        print("Hash of the block:{}".format(addblock.hash))# show the hash of the added block
        print("Previous Block Hash:{}".format(addblock.prevhash))# show the previous block hash
        print("data:{}\n".format(addblock.data))# show the transactions or data contained in that block



if __name__=="__main__":
    main()


    