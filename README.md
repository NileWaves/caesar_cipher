# Caesar Cipher
![caesar_cipher](https://user-images.githubusercontent.com/102873173/192584659-225a9b09-f593-4cac-a315-917da3f3d8c5.jpg)
\
\
Caesar cipher is a primitive encryption tool used by Julius Caesar to protect his military correspondence. 
By shifting the alphabet by a predetermined number of positions, a message becomes scrambled.
\
\
Suppose Caesar wants to send his Legatus the following message: "attackatdawn".
And he and his Legatus agreed on shifting down the alphabet by 3 letters.
He would write the message as such: "dwwdfndwgdzq". 
The Legatus can simply shift up by 3 letters to reveal the original message: "attackatdawn".
This method was often enough to fool his unwitting enemies. 
\
\
If one suspects that a message is encoded with a Caesar cipher, cracking it is a no brainer -- there isn't even the need for Frequency Analysis. Since each letter 
in the encoded text is derived by shifting a FIXED number of positions, the cracker can simply attempt to shift the alphabet one letter at a time, and on his or her worst day, the cracker will succeed at the 25th attempt. 
\
\
Thus, the Caesar cipher is said to be the simplest form of substitution cipher. In using a standard form of substitution cipher, the cryptographer replaces each letter of the plaintext with a different letter in the ciphertext. This requires a full table of letter replacements. For example, (a->g, b->e, c->z, d->j...). Both the sender and receiver of the message need to have a copy of this table to encrypt and decrypt messages. To crack messages encoded with this method, Frequency Analysis is used. 

