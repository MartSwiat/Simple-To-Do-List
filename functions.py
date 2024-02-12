def read_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print(f"{3*'*'}Numbers only please{3*'*'}")
