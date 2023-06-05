import math
import cmath 
import numpy as np
from cmath import exp, pi

######################################################################################################################
def key_scheduling(K):
    j=1
    s=7
    k_i=""
    for k in range(len(K)): #permuted combinated 1- it removes all the characters at 0,7,15,23..... so that the resulatant keylength is 56
        if k!=s:
            k_i=k_i+K[k]
        else:
            s=s+8
    print("The 56 bit key that is being used: ",k_i,end='\n')
    k_s=[]  #stores the keys for each round

    ######################################################################################################################
    for i in range(16):
        k_i_l=k_i[0:28] #splitting the key into two halves left and right
        k_i_r=k_i[28:56] #splitting the key into two halves left and right

        if i==1 or i==2 or i==9 or i==16: #in rounds 1,2,9,16 shifting is done by 1 to the left on the key
            k_i_ls=k_i_l[1:28]+k_i_l[0]
            k_i_rs=k_i_r[1:28]+k_i_r[0]
            k_i=k_i_ls+k_i_rs
        else:       #in other rounds shifing is done by 2 to the left 
            k_i_ls=k_i_l[2:28]+k_i_l[0:2]
            k_i_rs=k_i_r[2:28]+k_i_r[0:2]
            k_i=k_i_ls+k_i_rs
        s=6 
        k_si=""  #initialise the 48 bit round key
        for k in range(len(k_i)): #permuated combination-2, here we remove the 7th bits,i.e,6,13,20... to get the 48 bit final round key
            if k!=s:
                k_si=k_si+k_i[k]
            else:
                s=s+7
        k_s.append(k_si)
        print("This is the round key: ",k_si," for round ",i, end='\n')

    ######################################################################################################################
    return k_s

######################################################################################################################
def DES(A,k):

    ######################################################################################################################
    A=intitial_permuation(A) # the initial permuation applied to the plaintext
    ######################################################################################################################
    A_l=A[0:32]
    A_r=A[32:64]
    for i in range(16): #fiestal network
        A_rf=f(A_r,k[i]) #passing it to the 'f' function
        A_rff=int(A_rf,2)^int(A_l,2) 
        A_l=A_r
        A_r='{:032b}'.format(A_rff)
        A=A_l+A_r
        print("The ciphertext is : ",A," after round ",i,end="\n")
    ######################################################################################################################
    A=final_permutation(A) #inverse of the initial permutation
    ######################################################################################################################
    return A    

######################################################################################################################
def f(A,k):
    ######################################################################################################################
    A=Expansion(A) #converts 32 bit plaintext to 48 bits
    ######################################################################################################################
    c=int(A,2)
    d=int(k,2)
    a=c^d
    A_b='{:048b}'.format(a) #resultant of the XOR btw key and expanded plaintext
    print(A_b) #stores the output of the 'f' function
    C_f=""
    ######################################################################################################################
    for j in range(8):
        C=A_b[j*6:(j+1)*6] #taking 6 bit blocks. Therefore there are 48/6=8 blocks
        row=C[0]+C[5]
        column=C[1:5]
        r=int(row,2) # the first and the last bit give the row of the S_box
        c=int(column,2) # the middle 4 bits give the column of the S_box
        C=S_box(r,c) # S_box takes 6 bit input and gives 4 bit output
        C_f=C_f+C 
    ######################################################################################################################
    C_f=Permutation(C_f) # applying a final permutation
    ######################################################################################################################
    return C_f

######################################################################################################################
def Permutation(C): # the permutation of the S_box in the 'f' function
    C_r=C[15]+C[6]+C[19]+C[20]+C[28]+C[11]+C[27]+C[16]+C[0]+C[14]+C[22]+C[25]+C[4]+C[17]+C[30]+C[9]+C[1]+C[7]+C[23]+C[13]+C[31]+C[26]+C[2]+C[8]+C[18]+C[12]+C[29]+C[5]+C[21]+C[10]+C[3]+C[24]
    return C_r

######################################################################################################################
def Expansion(A): # converts 32 bit input to 48 bit
    a=A[28:32]
    b=A[0:4]
    A=a+A+b
    A_i=""
    for j in range(8): #8 blocks
        A_i=A_i+A[((j+1)*4-1):((j+2)*4+1)] #takes the last bit of the previous block and the first bit of the next block in addition to the current block,therefore 6 bits in each block
    return A_i

