import sys
print("Mensaje para","error", file=sys.stderr, flush=True)
print("Salida desde archivo", file=sys.stdout, flush=True)
print()
print("Mensaje para","error", file=sys.stderr, flush=False)
print("Salida desde archivo", file=sys.stdout, flush=False)

print("**************")
print("*            *")
print("*            *")
print("**************")

t = "palabra"
n = 23
print("Una palabra:",t," y un número",n)
print(f"Misma palabra: {t}. Mismo número: {n}")