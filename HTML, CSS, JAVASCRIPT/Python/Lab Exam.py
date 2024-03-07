'''
Lab_exam -- Nguyen Hung Anh -- 10/18/2023
A program to computer a weighted average for a final grade
'''
#This is a function definition; only done once.
def weighted_average(exam_weight, exam_score, labs_weight, labs_score):
    final_score = exam_weight * exam_score + labs_weight * labs_score
    return final_score

def main():
    print("Weighted Average Calculator")
    exam_category_weight = 0.75
    labs_category_weight = 0.25
    
    my_exam_score = 90.1
    my_labs_score = 10
    # This is a function call; can be done many times
    my_final_score = weighted_average(
                        exam_category_weight,
                        my_exam_score,
                        labs_category_weight,
                        my_labs_score)
    print(f"Final score:{my_final_score:.>5.1f}")
    
if __name__ == "__main__":
    main()

def weighted_average(exam_weight, exam_score, labs_weight, lab_score):
    final_score = exam_weight * exam_score + labs_weight * lab_score
    return final_score

def main():
    exam_category_weight = 0.75
    labs_category_weight = 0.25

    my_exam_score = 90.1
    my_labs_score = 10

    my_final_score = weighted_average(exam_category_weight, my_exam_score, labs_category_weight, my_labs_score)
    print(f"Final score:{my_final_score:.>5.1f}")

if __name__ == "__main__":
    main()

