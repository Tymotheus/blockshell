Development log

16.01.2023
The first problem I encountered was the fact,
that you can in fact start a shell session with a blockchain,
but when you quit it you can not restore it and you need to recreate it from scratch
(even though the blockchain is saved in chain.txt)

I started with replacing extension of .txt file into .json - as the format was already correct for json.

Then I created the readBlocks() function, to deserializer json file into a Blockchain object.

Another problem with the shell was the fact that each session creates a completely new blockchain.
Any mining overwrites the files in chain.json in your directory.
I changed it so now if you want to save you have to call the function manually.

22.01.2023
Following the CAP theorem, blockchain satisfies A+P.
Blockchain does not have SPOF - it makes it possible to achieve high availability.
As a P2P network it is also partition-tolerant.
"Finally completed blocks are broadcasted too (after integrity is secured)."
Consistency is not obvious - relies on P2P consensus achieved through cryptographic proofs (PoW, PoS, etc.)

About defining the users in the network:
"Users remain pseudonymous - linked through their cryptographic keys.
Pseudonym is H(PK), which can be used to transfer coins (through digital signature)"

23.01.2023
Next goal - execute the transactions.
PoW - only miner can execute the transactions to simplify the process.
In the real bitcoin blockchain, address of a user is hash of his private key.
I was thinking how I can simply encode it, my first idea was to use IP of the machine.
But it is not a good solution because of lots of reasons, so I decided to just pass as argument 
your id while mining so you will be assigned reward.

How to code other transaction than reward now?
PoW - you pass additional address while mining together with amount so it can get transfered in this block.
Problem: nothing stops you from using someone else's address as a payer XD
Possible solution: you hold your secret.

I updated the mining function so it now calculates hash of the passed argument (miner)
instead of saving it in the plain text.

I added transfer system:
1 transaction per block, miner has to execute transaction miner needs to pass private key (presumably his)
so its hash gets calculated, beneficiary hash and amount.
Problem: double spending

Planned development:
- Verifying transactions so there is no double spending
- Include multiple transactions per block - miner can get transactions, save them in file transaction.json,
then read them and include in the block
- Introduce fees per transactions: easy stuff
- Introduce merkel root hash calculation - one function which is later on added to the string, based on which block hash is calculated
- Adding real public/private keys, storing them in secret .yaml files or env_vars

Later on:
- Adding multiple recievers and multiple payers for one transaction

Questions to the prof:
1. Why in electrum testnet transactions I received have multiple outputs?
2. Why in blockchain transactions can have multiple inputs and multiple outputs?
3. Why "dotx" method is described as "do transaction?" Shouldn't it be called rather "create a block?" or "mine a block?"
There is no beneficiary, payer nor amount of transaction. Transaction is between sb and sb
4. Miner's machine uses its CPU to calculate puzzle hashes - why does it waste time and CPU to verify users' transactions sent to them,
when it can focus on calculating the puzzle? Block reward is much higher than fees + you do not receive fees if you don't manage to find the puzzle solution...

Add some simple unit tests.

Materials:
Ethereum testnet - so you can test your own solidity contract:
https://kovan.etherscan.io/
IDE for smart contracts and ethereum:
https://remix.ethereum.org/
