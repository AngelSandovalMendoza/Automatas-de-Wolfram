import numpy as np
import matplotlib.pyplot as plt

gen_length = 64
generations = []

def setup():
    rule_number = obtener_numero_regla()
    initial_random = input("¿Deseas generar un automata inicial aleatorio? (s/n): ")

    if initial_random.lower() == 's':
        generation1 = generar_configuracion_aleatoria()
    else:
        generation1 = [0] * gen_length
        generation1[gen_length // 2] = 1

    generations.append(generation1)

    for _ in range(32):
        next_generation(rule_number)

    show_final_automata(rule_number)

def apply_rule(left, center, right, rule):
    rule_binary = format(rule, '08b')[::-1]
    rule = [int(bit) for bit in rule_binary]
    index = 4 * left + 2 * center + right
    return rule[index]

def next_generation(rule):
    last_gen = generations[-1]
    next_gen = []

    for i in range(len(last_gen)):
        left = last_gen[i - 1] if i - 1 >= 0 else last_gen[-1]
        center = last_gen[i]
        right = last_gen[(i + 1) % len(last_gen)] if i + 1 < len(last_gen) else last_gen[0]

        next_gen.append(apply_rule(left, center, right, rule))

    generations.append(next_gen)

def show_final_automata(rule):
    plt.imshow(generations, cmap='binary', interpolation='none')
    plt.title(f'Automata Celular - Regla {rule}')
    plt.show()

def obtener_numero_regla():
    try:
        rule_number = int(input("Ingresa el número de regla de Wolfram: "))
        if 0 <= rule_number <= 255:
            return rule_number
        else:
            print("Por favor, ingresa un número entre 0 y 255.")
            return obtener_numero_regla()
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return obtener_numero_regla()

def generar_configuracion_aleatoria():
    return np.random.choice([0, 1], size=gen_length)

if __name__ == "__main__":
    setup()
