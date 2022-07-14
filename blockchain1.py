import hashlib
import json
from time import time  

class Blockchain():
    def __init__(self):
       self.chain = []
       self.pending_transactions = []
       self.new_block() #this will add each block to the chain
       
    def new_block(self, proof, previous_hash = None):
        block ={
            'index': len(self.chain) + 1, #used to reference individual block
            'timestamp' : time(), #stamps the block when it's created (users can check when they're transactionw as confirmed)
            'transactions': self.pending_transactions, #pending transactions will be included in new block
            'proof': proof, 
            'previous_hash': previous_hash or self.hash(self.chain[-1]) #hashed version of most recent approved block
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block