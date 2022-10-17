
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib
 
@dataclass
# Record class to store the sender, receiver and amount in a Blockchain ledger system.
class Record:
    # Sender of the Record
    sender : str
    # Receiver of the Record
    receiver : str
    # Amount of the Record
    amount: float


@dataclass
# Block class to store the Record, previous hash and timestamp of the block.
class Block:
    # The Record for this Block entry
    record: Record
    # The creator_id
    creator_id: int
    # The hash of the previous Block's Record
    prev_hash: str = "0"
    # The timestamp that this entry was added
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    # The nonce variable
    nonce: int = 0

    # Return a hash of the Block, which is based on the Record, creator_id, 
    # timestamp, prev_hash and nonce. 
    def hash_block(self):
        sha = hashlib.sha256()

        record = str(self.record).encode()
        sha.update(record)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()


@dataclass
# PyChain class to store a list of Block objects.
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    # Returns the proof of work. 
    def proof_of_work(self, block):

        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        print("Wining Hash", calculated_hash)
        return block

    # Adds a Block to the Blockchain
    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    # Returns whether the Blockchain is valid.   This iterates through the 
    # Blockchain and validates each of the hashes. 
    def is_valid(self):
        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:
            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            block_hash = block.hash_block()

        print("Blockchain is Valid")
        return True


@st.cache(allow_output_mutation=True)
#
# The Streamlit Application for displaying the Blockchain
#
def setup():
    print("Initializing Chain")
    return PyChain([Block("Genesis", 0)])


st.markdown("# PyChain")
st.markdown("## Store a Transaction Record in the PyChain")

pychain = setup()

# 
# Input fields for the Blockchain entry.
# 
input_sender = st.text_input("Sender")
input_receiver = st.text_input("Receiver")
input_amount = st.text_input("Amount")

amount = 0
try: 
    amount = float(input_amount)
except ValueError:
    amount = 0

#
# The 'Add Block' button.   This will add a Block to the Blockchain.
#
if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    record = Record(
        sender = input_sender, 
        receiver = input_receiver, 
        amount = input_amount)
    new_block = Block(
        record=record,
        creator_id=42,
        prev_hash=prev_block_hash
    )

    pychain.add_block(new_block)
    st.balloons()


#
# The 'Pychain Ledger' for displaying the Block entries. 
#
st.markdown("## The PyChain Ledger")

pychain_df = pd.DataFrame(pychain.chain).astype(str)
st.write(pychain_df)

difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 2)
pychain.difficulty = difficulty

st.sidebar.write("# Block Inspector")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

st.sidebar.write(selected_block)


#
# Button for validating the blockchain.
#
if st.button("Validate Chain"):
    st.write(pychain.is_valid())
