from Database import enc_table

# p = number.getPrime(512)
# q = number.getPrime(512)
# p = 59
# q = 53
# e = 65537  # usually a large prime number, or calculated using gcd(e,phi(pq))=1
# n=p*q


def retrieve_from_db():
    doc_pass = enc_table.find_one({'_id': 1})
    p = doc_pass["p"]
    q = doc_pass["q"]
    e = doc_pass["e"]
    n = p * q
    return p, q, n, e


p, q, n, e = retrieve_from_db()


def calculate_phi():
    return (p - 1) * (q - 1)


def generate_private_key():
    phi = calculate_phi()
    # print("phi: ", phi)
    return pow(e, -1, phi)


def crypt(plaintext):

    plaintext = plaintext.decode("iso-8859-1")
    # print(plaintext)
    ch_list = [ord(b) for b in plaintext]
    # print(ch_list)
    enc_list = [(ch ** e) % n for ch in ch_list]
    print(enc_list)
    # print(enc_list)
    return enc_list


def decrypt(cripttext_list):  # using TCR (faster than normal decryption)
    d = generate_private_key()

    def TCR(a, n):
        m1 = p
        m2 = q
        n1 = n % (m1 - 1)
        n2 = n % (m2 - 1)
        m1_mod_inverse = pow(m1, -1, m2)

        x1 = ((a % m1) ** n1) % m1
        x2 = ((a % m2) ** n2) % m2
        return x1 + m1 * (((x2 - x1) * m1_mod_inverse) % m2)
    txt_list = [chr(TCR(cripttext_list[i], d)) for i in range(len(cripttext_list))]

    plaintext = ""
    for ch in txt_list:
        plaintext = plaintext + ch
    return plaintext.encode("iso-8859-1")


# def decrypt(cripttext):
#     return (cripttext ** generate_private_key()) % n
