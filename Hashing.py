 # Hashing: 
    # it's a method of sorting and indexing data. the idea behind hashing is to allow large amount of data to be indexed using keys commonly created by formulas. 
    # check visualization\Hashing\hashing.png
 # why:
    # used due to it's time efficient in case of search operations.

# Hash Terminology: check visualization\Hashing\hash terminology.png / collision.png 
# Hash Functions: check visualization\Hashing\char and num hash functions.png
   # Properties of good hash functions:
      # 1. It distributes hash values uniformly across hash table.
      # 2. It has to use all input values.
# Collision Resolution Techniques:
   # 1. Direct Chaining: Implements the buckets as linked list. Colliding elements are stored in this lists. check visualization\Hashing\direct chaining.png
   # 2. Open Addressing: Colliding elements are stored other vacant buckets. During storage and lookup these are found through so called "Probing".
      # - Linear Probing: It places new key into the closest empty cell. check visualization\Hashing\linear probing.png
      # - Quadratic Probing: Adding arbitrary  quadratic polynomial to the index until an empty cell is found. check visualization\Hashing\quadratic probing.png
      # - Double Hashing: Interval between probes is computed by another hash functions. check visualization\Hashing\double hashing.png