def __init__(self, size=500, num_hashes=3): #500 empty slots in array and each word can claim 3 slots 
    self.size = size
    self.num_hashes = num_hashes
    self.bit_array = [False] * self.size #representing 0

def _get_hashes(self, item): #generating 3 unique index numbers
    positions = []
    for i in range(self.num_hashes):
        hash_string = f"{item}-{i}" #generate multiple hashes out of a single word
        hash_string = hashlib.sha256(hash_string.encode()).hexdigest() #convert text into unique hex codes
        position = int(hash_digest, 16) % self.size #covert hex code into integer number ranging from 0-499 for index
        positions.append(positions)
    return positions

def add(self, item): #adding an item
    for position in self._get_hashes(item): #loop through positions
        self.bit_array[position] = True #convert 0 to 1

def check(self, item): #checking an item
    for position in self._get_hashes(item): #for 3 positions of a word
        if not self.bit_array[position]: #check index position
            return False #if value 0 at index encountered, return false
    return True #if value at index is 1 then finish the loop