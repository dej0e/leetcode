class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def is_valid(num):
            if num == "0":
                return True
            elif num[0] == "0":
                return False
            elif int(num) > 255:
                return False
            else:
                return True

        def get_edges(start_index):
            segments = []
            for i in range(start_index, start_index + 3):
                if i < len(s):
                    segments.append(s[start_index: i + 1])
            return segments

        def to_ip_address(path):
            address = path[0]
            for i in range(1, 4):
                address += "." + path[i]
            return address

        def dfs(start_index, path):
            if len(path) > 4:
                return
            if start_index == len(s):
                if len(path) == 4:
                    ans.append(to_ip_address(path))
                return

            for edge in get_edges(start_index):
                if is_valid(edge):
                    path.append(edge)
                    dfs(start_index + len(edge), path)
                    path.pop()

        dfs(0, [])
        return ans
