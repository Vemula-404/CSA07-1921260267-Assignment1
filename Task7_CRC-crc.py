def mod2_div(dividend, divisor):
    rem = list(dividend)
    for i in range(len(dividend) - len(divisor) + 1):
        if rem[i] == "1":
            for j in range(len(divisor)):
                rem[i + j] = str(int(rem[i + j]) ^ int(divisor[j]))
    return "".join(rem[-(len(divisor) - 1):])

def crc_encode(data, gen):
    return data + mod2_div(data + "0" * (len(gen) - 1), gen)

def check(frame, gen):
    return set(mod2_div(frame, gen)) == {"0"}

if __name__ == "__main__":
    gen, data = "1011", "1101011011"
    tx = crc_encode(data, gen)
    print("CRC bits:   ", tx[-3:])
    print("Transmitted:", tx)
    print("No error accepted:", check(tx, gen))
    one = list(tx); one[3] = "1" if one[3] == "0" else "0"
    print("1-bit error accepted:", check("".join(one), gen))
    burst = list(tx)
    for k in (2, 3, 4):
        burst[k] = "1" if burst[k] == "0" else "0"
    print("3-bit burst accepted:", check("".join(burst), gen))
    print("Task 7.2 frame 11010110111011 accepted:", check("11010110111011", gen))