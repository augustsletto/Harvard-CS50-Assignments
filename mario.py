hashtag = "#"
twogap = "  "
onegap = " "

game_done = False

while not game_done:
    try:
        height = int(input("Height: "))
    except ValueError:
        continue
    else:
        if height in range(1, 9):
            h = height - 1
            for i in range(height):
                i += 1

                print(f"{onegap*h}{hashtag*i}{twogap}{hashtag*i}")
                h -= 1
            game_done = True
