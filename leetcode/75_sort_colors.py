def sort_colors(colors):
    red, white, blue = 0, 0, len(colors)-1
    while white <= blue:
        if colors[white] == 0:
            colors[red], colors[white] = colors[white], colors[red]
            red += 1
            white += 1
        elif colors[white] == 1:
            white += 1
        else:
            colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1


if __name__ == '__main__':
    colors = [0, 1, 0, 2, 0, 2, 1, 1, 0]
    sort_colors(colors)
    print(colors)
