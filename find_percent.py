from decimal import Decimal

if __name__ == '__main__':
    n = int(raw_input())
    
    student_marks = {}
    
    
    
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    
        query_name = raw_input()
        
# Extract the values into a list: query_scores
    query_scores = student_marks[query_name]

    # Sum the scores in the list: total_scores
    total_scores = sum(query_scores)

    # Convert the floats to decimals and average the scores: avg
    avg = Decimal(total_scores/3)

    # Print the mean of the scores, correct to two decimals
    print(round(avg,2))

        
