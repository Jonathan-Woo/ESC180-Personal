def reverse_str(s):
    reversed_str = ""
    #invariant: reversed_str is the reversed version of s[:i] for iteration i

    for ch in s:
        reversed_str = ch + reversed_str

    #invariant: a condition that holds at every iteration of the loop

    return reversed_str

def is_anagram(text_1,text_2):
    text_1 = text_1.replace(" ","")
    text_2 = text_2.replace(" ","")

    for ch in text_1 + text_2:
        if text_1.count(ch) != text_2.count(ch):
            return False
    return True

def is_anagram_2(text_1,text_2):
    return (sorted(text_1.replace(" ",""))) == (sorted(text_2.replace(" ","")))

    #a router needs to receive N data packets (represent them as strings), and needs to transmit one of the N packets, uniformly at random (i.e. each packet should have an equal probably of being transmitted



if __name__ == "__main__":
    print(is_anagram_2("face","faced"))