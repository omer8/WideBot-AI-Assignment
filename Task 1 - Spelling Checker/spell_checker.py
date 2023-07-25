
#read dictionary file
with open('/content/dictionary.txt', "rb") as f:
    dicts = f.readlines()
dicts = [w.decode('ISO-8859-1').strip() for w in dicts]

# Structure of a Trie node
class TrieNode:
	def __init__(self):

		# Store address of a character
		self.trie = [None] * 256
		# Check if the character is last character of a string or not
		self.isEnd = False

# Function to insert a string into Trie
def insert_trie(root, s):
	temp = root
	# Traverse the string, s
	for i in range(len(s)):
		if not temp.trie[ord(s[i])]:
			# Initialize a node
			temp.trie[ord(s[i])] = TrieNode()
		# Update temp
		temp = temp.trie[ord(s[i])]
	# Mark the last character of the string to true
	temp.isEnd = True

# Function to print suggestions of the string
def print_suggestions(root, res):
	# If current character is the last character of a string
	if root.isEnd:
		print(res,end=" ")

	# Iterate over all possible characters of the string
	for i in range(256):
		# If current character present in the Trie
		if root.trie[i]:
			# Insert current character into Trie
			res_list = list(res)
			res_list.append(chr(i))
			print_suggestions(root.trie[i], "".join(res_list))

# Function to check if the string is present in Trie or not
def check_present(root, key):
	# Traverse the string
	for i in range(len(key)):
		# If current character not present in the Trie

		if not root.trie[ord(key[i])]:
			print_suggestions(root, key[:i])
			return False
		# Update root
		root = root.trie[ord(key[i])]
	if root.isEnd:
		return True
	print_suggestions(root, key)
	return False

# Function to insert a new word into dict
def insert_dict(newword):
	import bisect
	#check if word exist in dicts
	if newword not in dicts:
		#add word in appropriate place in dicts from left
		dicts[bisect.bisect_left(dicts,newword)] = newword

#1 Store this dictionary in a suitable data structure.
## Time Complexity: O(N * M), where M is the maximum length of the string
## space complexity: O(N * 256)

import timeit
start = timeit.default_timer()

## Initialize a Trie
root = TrieNode()
## Insert words to trie
for s in dicts:
	insert_trie(root, s)

print("The time taken is ",timeit.default_timer() - start)

#2 Take an input word and return the nearest 4 words if this word is not in the dictionary
## Time Complexity: O(L) where L is length of word
## space complexity: O(1)

inp = input().lower()
start = timeit.default_timer()
##return the nearest words
if check_present(root, inp):
	print(inp)

print("\nThe time taken is {}".format(timeit.default_timer() - start))

#3 Take an input word and add this word to the dictionary
## Time Complexity:  O(L) where L is length of word
## space complexity: O(L) where L is length of word

inp = input().lower()
start = timeit.default_timer()
##insert word
insert_dict(inp)
print(dicts)

print("The time taken is {}".format(timeit.default_timer() - start))
