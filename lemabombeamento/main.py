def pertence_linguagem(w: str) -> bool:
    """
    Verifica se a palavra w pertence à linguagem L = { aⁿbⁿ | n ≥ 0 }.
    """
    n = len(w)
    a_count = 0

    for c in w:
        if c == 'a':
            a_count += 1
        else:
            break

    return w == 'a' * a_count + 'b' * a_count


def aplicar_lema_bombeamento(w: str, p: int):
    """
    Aplica o lema do bombeamento à palavra w com comprimento de bombeamento p.
    """
    print(f"\nPalavra w: '{w}'")
    print(f"Comprimento mínimo de bombeamento p: {p}\n")

    encontrou_quebra = False

    for i in range(1, p + 1):  # x termina em i
        x = w[:i]
        for j in range(1, p - i + 1):  # y tem ao menos 1 caractere
            y = w[i:i + j]
            z = w[i + j:]

            print(f"Divisão: x = '{x}', y = '{y}', z = '{z}'")

            for k in [0, 1, 2]:  # bombeia y^k
                nova = x + y * k + z
                resultado = pertence_linguagem(nova)
                status = "PERTENCE" if resultado else "NÃO pertence"
                print(f"  i = {k} → '{nova}' → {status}")

                if not resultado:
                    encontrou_quebra = True
                    print("  ⚠️  Quebra detectada nessa divisão!\n")

            print("-" * 50)

    if encontrou_quebra:
        print("\n✅ Conclusão: A linguagem NÃO é regular (houve quebra do lema).")
    else:
        print("\n❌ Conclusão: Não houve quebra. O lema não foi violado.")


if __name__ == "__main__":
    print("💡 Linguagem utilizada: L = { aⁿbⁿ | n ≥ 0 }\n")

    # Entrada do usuário
    w = input("Digite uma cadeia (ex: aabb): ").strip()
    
    while True:
        try:
            p = int(input("Digite o valor de p (comprimento mínimo de bombeamento): "))
            if p <= 0:
                print("p deve ser maior que 0.")
                continue
            break
        except ValueError:
            print("Digite um número inteiro válido para p.")

    aplicar_lema_bombeamento(w, p)
