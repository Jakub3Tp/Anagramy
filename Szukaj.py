anagram_a = input("Podaj wyraz: ")
anagram_b = input("Podaj jej anagram: ")

def czy_anagram():
    sortowana_anagram_a = sorted(anagram_a)
    sortowana_anagram_b = sorted(anagram_b)
    if sortowana_anagram_a == sortowana_anagram_b:
        print("Anagramy")
    else:
        print("Nie jest Anagramem")

czy_anagram();
