import random

def generate_secret_code():
    renkler = ['R', 'G', 'B', 'Y', 'C', 'M']
    code = []
    while len(code) < 4:
        color = random.choice(renkler)
        if code.count(color) < 2:
            code.append(color)
    return code

def evaluate_guess(secret_code, guess):
    siyah_pegs = sum(s == g for s, g in zip(secret_code, guess))
    beyaz_pegs = 0
    for color in set(secret_code):
        beyaz_pegs += min(secret_code.count(color), guess.count(color))
    beyaz_pegs -= siyah_pegs
    return siyah_pegs, beyaz_pegs

def main():
    secret_code = generate_secret_code()
    max_attempts = 13
    attempts = 12

    while attempts >= 0:
        remaining_attempts = attempts + 1
        guess = input(f"{remaining_attempts}. Tahmininizi 4 renk olarak girin (R G B Y C M): ").upper().split()

        if len(guess) != 4 or not all(color in ['R', 'G', 'B', 'Y', 'C', 'M'] for color in guess):
            print("Geçersiz giriş yaptınız, renkler kümesinden lütfen 4 renk giriş yapın ve aynı renkten max 2 defa girin (R G B Y C M)")
            continue

        attempts -= 1
        siyah_pegs, beyaz_pegs = evaluate_guess(secret_code, guess)

        if siyah_pegs == 4:
            print(f"Tebrikler, gizli kodu {remaining_attempts - 1} denemede çözdünüz.")
            break
        else:
            print(f"Sonuç: {siyah_pegs} siyah, {beyaz_pegs} beyaz. Kalan hakkınız: {attempts + 1}")

        if attempts < 0:
            print(f"Tahmin hakkınız doldu. Gizli kod: {' '.join(secret_code)}")

if __name__ == '__main__':
    main()