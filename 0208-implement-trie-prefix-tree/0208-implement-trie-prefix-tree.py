"""
1. First used a simple list, if in list and .startswith() method to solve, but while reading comments section, I realised Trie is a completely diff data structure.
2. after watching a youtube vedio, I learnt it is a graph with a root node, and each word is created a children to it, similar word like car and card would be on same graph c->a->r and d would extend over r, with end = true or false at each node to represent if the node is yet to end or completed.
3. created a new class to create a tirenode with children and end.
4. insert would check if the char of node is in children, if nore create new and node, assign it to children, and move the current node the children node, until end of the char in word. at end mark end as true to signify the word is end at current node.
5. for search, serach if char is in children of current node, if not return false if true keep searching, if loop ends, return true if end is true else false ex:- dog and we search do would return false
6. same exact logic as search instead of checking if end is true or false, it will return true if the loop end.

time comp:- 
    1. insert:- O(l), l being no of char in word
    2. search :- O(l)
    3. startswith:- O(l), l being no of words to search
Space comp:- O(n*l), no of words * avg len of its char's
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        
        return True
        
        

"""
class Trie:

    def __init__(self):
        self.ans = []
        

    def insert(self, word: str) -> None:
        self.ans.append(word)
        

    def search(self, word: str) -> bool:
        if word in self.ans:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        for word in self.ans:
            if word.startswith(prefix):
                return True
        return False
        
"""

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)