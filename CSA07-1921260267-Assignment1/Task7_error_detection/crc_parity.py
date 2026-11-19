def mod2_div(dividend, divisor):
    rem = list(dividend)
    for i in range(len(dividend) - len(divisor) + 1):
        if rem[i] == "1":
            for j in range(len(divisor)):
                rem[i+j] = str(int(rem[i+j]) ^ int(divisor[j]))
    return "".join(rem[-(len(divisor)-1):])

if __name__ == "__main__":
    data = "1101011011"
    gen = "1011"
    padded = data + "000"
    
    rem = mod2_div(padded, gen)
    frame = data + rem
    print(f"Data: {data}, Gen: {gen}")
    print(f"Remainder: {rem}")
    print(f"Transmitted: {frame}")
    
    # Test no error
    print(f"No error check: {mod2_div(frame, gen) == '000'}")