import collections
# 56 ) 트라이 구현
# 트라이의 insert,search,startsWith 메소드를 구현하라.

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    # 처음 Trie 클래스를 생성하게 되면 root 노드로 별도 선언한 TrieNode 클래스를 갖게 된다.
    def __init__(self):
        self.root = TrieNode()

    # 삽입
    # 루트부터 자식 노드가 점점 깊어지면서 문자 단위의 다진 트리 형태가 된다.
    # 각각의 노드는 word 값을 갖게 되며 마지막 단어의 word(= 단어가 모두 완성되었을때)만 True가 된다.
    def insert(self, word : str ) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word : str ) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix : str ) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]
        return True


if __name__ == "__main__":

    trie = Trie()

    trie.insert("apple")
    trie.search("apple") # true
    trie.search("app") # false
    trie.startsWith("app") # true
    trie.insert("app")
    trie.search("app")  # true