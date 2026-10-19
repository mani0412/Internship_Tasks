# The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem
k = int(input())
rooms = list(map(int, input().split()))

room_set = set(rooms)

print((sum(room_set) * k - sum(rooms)) // (k - 1))
