import sys
input = sys.stdin.readline

word = input().strip()

print(int(word[::-1] == word))