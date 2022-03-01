def fizz_buzz(num):
    output = ""
    if num % 3 == 0:
        output = "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    return(output or num)


def fizz_buzz2(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num


def fizz_buzz3(num):
    output = "Fizz" if num % 3 == 0 else ""
    output += "Buzz" if num % 5 == 0 else ""
    if output == "":
        return num
    else:
        return output


def fizz_buzz_range(lower_limit, upper_limit):
    for i in range(lower_limit, upper_limit+1):
        output = "Fizz" if i % 3 == 0 else ""
        output += "Buzz" if i % 5 == 0 else ""
        print(i) if output == "" else print(f"{i} - {output}")


def run(N, M):
		sequence = ""

		for i in range(N, M+1):
			output = "Fizz" if i % 3 == 0 else ""
			output += "Buzz" if i % 5 == 0 else ""

			if output == "":
				sequence += str(i)
			else:
				sequence += output
			
			if i != M:
				sequence += ","
			
		return sequence

# print(fizz_buzz(1))
# print(fizz_buzz(3))
# print(fizz_buzz(5))
# print(fizz_buzz(15))
# fizz_buzz_range(1, 100)
print(run(1,15))
