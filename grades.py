def calculate_average(grades_list):
    if not grades_list:
        return 0.0
    
    total = sum(grades_list)
    average = total / len(grades_list)
    return average
