# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
t = int(input())

scores = []
ans = []
for i in range(t):
    # 전체 학생 수, 등수, 성적 비율, 수행 개수, 과락 점수 기준
    l, s, n, k, m, *vs = map(int, input().split())

    ans.append((s / l * 100 < n) and all([j > m for j in vs]))

print(int(all(ans)))
