import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 구두점 제거 및 소문자 변환
        words = [word for word in re.sub(r'[\W]',' ', paragraph).lower().split() if word not in banned]
        
        # 단어 빈도수 계산
        counts = collections.Counter(words)
    
        # 가장 많이 등장한 단어 반환
        return counts.most_common(1)[0][0]