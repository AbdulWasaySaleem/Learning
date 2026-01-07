# Encoding and Decoding Strings
# Given an array of strings, return their encoding and decoding
# Example: Input: ["Hello","World"], Output: ["5#Hello5#World"]
# Formula = NumberOfWords(Identifier as #,@,&,*)ActualWord

def encode(strs):
    encoded = ""
    for s in strs:
        encoded += str(len(s)) + "#" + s
    return encoded

def decode(s):
    result = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1

        length = int(s[i:j])
        word = s[j + 1 : j + 1 + length]
        result.append(word)

        i = j + 1 + length

    return result

strs = ["Hello","World"]

encoded = encode(strs)
print("encoded string: ",encoded)

decoded = decode(encoded)
print("decoded string: ",decoded)
