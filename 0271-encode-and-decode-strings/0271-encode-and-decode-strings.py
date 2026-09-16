class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for text in strs:
            encoded.append(text.replace(" ", "�"))
        return "ϴ".join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        strings = s.split("ϴ")
        res = []
        for text in strings:
            decoded = text.replace("�", " ")
            res.append(decoded)
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
