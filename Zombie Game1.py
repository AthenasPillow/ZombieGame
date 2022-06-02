import random
import time
import sys
#Everthing works but the movement.
Hello = ' '
A = 1
B = 1
C = 1
D = 16
E = 1
F = 1
G = 1
H = 1
I = 1
J = 1
K = 1
L = 1
M = 1
N = 1
O = 1

def CreateramndomMap(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O):
    Mec = 1
    Mecha = 2
    Hos = 3
    Hospi = 4
    Sho = 5
    Shops = 6
    Wep = 7
    Weap = 8
    while A == B or A == C or A == D or A == E or A == F or A == G or A == H or A == I or A == J or A == K or A == L or A == M or A == N or A == O or B == C or B == D or B == E or B == F or B == G or B == H or B == I or B == J or B == K or B == L or B == M or B == N or B == O or C == D or C == E or C == F or C == G or C == H or C == I or C == J or C == K or C == L or C == M or C == N or C == O or D == E or D == F or D == G or D == H or D == I or D == J or D == K or D == L or D == M or D == N or D == O or E == F or E == G or E == H or E == I or E == J or E == K or L == M or E == N or E == O or F == H or F == I or F == G or F == J or F == K or F == L or F == M or F == N or F == O or G == H or G == I or G == J or G == K or G == L or G == M or G == N or G == O or H == I or H == J or H == K or H == L or H == M or H == N or H == O or I == J or I == K or I == L or I == M or I == N or I == O or J == K or J == L or J == M or J == N or J == O or K == L or K == M or K == N or K == O or L == M or L == N or L == O or M == N or M == O or N == O:
        A = random.randint(1, 14)
        B = random.randint(1, 14)
        C = random.randint(1, 14)
        E = random.randint(1, 14)
        F = random.randint(1, 14)
        G = random.randint(1, 14)
        H = random.randint(1, 14)
        I = random.randint(1, 14)
        J = random.randint(1, 14)
        K = random.randint(1, 14)
        L = random.randint(1, 14)
        M = random.randint(1, 14)
        N = random.randint(1, 14)
        O = random.randint(1, 14)
    a = A
    b = B
    c = C
    e = E
    f = F
    g = G
    h = H
    i = I
    j = J
    k = K
    l = L
    m = M
    n = N
    o = O
    if A == Mec or A == Hos or A == Sho or A == Wep or A == Mecha or A == Hospi or A == Shops or A == Weap:
        if A == Mec:
            A = '''
_______
|     |
| Mec |
|_____|'''
        elif A == Mecha:
            A = '''
_______
|     |
| Mec |
|_____|'''
        elif A == Hospi:
            A = '''
_______
|     |
| Hos |
|_____|'''            

        elif A == Shops:
            A = '''           
_______
|     |
| Sho |
|_____|''' 
        elif A == Weap:
            A = '''
_______
|     |
| Wep |
|_____|'''
        elif A == Hos:
            A = '''
_______
|     |
| Hos |
|_____|'''
        elif A == Sho:
            A = '''           
_______
|     |
| Sho |
|_____|'''
        elif A == Wep:          
            A = '''
_______
|     |
| Wep |
|_____|'''
    else:

        A = '''
_______
|     |
|     |
|_____|'''
    if B == Mec or B == Hos or B == Sho or B == Wep or B == Mecha or B == Hospi or B == Shops or B == Weap:
        if B == Mec:
            B = '''
_______
|     |
| Mec |
|_____|'''
        elif B == Mecha:
            B = '''
_______
|     |
| Mec |
|_____|'''
        elif B == Hospi:
            B = '''
_______
|     |
| Hos |
|_____|'''            

        elif B == Shops:
            B = '''           
______ 
|     |
| Sho |
|_____|''' 
        elif B == Weap:
            B = '''
_______
|     |
| Wep |
|_____|'''
        elif B == Hos:
            B = '''
_______
|     |
| Hos |
|_____|'''
        elif B == Sho:
            B = '''           
______ 
|     |
| Sho |
|_____|'''
        elif B == Wep:          
            B = '''
_______
|     |
| Wep |
|_____|'''
    else:

        B = '''
_______
|     |
|     |
|_____|'''
    if C == Mec or C == Hos or C == Sho or C == Wep or C == Mecha or C == Hospi or C == Shops or C == Weap:
        if C == Mec:
            C = '''
_______
|     |
| Mec |
|_____|'''
        elif C == Mecha:
            C = '''
_______
|     |
| Mec |
|_____|'''
        elif C == Hospi:
            C = '''
_______
|     |
| Hos |
|_____|'''            

        elif C == Shops:
            C = '''           
______ 
|     |
| Sho |
|_____|''' 
        elif C == Weap:
            C = '''
_______
|     |
| Wep |
|_____|'''
        elif C == Hos:
            C = '''
_______
|     |
| Hos |
|_____|'''
        elif C == Sho:
            C = '''           
______ 
|     |
| Sho |
|_____|'''
        elif C == Wep:          
            C = '''
_______
|     |
| Wep |
|_____|'''
    else:

        C = '''
_______
|     |
|     |
|_____|'''
    if E == Mec or E == Hos or E == Sho or E == Wep or E == Mecha or E == Hospi or E == Shops or E == Weap:
        if E == Mec:
            E = '''
_______
|     |
| Mec |
|_____|'''
        elif E == Mecha:
            E = '''
_______
|     |
| Mec |
|_____|'''
        elif E == Hospi:
            E = '''
_______
|     |
| Hos |
|_____|'''            

        elif E == Shops:
            E = '''           
______ 
|     |
| Sho |
|_____|''' 
        elif E == Weap:
            E = '''
_______
|     |
| Wep |
|_____|'''
        elif E == Hos:
            E = '''
_______
|     |
| Hos |
|_____|'''
        elif E == Sho:
            E = '''           
______ 
|     |
| Sho |
|_____|'''
        elif E == Wep:          
            E = '''
_______
|     |
| Wep |
|_____|'''
    else:

        E = '''
_______
|     |
|     |
|_____|'''
    if F == Mec or F == Hos or F == Sho or F == Wep or F == Mecha or F == Hospi or F == Shops or F == Weap:
        if F == Mec:
            F = '''
_______
|     |
| Mec |
|_____|'''
        elif F == Mecha:
            F = '''
_______
|     |
| Mec |
|_____|'''
        elif F == Hospi:
            F = '''
_______
|     |
| Hos |
|_____|'''            

        elif F == Shops:
            F = '''           
______ 
|     |
| Sho |
|_____|''' 
        elif F == Weap:
            F = '''
_______
|     |
| Wep |
|_____|'''
        elif F == Hos:
            F = '''
_______
|     |
| Hos |
|_____|'''
        elif F == Sho:
            F = '''           
______ 
|     |
| Sho |
|_____|'''
        elif F == Wep:          
            F = '''
_______
|     |
| Wep |
|_____|'''
    else:

        F = '''
_______
|     |
|     |
|_____|'''
    if G == Mec or G == Hos or G == Sho or G == Wep or G == Mecha or G == Hospi or G == Shops or G == Weap:
        if G == Mec:
            G = '''
_______
|     |
| Mec |
|_____|'''
        elif G == Mecha:
            G = '''
_______
|     |
| Mec |
|_____|'''
        elif G == Hospi:
            G = '''
_______
|     |
| Hos |
|_____|'''            

        elif G == Shops:
            G = '''           
______ 
|     |
| Sho |
|_____| ''' 
        elif G == Weap:
            G = '''
_______
|     |
| Wep |
|_____|'''          
        elif G == Hos:
            G = '''
_______
|     |
| Hos |
|_____|'''
        elif G == Sho:
            G = '''           
______ 
|     |
| Sho |
|_____|'''
        elif G == Wep:          
            G = '''
_______
|     |
| Wep |
|_____|'''
    else:

        G = '''
_______
|     |
|     |
|_____|'''
    if H == Mec or H == Hos or H == Sho or H == Wep or H == Mecha or H == Hospi or H == Shops or H == Weap:
        if H == Mec:
            H = '''
_______
|     |
| Mec |
|_____| '''
        elif H == Mecha:
            H = '''
_______
|     |
| Mec |
|_____| '''
        elif H == Hospi:
            H = '''
_______
|     |
| Hos |
|_____| '''            

        elif H == Shops:
            H = '''           
______ 
|     |
| Sho |
|_____| ''' 
        elif H == Weap:
            H = '''
_______
|     |
| Wep |
|_____|'''
        elif H == Hos:
            H = '''
_______
|     |
| Hos |
|_____| '''
        elif H == Sho:
            H = '''           
______ 
|     |
| Sho |
|_____| '''
        elif H == Wep:          
            H = '''
_______
|     |
| Wep |
|_____|'''
    else:

        H = '''
_______
|     |
|     |
|_____| '''
    if I == Mec or I == Hos or I == Sho or I == Wep or I == Mecha or I == Hospi or I == Shops or I == Weap:
        if I == Mec:
            I = '''
_______
|     |
| Mec |
|_____|'''
        elif I == Mecha:
            I = '''
_______
|     |
| Mec |
|_____|'''
        elif I == Hospi:
            I = '''
_______
|     |
| Hos |
|_____|'''            

        elif I == Shops:
            I = '''           
______ 
|     |
| Sho |
|_____|''' 
        elif I == Weap:
            I = '''
_______
|     |
| Wep |
|_____|'''
        elif I == Hos:
            I = '''
_______
|     |
| Hos |
|_____|'''
        elif I == Sho:
            I = '''           
______ 
|     |
| Sho |
|_____|'''
        elif I == Wep:          
            I = '''
_______
|     |
| Wep |
|_____|'''
    else:

        I = '''
_______
|     |
|     |
|_____|'''
    if J == Mec or J == Hos or J == Sho or J == Wep or J == Mecha or J == Hospi or J == Shops or J == Weap:
        if J == Mec:
            J = '''
_______
|     |
| Mec |
|_____|'''
        elif J == Mecha:
            J = '''
_______
|     |
| Mec |
|_____|'''
        elif J == Hospi:
            J = '''
_______
|     |
| Hos |
|_____|'''            

        elif J == Shops:
            J = '''           
______ 
|     |
| Sho |
|_____|''' 
        elif J == Weap:
            J = '''
_______
|     |
| Wep |
|_____|'''
        elif J == Hos:
            J = '''
_______
|     |
| Hos |
|_____|'''
        elif J == Sho:
            J = '''           
______ 
|     |
| Sho |
|_____|'''
        elif J == Wep:          
            J = '''
_______
|     |
| Wep |
|_____|'''
    else:

        J = '''
_______
|     |
|     |
|_____|'''
    if K == Mec or K == Hos or K == Sho or K == Wep or K == Mecha or K == Hospi or K == Shops or K == Weap:
        if K == Mec:
            K = '''
_______
|     |
| Mec |
|_____| '''
        elif K == Mecha:
            K = '''
_______
|     |
| Mec |
|_____| '''
        elif K == Hospi:
            K = '''
_______
|     |
| Hos |
|_____| '''            

        elif K == Shops:
            K = '''           
______
|     |
| Sho |
|_____| ''' 
        elif K == Weap:
            K = '''
_______
|     |
| Wep |
|_____|'''
        elif K == Hos:
            K = '''
_______
|     |
| Hos |
|_____| '''
        elif K == Sho:
            K = '''           
______
|     |
| Sho |
|_____| '''
        elif K == Wep:          
            K = '''
_______
|     |
| Wep |
|_____|'''
    else:

        K = '''
_______
|     |
|     |
|_____| '''
    if L == Mec or L == Hos or L == Sho or L == Wep or L == Mecha or L == Hospi or L == Shops or L == Weap:
        if L == Mec:
            L = '''
_______
|     |
| Mec |
|_____|'''
        elif L == Mecha:
            L = '''
_______
|     |
| Mec |
|_____|'''
        elif L == Hospi:
            L = '''
_______
|     |
| Hos |
|_____|'''            

        elif L == Shops:
            L = '''           
______ 
|     |
| Sho |
|_____|''' 
        elif L == Weap:
            L = '''
_______
|     |
| Wep |
|_____|'''
        elif L == Hos:
            L = '''
_______
|     |
| Hos |
|_____|'''
        elif L == Sho:
            L = '''           
______ 
|     |
| Sho |
|_____|'''
        elif L == Wep:          
            L = '''
_______
|     |
| Wep |
|_____|'''
    else:

        L = '''
_______
|     |
|     |
|_____|'''
    if M == Mec or M == Hos or M == Sho or M == Wep or M == Mecha or M == Hospi or M == Shops or M == Weap:
        if M == Mec:
            M = '''
_______
|     |
| Mec |
|_____|'''
        elif M == Mecha:
            M = '''
_______
|     |
| Mec |
|_____|'''
        elif M == Hospi:
            M = '''
_______
|     |
| Hos |
|_____|'''            

        elif M == Shops:
            M = '''           
______ 
|     |
| Sho |
|_____|''' 
        elif M == Weap:
            M = '''
_______
|     |
| Wep |
|_____|'''
        elif M == Hos:
            M = '''
_______
|     |
| Hos |
|_____|'''
        elif M == Sho:
            M = '''           
______ 
|     |
| Sho |
|_____|'''
        elif M == Wep:          
            M = '''
_______
|     |
| Wep |
|_____|'''
    else:

        M = '''
_______
|     |
|     |
|_____|'''
    if N == Mec or N == Hos or N == Sho or N == Wep or N == Mecha or N == Hospi or N == Shops or N == Weap:
        if N == Mec:
            N = '''
_______
|     |
| Mec |
|_____|'''
        elif N == Mecha:
            N = '''
_______
|     |
| Mec |
|_____|'''
        elif N == Hospi:
            N = '''
_______
|     |
| Hos |
|_____|'''            

        elif N == Shops:
            N = '''           
______ 
|     |
| Sho |
|_____|''' 
        elif N == Weap:
            N = '''
_______
|     |
| Wep |
|_____|'''
        elif N == Hos:
            N = '''
_______
|     |
| Hos |
|_____|'''
        elif N == Sho:
            N = '''           
______ 
|     |
| Sho |
|_____|'''
        elif N == Wep:          
            N = '''
_______
|     |
| Wep |
|_____|'''
    else:

        N = '''
_______
|     |
|     |
|_____|'''    
    if O == Mec or O == Hos or O == Sho or O == Wep or O == Mecha or O == Hospi or O == Shops or O == Weap:
        if O == Mec:
            O = '''
_______
|     |
| Mec |
|_____| '''
        elif O == Mecha:
            O = '''
_______
|     |
| Mec |
|_____| '''
        elif O == Hospi:
            O = '''
_______
|     |
| Hos |
|_____| '''            

        elif O == Shops:
            O = '''           
______
|     |
| Sho |
|_____| ''' 
        elif O == Weap:
            O = '''
_______
|     |
| Wep |
|_____|'''
        elif O == Hos:
            O = '''
_______
|     |
| Hos |
|_____| '''
        elif O == Sho:
            O = '''           
______
|     |
| Sho |
|_____|'''
        elif O == Wep:          
            O = '''
_______
|     |
| Wep |
|_____|'''
    else:

        O = '''
_______
|     |
|     |
|_____|'''
    S = '''
_______
|     |
SCHOOL|
|_____|'''
    P = '''
_______
|     |
|Exit!|
|_____|'''
    printblox(A, B, C, P)
    printblox(E, F, G, H)
    printblox(I, S, J, K)
    printblox(L, M, N, O)
    whereYouare(a,b,c,P, e,f,g,h, i,S,j,k, l,m,n,o, A,B,C, E,F,G,H, I,J,K, L,M,N,O)
