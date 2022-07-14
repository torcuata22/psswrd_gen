import hashlib
import json
from time import time  

class Blockchain():
   def __init__(self):
       self.chain = []
       self.pending_transactions = []
       