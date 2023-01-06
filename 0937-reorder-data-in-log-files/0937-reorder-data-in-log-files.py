class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        lett = []
        digi = []
        for log in logs:
            if log.split()[1].isalpha():
                lett.append(log)
            else:
                digi.append(log)

        lett.sort(key=lambda x : (x.split()[1:], x.split()[0]))

        return lett + digi