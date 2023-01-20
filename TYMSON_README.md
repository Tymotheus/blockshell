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



Questions to the prof:
1. Why in electrum testnet transactions I received have multiple outputs?
2. Why in blockchain transactions can have multiple inputs and multiple outputs?
3. Why "dotx" method is described as "do transaction?" Shouldnt it be called rather "create a block?" or "mine a block?"
There is no beneficiary, payer nor amount of transaction. Transaction is between sb and sb
4.

Add some simple unit tests.