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
        self.pending_transactions = [] #empty pending transactions (we added them in 'transactions')
        self.chain.append(block) 
        return block
    
    #search blockchain for most recent block:
    @property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount  
            }
        self.pending_transactions.append(transaction) 
        return self.last_block['index']+1
    
    #f(x) to hash blocks:
    def hash(self, block):
        string_object = json.dumps(block, sort_keys = True) #encodes block (JSON object) into string
        block_string = string_object.encode() #encodes string into any encoding supported by Python
        
        raw_hash = hashlib.sha256(block_string) #sha256 is a hash function used by bitcoin, turns it into hexadecimal string
        hex_hash = raw_hash.hexdigest()
        
        return hex_hash
    
#Building the chain:        
blockchain = Blockchain()
t1 = blockchain.new_transaction('Satoshi', 'Loki', '4 BTC')
t2 = blockchain.new_transaction('Loki', 'Freyby', '2 BTC')
t3 = blockchain.new_transaction('Freyby', 'Satoshi', '1 BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction('Freyby', 'Loki', '5 BTC')
t5 = blockchain.new_transaction('Loki', 'Satoshi', '4 BTC')
t6 = blockchain.new_transaction('Satoshi', 'Freyby', '3 BTC')
blockchain.new_block(6789)

print('blockchain', blockchain.chain)