import hashlib

def hashgenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

# this class is a prototype of a block in the blockchain
class Block :
    def __init__(self, data, prev_hash, curr_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.curr_hash = curr_hash

# this class is a prototype of the whole blockchain
class Blockchain :
    def __init__(self):
        gen_data = "hello my name is Arya"
        prev_hash = "0000"
        curr_hash = hashgenerator("genesis hash")
        genesis_block = Block(gen_data, prev_hash, curr_hash)
        self.chain = [genesis_block]
    def add_block(self, data):
        # the prev_hash of the current block is the curr_hash of the previous block
        prev_hash = self.chain[-1].curr_hash
        # we have to pass unique values in the hashgen... function
        curr_hash = hashgenerator(data+prev_hash)
        curr_block = Block(data, prev_hash, curr_hash)
        self.chain.append(curr_block)

# now we start creating the blockchain
bc = Blockchain()
bc.add_block("1")
bc.add_block("2")
bc.add_block("3")

for block in bc.chain :
    print(block.__dict__)