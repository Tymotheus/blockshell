# -*- coding: utf-8 -*-
# ===================================================
# ==================== META DATA ===================
# ==================================================
__author__ = "Daxeel Soni"
__url__ = "https://daxeel.github.io"
__email__ = "daxeelsoni44@gmail.com"
__license__ = "MIT"
__version__ = "0.11"
__maintainer__ = "Tymoteusz Ciesielski"

# ==================================================
# ================= IMPORT MODULES =================
# ==================================================
import hashlib
import datetime
import json
from colorama import Fore, Back, Style
import time


# ==================================================
# =================== BLOCK CLASS ==================
# ==================================================
class Block:
    """
        Create a new block in chain with metadata
    """
    def __init__(self, data, index=0, previousHash="", timestamp="", nonce=0, hash=""):
        self.index = index
        self.previousHash = previousHash
        self.data = data
        self.timestamp = str(datetime.datetime.now()) if len(timestamp) == 0 else timestamp
        self.nonce = 0
        self.hash = self.calculateHash() if len(hash) == 0 else hash

    def calculateHash(self):
        """
            Method to calculate hash from metadata
        """
        hashData = str(self.index) + str(self.data) + self.timestamp + self.previousHash + str(self.nonce)
        return hashlib.sha256(hashData.encode('utf-8')).hexdigest()

    def mineBlock(self, difficulty, miner=""):
        """
            Method for Proof of Work
        """
        print(Back.RED + "\n[Status] Mining block (" + str(self.index) + ") with PoW ...")
        startTime = time.time()

        while self.hash[:difficulty] != "0"*difficulty:
            self.nonce += 1
            self.hash = self.calculateHash()
        self.data = dict()
        self.data["transactions"] = [{"id": 0, "payer": "Block Reward", "beneficiary": miner, "amount": 50.0}]
        endTime = time.time()

        print(Back.BLUE + "[ Info ] Time Elapsed : " + str(endTime - startTime) + " seconds.")
        print(Back.BLUE + "[ Info ] Mined Hash : " + self.hash)
        print(Style.RESET_ALL)


# ==================================================
# ================ BLOCKCHAIN CLASS ================
# ==================================================
class Blockchain:
    """
        Initialize blockchain
    """
    def __init__(self, chain=[]):
        self.chain = [self.createGenesisBlock()] if len(chain) == 0 else chain
        self.difficulty = 3

    def createGenesisBlock(self):
        """
            Method create genesis block
        """
        return Block("Genesis Block")

    def addBlock(self, newBlock, miner=""):
        """
            Method to add new block from Block class
        """
        newBlock.index = len(self.chain)
        newBlock.previousHash = self.chain[-1].hash
        newBlock.mineBlock(self.difficulty, miner)
        self.chain.append(newBlock)

    def concatBlock(self, newBlock):
        """
        Method for concatanation of Blocks from file
        """
        self.chain.append(newBlock)


    def writeBlocks(self):
        """
            Method to write new mined block to blockchain
        """
        dataFile = open("chain.json", "w")
        chainData = []
        for eachBlock in self.chain:
            chainData.append(eachBlock.__dict__)
        dataFile.write(json.dumps(chainData, indent=4))
        dataFile.close()

    @classmethod
    def readBlocks(self):
        input = json.loads(open("chain.json", "r").read())
        return Blockchain([Block(**block) for block in input])

