# 01. 「パタトクカシーー」

word = "パタトクカシーー"
print(word[1::2])

for i in range(len(word)):
    if not i % 2:
        print(word[i], end='')

print()

print('a', 'b', sep=',')

print("".join([s for i, s in enumerate(word) if not i % 2]))


print(filter(lambda s:s%2==1, word) )