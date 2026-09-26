import time

frases = [
    "Bankai!",
    "Getsuga Tensho!",
    "Zangetsu...",
    "Bleach!",
]

for frase in frases:
    for character in frase:
        print(character, end="", flush=True)
        time.sleep(0.08)
    print()
    time.sleep(1)