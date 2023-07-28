def last_ten_digits_of_series(limit):
    # Calculate the sum of the series
    total_sum = sum(i**i for i in range(1, limit + 1))
    
    # Convert the sum to a string to extract the last ten digits
    total_sum_str = str(total_sum)
    
    # Extract the last ten digits and convert them back to an integer
    last_ten_digits = int(total_sum_str[-10:])
    
    return last_ten_digits

if __name__ == "__main__":
    limit = 10
    last_ten_digits = last_ten_digits_of_series(limit)
    
    print(f"The last ten digits of the series are: {last_ten_digits}")

