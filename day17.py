n = 3
keywords = ["Hello", "Journal", "Secret"]
shift_value = 3

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypted_keywords = []

for st in keywords:
    result = ""
    for i in range(len(st)):
        if not st[i].isalpha():
            result += st[i]
        else:
            found = False
            for j in range(len(lowercase)):
                if lowercase[j] == st[i]:
                    val = j + shift_value
                    if val >= 26:
                        val -= 26
                    result += lowercase[val]
                    found = True
                    break
            if not found:
                for j in range(len(uppercase)):
                    if uppercase[j] == st[i]:
                        val = j + shift_value
                        if val >= 26:
                            val -= 26
                        result += uppercase[val]
                        break
    encrypted_keywords.append(result)

print(encrypted_keywords)
