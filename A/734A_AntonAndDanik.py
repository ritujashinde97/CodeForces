n = input()
games = input().upper()

if games.count('A')>games.count('D'):
    print('Anton')
elif games.count('D')>games.count('A'):
    print('Danik')
elif games.count('D')==games.count('A'):
    print('Friendship')