######################################################################################################################
def S_box(row,column): 
    S=[[0 for j in range(16)] for i in range(4)]
    S[0][0]=14
    S[0][1]=4
    S[0][2]=13
    S[0][3]=1
    S[0][4]=2
    S[0][5]=15
    S[0][6]=11
    S[0][7]=8
    S[0][8]=3
    S[0][9]=10
    S[0][10]=6
    S[0][11]=12
    S[0][12]=5
    S[0][13]=9
    S[0][14]=0
    S[0][15]=7
    S[1][0]=0
    S[1][1]=15
    S[1][2]=7
    S[1][3]=4
    S[1][4]=14
    S[1][5]=2
    S[1][6]=13
    S[1][7]=1
    S[1][8]=10
    S[1][9]=6
    S[1][10]=12
    S[1][11]=11
    S[1][12]=9
    S[1][13]=5
    S[1][14]=3
    S[1][15]=8
    S[2][0]=4
    S[2][1]=1
    S[2][2]=14
    S[2][3]=8
    S[2][4]=13
    S[2][5]=6
    S[2][6]=2
    S[2][7]=11
    S[2][8]=15
    S[2][9]=12
    S[2][10]=9
    S[2][11]=7
    S[2][12]=3
    S[2][13]=10
    S[2][14]=5
    S[2][15]=0
    S[3][0]=15
    S[3][1]=12
    S[3][2]=8
    S[3][3]=2
    S[3][4]=4
    S[3][5]=9
    S[3][6]=1
    S[3][7]=7
    S[3][8]=5
    S[3][9]=11
    S[3][10]=3
    S[3][11]=14
    S[3][12]=10
    S[3][13]=0
    S[3][14]=6
    S[3][15]=13

    res='{:04b}'.format(S[row][column])
    return res

######################################################################################################################
def intitial_permuation(A):
    A_c=A[57]+A[49]+A[41]+A[33]+A[25]+A[17]+A[9]+A[1]+A[59]+A[51]+A[43]+A[35]+A[27]+A[19]+A[11]+A[3]+A[61]+A[53]+A[45]+A[37]+A[29]+A[21]+A[13]+A[5]+A[63]+A[55]+A[47]+A[39]+A[31]+A[23]+A[15]+A[7]+A[56]+A[48]+A[40]+A[32]+A[24]+A[16]+A[8]+A[0]+A[58]+A[50]+A[42]+A[34]+A[26]+A[18]+A[10]+A[2]+A[60]+A[52]+A[44]+A[36]+A[28]+A[20]+A[12]+A[4]+A[62]+A[54]+A[46]+A[38]+A[30]+A[22]+A[14]+A[6]
    return A_c

########################################################################################################################
def final_permutation(A):
    A_c=A[39]+A[7]+A[47]+A[15]+A[55]+A[23]+A[63]+A[31]+A[38]+A[6]+A[46]+A[14]+A[54]+A[22]+A[62]+A[30]+A[37]+A[5]+A[45]+A[13]+A[53]+A[21]+A[61]+A[29]+A[36]+A[4]+A[44]+A[12]+A[52]+A[20]+A[60]+A[28]+A[35]+A[3]+A[43]+A[11]+A[51]+A[19]+A[59]+A[27]+A[34]+A[2]+A[42]+A[10]+A[50]+A[18]+A[58]+A[26]+A[33]+A[1]+A[41]+A[9]+A[49]+A[17]+A[57]+A[25]+A[32]+A[0]+A[40]+A[8]+A[48]+A[16]+A[56]+A[24]
    return A_c

######################################################################################################################
if __name__=='__main__':
    a=input("Enter the Plaintext to be encrypted: ")
    K=input("Enter the Key(64 bits= 8 characters): ")


    K=''.join(format(ord(i), '08b') for i in K) #Converting the key to binary
    a=''.join(format(ord(i), '08b') for i in a) #Converting PT to binary
    b=len(a)  #length of PT
    ######################################################################################################################
    while b%64!=0 : #padding with 0
        b=b+1
        a=a+'0' 
    ######################################################################################################################
    print("The padded Plaintext is: ",a) #printing the padded PT

    ######################################################################################################################
    k=key_scheduling(K) #Scheduling the keys
    ######################################################################################################################
    c=int(b/64) #number of blocks

    ######################################################################################################################
    for j in range (c):
        A=a[j*64:(j+1)*64] #getting each block as DES is a block cipher
        print("The resultant ciphertext in binary is: ",DES(A,k)," for block ",j,end='\n') #performing DES on each block separately
    ######################################################################################################################

##############################################################################################################
    
