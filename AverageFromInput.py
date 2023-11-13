# CS175
# Sashank Vaddiparty
# AverageFromInput

def main():  # This is where our main code will reside
    # This line sets up the path to the file you want to read from
    path_to_file = "C:/Users/Sasha/Downloads/numbers (1).txt"

    try:  # A try block lets you test a block of code for errors. It means "try this code".

        # Open the file for reading
        file = open(path_to_file, "r")  # This line tries to open the file at the path specified by path_to_file in read mode ("r").

        # Here, we're initializing two variables: total to store the sum of numbers and count to keep track of how many numbers we've read.
        total = 0
        count = 0
        
        # Read each line from the file
        for line in file:  # This line starts a for loop that will iterate over each line in the file.
            try:
                number = float(line)  # Here, we convert the current line (which is a string) into a floating-point number.
            except ValueError:
                print(f"Could not convert '{line.strip()}' to a float.")
                continue  # Skip to the next iteration of the loop

            count += 1  # This increments our count by 1 for each number we read.
            total += number  # This line adds the current number to our running total.

            print(f"I read in {count} number(s) Current number is: {number:.2f} Total is: {total:.2f}")  # Output format using an f-string, which allows us to embed expressions inside string literals.
        
        # After loop finishes, we calculate the average of the numbers.
        average = total / count
        print(f"Average: {average:.1f}")
        
        file.close()  # Close the file

    except Exception as e:  # If any errors occur inside the try block, the code inside this except block will run. It will capture any kind of exception and store it in the variable e.
        print("An error occurred:", e)

# Call the main function
if __name__ == "__main__":
    main()
