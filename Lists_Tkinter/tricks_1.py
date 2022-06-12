with open("random_text.txt", "r") as the_text:
    lines = the_text.readline()
    new_lines = []
    for item in lines:
        if item == ".":
            new_lines.append("!")
        else:
            new_lines.append(item)
    final_text = "".join([str(item) for item in new_lines])
    print(final_text)

    final_text_map = map(lambda x: x, new_lines)
    final_text_map_list = (list(final_text_map))
    print("".join([str(item) for item in final_text_map_list]))