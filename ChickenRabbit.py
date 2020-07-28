# class puzzle:
def solve(heads, legs):
    error_msg = "No Solution"
    for r in range(heads + 1):
        c = heads - r
        if r * 4 + c * 2 == legs:
            return "chicken " + str(c) + ", rabbit " + str(r)
    return error_msg

    # if "__name__" == "__Main__":


solution = solve(35, 95)
print(solution)
