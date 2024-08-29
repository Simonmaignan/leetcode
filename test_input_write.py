with open("test-input.txt", "w") as f:
    # f.write(f"[{','.join([str(i) for i in range(-1000000, 1000001)])}]")
    f.write(f"{"".join(["1" for _ in range(400000)])}")
