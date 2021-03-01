import sort_counter


def ascending_selection_sort_weights(helicopters):
    for current_position in range(len(helicopters)):
        min_value = current_position
        for fill_position in range(current_position+1, len(helicopters)):

            if helicopters[fill_position].max_lifting_weight < helicopters[min_value].max_lifting_weight:
                min_value = fill_position
            sort_counter.selection_comparisons_counter += 1
        if min_value != current_position:
            helicopters[current_position], helicopters[min_value] = helicopters[min_value], helicopters[current_position]
            sort_counter.selection_swap_counter += 1
    return helicopters