 # Hashing: 
    # it's a method of sorting and indexing data. the idea behind hashing is to allow large amount of data to be indexed using keys commonly created by formulas. 
    # check visualization\Hashing\hashing.png
 # why:
    # used due to it's time efficient in case of search operations.

# Hash Terminology: check visualization\Hashing\hash terminology.png / collision.png 
# Hash Functions: check visualization\Hashing\char and num hash functions.png / time complexity.png
   # Properties of good hash functions:
      # 1. It distributes hash values uniformly across hash table.
      # 2. It has to use all input values.
def mod(number, cellNumber): # for integers.
    return number % cellNumber
def modASCII(string, cellNumber): # for chars.
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber

# Collision Resolution Techniques:
   # 1. Direct Chaining: Implements the buckets as linked list. Colliding elements are stored in this lists. check visualization\Hashing\direct chaining.png

   # 2. Open Addressing: Colliding elements are stored other vacant buckets. During storage and lookup these are found through so called "Probing".
      # - Linear Probing: It places new key into the closest empty cell. check visualization\Hashing\linear probing.png
      # - Quadratic Probing: Adding arbitrary  quadratic polynomial to the index until an empty cell is found. check visualization\Hashing\quadratic probing.png
      # - Double Hashing: Interval between probes is computed by another hash functions. check visualization\Hashing\double hashing.png

   # Pros and Cons of these techniques:
      # Direct Chaining:
         # 1. Hash table is never full.
         # 2. Huge linked lists causes performance leaks (time complexity of search operations is O(N)).
      # Open Addressing:
         # 1. Easy implementation.
         # 2. When table is full, creation of new hash table affects performance (time complexity of search operations is O(N)).

   # which one to use:
      # if the input size is known, we always use "Open Addressing".
      # if we perform deletion operation frequently we use "Direct Chaining".

   # P.S. Python uses "Open Addressing" (by using something called Random Probing) to handle collisions.
   # to avoid slowing down lookups, the dict will be resized when it is two-thirds full.

# if the hash table is full, we should create 2x (double) size of current hash table and recall the hashing for current keys (recompute every key hash).