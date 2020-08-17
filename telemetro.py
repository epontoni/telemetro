import math

def distancia(alpha, beta):
    alpha_rad = math.radians(alpha)
    beta_rad = math.radians(beta)

    d = math.sin(alpha_rad)*math.sin(beta_rad)/math.sin(math.pi - (alpha_rad + beta_rad))

    return d

a = float(input("Ingrese ángulo alpha: "))
b = float(input("Ingrese ángulo beta: "))

print(f"La distancia al objeto es: {distancia(a,b)}")



