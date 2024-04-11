class half_pyramid:
    def pyramid(n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print("* ", end="")
            print("\r")

    
    pyramid(5)