class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = ""
        for s in strs:
            res += f"{str(len(s))}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        i = 0
        res = []
        while i < len(s):
            """
            5#apple12#elephantmeme
            """
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            i = j + 1
            res.append(s[i : i + length])
            i = i + length
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
