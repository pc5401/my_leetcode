class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:  # 빈 문자열일 경우 빈 문자열을 반환
            return ''
        # 집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))