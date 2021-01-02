from Cryptodome.Util import number

# p = number.getPrime(512)
# q = number.getPrime(512)
p = 61
q = 53
e = 65537  # usually a large prime number, or calculated using gcd(e,phi(pq))=1

n = p * q


def calculate_phi():
    return (p - 1) * (q - 1)


def generate_private_key():
    phi = calculate_phi()
    # print("phi: ", phi)
    return pow(e, -1, phi)


def crypt(plaintext):
    return (plaintext ** e) % n


def decrypt(cripttext):  # using TCR (faster than normal decryption)
    d = generate_private_key()

    # print("d: ", d)

    def TCR(a, n):
        m1 = p
        m2 = q
        n1 = n % (m1 - 1)
        n2 = n % (m2 - 1)
        m1_mod_inverse = pow(m1, -1, m2)

        x1 = ((a % m1) ** n1) % m1
        x2 = ((a % m2) ** n2) % m2
        return x1 + m1 * (((x2 - x1) * m1_mod_inverse) % m2)

    return TCR(cripttext, d)


# def decrypt(cripttext):
#     return (cripttext ** generate_private_key()) % n


text = 123
ct = crypt(text)
print(ct)
dt = decrypt(ct)
print(dt)