def printblox(A, B, C, P):
    #Prints the blocks on a single line.
    a_list = A.split("\n")
    b_list = B.split("\n")
    c_list = C.split("\n")
    d_list = P.split('\n')
    print(a_list[0], b_list[0], c_list[0], d_list[0])
    print(a_list[1], b_list[1], c_list[1], d_list[1])
    print(a_list[2], b_list[2], c_list[2], d_list[2])
    print(a_list[3], b_list[3], c_list[3], d_list[3])
    print(a_list[4], b_list[4], c_list[4], d_list[4])
def whereYouare(a,b,c,P, e,f,g,h, i,S,j,k, l,m,n,o, A,B,C, E,F,G,H, I,J,K, L,M,N,O):
    s = S
    #Mec = 1
    #Mecha = 2
    #Hos = 3
    #Hospi = 4
    #Sho = 5
    #Shops = 6
    #Wep = 7
    #Weap = 8
    Location = P
    inventory = [ ]
    hi = ' '
    GameisNotwon = True
    while GameisNotwon == True:
        if Location == s:
            #For School
            print('You are standing in front of a red brick building named Carlton High School.')
            print('What direction do you want to go? (North, East, South, or West)')
            movement = hi
            while movement != 'north' or 'North' or 'west' or 'West' or 'South' or 'south' or 'East' or 'east':
                movement = input()
                movement = str(movement)
                if movement == ('North') or ('north'):
                    Location = f
                    break
                elif movement == ('West') or ('west'):
                    Location = i
                    break
                elif movement == ('South') or ('south'):
                    Location = m
                    break
                elif movement == ('East') or ('east'):
                    Location = j
                    break
            printblox(A,B,C,P)
            printblox(E,F,G,H)
            printblox(I,S,J,K)
            printblox(L,M,N,O)
        elif Location == a:
            if a == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif a == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif a == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif a == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (East or South)')
            movement = hi
            while movement != 'South' or 'south' or 'East' or 'east':
                movement = input()
                movement = str(movement)
                if movement == ('South') or ('south'):
                    Location = e
                    break
                elif movement == ('East') or ('east'):
                    Location = b
                    break
            printblox(A,B,C,P)
            printblox(E,F,G,H)
            printblox(I,S,J,K)
            printblox(L,M,N,O)
        elif Location == b:
            if b == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif b == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif b == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif b == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (East, West, or South)')
            movement = hi
            while movement != 'South' or 'south' or 'East' or 'east' or 'west' or 'West':
                movement = input()
                movement = str(movement)
                if movement == ('South') or ('south'):
                    Location = f
                    break
                elif movement == ('East') or ('east'):
                    Location = c
                    break
                elif movement == ('west') or ('West'):
                    Location = a
                    break
            printblox(A,B,C,P)
            printblox(E,F,G,H)
            printblox(I,S,J,K)
            printblox(L,M,N,O)
        elif Location == c:
            if c == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif c == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif c == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif c == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (East, West, or South)')
            movement = hi
            while movement != 'South' or 'south' or 'East' or 'east' or 'west' or 'West':
                movement = input()
                movement = str(movement)
                if movement == ('South') or ('south'):
                    Location = g
                    break
                elif movement == ('East') or ('east'):
                    Location = P
                    break
                elif movement == ('West') or ('west'):
                    Location = b
                    break
            printblox(A,B,C,P)
            printblox(E,F,G,H)
            printblox(I,S,J,K)
            printblox(L,M,N,O)
                  
        elif Location == e:
            if e == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif e == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif e == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif e == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (North, East, or South)')
            movement = hi
            while movement != 'South' or 'south' or 'east' or 'East' or 'North' or 'north':
                movement = input()
                movement = str(movement)
                if movement == ('South') or ('south'):
                    Location = i
                    break
                elif movement == ('East') or ('East'):
                    Location = f
                    break
                elif movement == ('North') or ('north'):
                    Location = a
                    break
            printblox(A,B,C,P)
            printblox(E,F,G,H)
            printblox(I,S,J,K)
            printblox(L,M,N,O)
                
                 
        elif Location == f:
            if f == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif f == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif f == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif f == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (North, East, West, or South)')
            movement = hi
            while movement != 'South' or 'south' or 'East' or 'east' or 'North' or 'north' or 'West' or 'west':
                movement = input()
                movement = str(movement)
                if movement == ('South') or ('south'):
                    Location = s
                    break
                elif movement == ('East') or ('east'):
                    Location = g
                    break
                elif movement == ('North') or ('north'):
                    Location = b
                    break
                elif movement == ('West') or ('west'):
                    Location = e
                    break
            printblox(A,B,C,P)
            printblox(E,F,G,H)
            printblox(I,S,J,K)
            printblox(L,M,N,O)
                     
                 
        elif Location == g:
            if g == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif g == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif g == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif g == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (North, East, West, or South)')
            movement = hi
            while movement != 'South' or 'south' or 'East' or 'east' or 'North' or 'north' or 'West' or 'west':
                movement = input()
                movement = str(movement)
                if movement == ('South') or ('south'):
                    Location = j
                    break
                elif movement == ('East') or ('east'):
                    Location = h
                    break
                elif movement == ('North') or ('north'):
                    Location = c
                    break
                elif movement == ('West') or ('west'):
                    Location = f
                    break
                     
            printblox(A,B,C,P)
            printblox(E,F,G,H)
            printblox(I,S,J,K)
            printblox(L,M,N,O)
        elif Location == a:
            if h == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif h == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif h == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif h == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (North, West, or South)')
            movement = hi
            while movement != 'South' or 'south' or 'North' or 'north' or 'west' or 'West':
                movement = input()
                movement = str(movement)
                if movement == ('South') or ('south'):
                    Location = k
                    break
                elif movement == ('north') or ('North'):
                    Location = P
                    break
                elif movement == ('West') or ('west'):
                    Location = g
                    break
                 
            printblox(A,B,C,P)
            printblox(E,F,G,H)
            printblox(I,S,J,K)
            printblox(L,M,N,O)
        elif Location == i:
            if i == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif i == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif i == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif i == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (North, East, or South)')
            movement = hi
            while movement != 'South' or 'south' or 'East' or 'east' or 'north' or 'North':
                movement = input()
                movement = str(movement)
                if movement == ('South') or ('south'):
                    Location = l
                    break
                elif movement == ('East') or ('east'):
                    Location = s
                    break
                elif movement == ('North') or ('north'):
                    Location = e
                    break
            printblox(A,B,C,P)
            printblox(E,F,G,H)
            printblox(I,S,J,K)
            printblox(L,M,N,O)
                
           
        elif Location == j:
            if j == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif j == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif j == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif j == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (North, East, South, or West)')
            movement = hi
            while movement != 'South' or 'south' or 'East' or 'east' or 'west' or 'West' or 'north' or 'North':
                movement = input()
                movement = str(movement)
                if movement == ('South') or ('south'):
                    Location = n
                    break
                elif movement == ('East') or ('east'):
                    Location = k
                    break
                elif movement == ('west') or ('West'):
                    Location = s
                    break
                elif movement == ('north') or ('North'):
                    Location = g
                    break
            printblox(A,B,C,P)
            printblox(E,F,G,H)
            printblox(I,S,J,K)
            printblox(L,M,N,O)
                
           
        elif Location == k:
            if k == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif k == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif k == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif k == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (West, North, or South)')
            movement = hi
            while movement != 'South' or 'south' or 'West' or 'west' or 'North' or 'north':
                movement = input()
                movement = str(movement)
                if movement == ('South') or ('south'):
                    Location = o
                    break
                elif movement == ('West') or ('west'):
                    Location = j
                    break
                elif movement == ('North') or ('north'):
                    Location = h
                    break
            printblox(A,B,C,P)
            printblox(E,F,G,H)
            printblox(I,S,J,K)
            printblox(L,M,N,O)
                
        elif Location == l:
            if l == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif l == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif l == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif l == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (East or North)')
            movement = hi
            while movement != 'North' or 'north' or 'East' or 'east':
                movement = input()
                movement = str(movement)
                if movement == ('North') or ('north'):
                    Location = i
                    break
                elif movement == ('East') or ('east'):
                    Location = m
                    break
                printblox(A,B,C,P)
                printblox(E,F,G,H)
                printblox(I,S,J,K)
                printblox(L,M,N,O)
                
            
        elif Location == m:
                if m == 1 or 2:
                    print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                    print('You go inside, and grab a tool.')
                    inventory.append('Tool')
                elif m == 3 or 4:
                    print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                    print('You run inside, and nab a medkit.')
                    inventory.append('Medkit')
                elif m == 5 or 6:
                    print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                    print('You hustle inside, and steal some food.')
                    inventory.append('Food')
                elif m == 7 or 8:
                    print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                    print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                    inventory.append('Sword')
                else:
                    print('You are standing on an empty street, with cars laying on their sides, abandoned.')
                print('What direction do you want to go? (West, East, or North)')
                movement = hi
                while movement != 'North' or 'north' or 'East' or 'east' or 'west' or 'west':
                    movement = input()
                    movement = str(movement)
                    if movement == ('North') or ('north'):
                        Location = s
                        break
                    elif movement == ('East') or ('east'):
                        Location = l
                        break
                    elif movement == ('West') or ('west'):
                        Location = n
                        break
                printblox(A,B,C,P)
                printblox(E,F,G,H)
                printblox(I,S,J,K)
                printblox(L,M,N,O)
                    
                   
           
        elif Location == n:
            if n == 1 or 2:
                print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                print('You go inside, and grab a tool.')
                inventory.append('Tool')
            elif n == 3 or 4:
                print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                print('You run inside, and nab a medkit.')
                inventory.append('Medkit')
            elif n == 5 or 6:
                print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                print('You hustle inside, and steal some food.')
                inventory.append('Food')
            elif n == 7 or 8:
                print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                inventory.append('Sword')
            else:
                print('You are standing on an empty street, with cars laying on their sides, abandoned.')
            print('What direction do you want to go? (West, East, or North)')
            movement = hi
            while movement != 'North' or 'north' or 'East' or 'east' or 'west' or 'West':
                movement = input()
                movement = str(movement)
                if movement == ('North') or ('north'):
                    Location = j
                    break
                elif movement == ('East') or ('east'):
                    Location = o
                    break
                elif movement == ('West') or ('west'):
                    Location = m
                    break
                printblox(A,B,C,P)
                printblox(E,F,G,H)
                printblox(I,S,J,K)
                printblox(L,M,N,O)
            
        elif Location == o:
                if o == 1 or 2:
                    print('You once visited this place to check your car\'s tires and it is O-Riely Atuoparts. You stand outside it wondering if you could use anything from in there for your car.')
                    print('You go inside, and grab a tool.')
                    inventory.append('Tool')
                elif o == 3 or 4:
                    print('You are standing outside a white building with a red cross, a Hospital, preparing to go inside and loot it for med kits.')
                    print('You run inside, and nab a medkit.')
                    inventory.append('Medkit')
                elif o == 5 or 6:
                    print('You are standing outside the shop In-and-out, preparing to run inside and run out with your hands full of whatever you can find.')
                    print('You hustle inside, and steal some food.')
                    inventory.append('Food')
                elif o == 7 or 8:
                    print('You are standing in front of what seems to be a pile of guns, knifes, and other weapons that seems to stretch on forever.')
                    print('You find a sword amoungst the plie, and test it on a zombie nearby then store it for safe keeping.')
                    inventory.append('Sword')
                else:
                    print('You are standing on an empty street, with cars laying on their sides, abandoned.')
                print('What direction do you want to go? (West or North)')
                movement = hi
                while movement != 'North' or 'north' or 'West' or 'west':
                    movement = input()
                    movement = str(movement)
                    if movement == ('North') or ('north'):
                        Location = k
                        break
                    elif movement == ('West') or ('west'):
                        Location = n
                        break

                printblox(A,B,C,P)
                printblox(E,F,G,H)
                printblox(I,S,J,K)
                printblox(L,M,N,O)
                    
                
        elif Location == P:
                print('You are standing before the exit of this town, debating whether you will survive with the materials you have, and without one needed material you will lose.')
                print('Where do you wish to move? (South, West, or bye is you wish to escape.)')
                movement = hi
                while movement != 'south' or 'South' or 'west' or 'West' or 'bye' or 'Bye':
                    movement = input()
                    movement = str(movement)
                    if movement == ('South') or ('south'):
                        Location = e
                        break
                    elif movement == ('bye') or ('Bye'):
                        if len(inventory) >= 7:
                            print('CONGRATULATIONS! You win!')
                            print('This is what you had:')
                            print(inventory)
                            GameisNotwon = False
                            break
                        
                        else:
                            print('Your car crashed on the side of the road and the zombies came and ate your brain.')
                            GameisNotwon = False
                            break
                    elif movement == ('west') or ('West'):
                        Location = c
                        break
                    print(inventory)
                printblox(A,B,C,P)
                printblox(E,F,G,H)
                printblox(I,S,J,K)
                printblox(L,M,N,O)
