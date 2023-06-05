# DES
Date Encryption Standard

It is based on **FIESTAL NETWORKS**
# Fiestal Network:
![image](https://github.com/7h4nd5RG0d/DES/assets/128285431/d483f4aa-3209-4bdd-8153-5f9e4e8c3020)

>- The initial plaintext is divided into 2 halves left and right.  
>- The right half becomes the left half for the next round.  
>- The right half is passed through an 'f' function along with the round key and the output is XOR'd with the left half. This gives the right half for the next round.  

# Key Scheduling:
![image](https://github.com/7h4nd5RG0d/DES/assets/128285431/d9fb9378-8267-43bd-8855-fbb601f1b65f)
>- The initial key size is 64 bits.  
>- This 64-bit key is passed through PC-1(Permuted combination-1) which removes the last bit of each 8-bit block( Since there are 64 bits ---> there are 8 blocks of 8 bits therefore 8 bits are removed and the resultant is 56 bits long.  
>- This 56-bit initial key is passed through a recursive function 16 times to get the 16 round keys.  
>- In each recursion the 56-bit key is split into 2 halves left(L) and right(R), and then both the halves are shifted according to the round number(In rounds 1,2,9,16 the shift is by one bit to the left and for each of the other round the shift is 2 bits to the left), this shifted key is passed through PC-2 which removes the last bit of each 7-bit block.  
>- Finally we get the 48-bit round keys of each round.  
>**NOTE: PC-1 and PC-2 are basically compression functions as they are removing 8 bits from the input.** 

# Steps involved in each round:
>-  Split the plaintext of each round into halves L and R.
>- The right half R is the left half for the next round
>- The right half is then passed through the **'f' function** along with the round key and then XOR'd with the left half. The final output is the right half for the next round.

# The 'f' function:
![image](https://github.com/7h4nd5RG0d/DES/assets/128285431/78772c36-097b-4d1f-9e22-02eec13b6493)
>- The right half is passed through an expansion box.
>- The output is XOR'd with the round key
>- The 48-bit output is then split into 8 blocks of 6 bits each and each block is passed through an S-box.
>- The S-box takes a 6-bit input and gives a 4-bit output. The first and last bit of each block gives the row number and the middle 4 bits give the column number in the S-box.
>- The 32-bit output from the S-box is passed through a permutation box and finally we get the 32-bit resultant string.
>- NOTE: The S-box is a compression function as it takes a 6-bit input and gives a 4-bit output

# The Expansion box:
>- The input to the expansion box is 32-bit in length.
>- It is split into 8 blocks of 4 bits each.
>- To each block we add the last bit of the previous block to the start and the first bit of the next block to the end to make it a total of 6 buts in each block
>- The total length will be 48 bits.

# Steps involved in DES:
>- Take the plaintext and divide it into 64-bit blocks. If the last block does not have 64 bits use a padding scheme to convert it into 64 bits.
>- **NOTE: DES is a BLOCK CIPHER**
>- Pass the plaintext into an initial permutation.
>- This output is passed through 16 rounds of the fiestal network
>- The output is then passed through an inverse permutation to get the final ciphertext of the block


# Python code:
>- 1)The padding scheme:- If the last block is not 64  bits 0's are appended to make it 64-bit
>- 2)The s-boxes used in a round are the same. In practice the 8 S-boxes are different 
>- 3)PC-1:- Takes 64-bit input and gives 56-bit output by removing the last bit of each 8 bit-block
>- 4)PC-2:- Takes 56-bit input and gives 48-bit output by removing the last bit of each 7-bit block.


# Output:
![image](https://github.com/7h4nd5RG0d/DES/assets/128285431/40f123cd-937b-4c17-b8e0-26a9e775a7c9)

### References for images:
> 1)https://www.researchgate.net/figure/Illustration-of-a-round-in-a-Feistel-network_fig1_224645711
> 2)https://www.researchgate.net/figure/Function-f-of-DES-5_fig2_309634531
