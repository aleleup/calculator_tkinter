def display_operation(display_array, display_text, total_sum):
    
    i = 0
    for item in display_array:
        print(type(item))
        if type(item) != str:
            display_array[i] = str(item)
        i += 1

    if total_sum:
        display_text.set(f"{' '.join(display_array)} {total_sum}")
    else:
        display_text.set(f"{' '.join(display_array)}")