def startup(Hello):
    print('You are surviving in the zombie apoclypse, your town has been overrun and you must escape to the nearest apocolypse shelter.')
    time.sleep(3)
    print()
    print('You are driving to the shelter in your mom\'s old van.')
    time.sleep(5)
    print()
    print('The van just broke down outside of a school (a safe place) and you must gather supplies to fix it, fight the zombies, and escape.')
    time.sleep(3)
    print()
    print('Very fortunately, you are in a town that you know your way around, so you can get everything with ease, but you have to not get bitten.')

    
def showInstructions():
    print('''Rules:
If you try to escape without required items, you lose.
To escape get ALL required items, reach the exit, and type in Bye!
When fighting a zombie you will be prompted to fight, flee, or make a distraction.
You will know the map.
4 items are obtainable from each place( 1 being a weapon. )
You can only take one item from each place, but you will be prompted with 2.
You can only carry 2 weapons at a time, and weapons will break after 1 zombie fight.
Zombies have a 1 in 4 chance to drop a needed item.
You will find zombies randomly, and the map changes everytime you play.
Sho stands for Shop, wep stands for Weapon Stash, hos stand for Hospital, and mec stands for Mechanic.
The required items are 2 mechanic items, 2 hospital items, 2 shop items, and 1 weapon.
''')
print('Would you like to view the rules? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()
    time.sleep(20)
startup(Hello)
time.sleep(1)
print('Here is the map')
CreateramndomMap(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O)
