def countdown_head(n):
    if n < 0:
        return
    print(n)
    countdown_head(n - 1)


countdown_head(20)