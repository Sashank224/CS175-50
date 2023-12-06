#cs175
#Sashank Vaddiparty
#ExpensePie




# Import the matplotlib.pyplot module for plotting graphs
import matplotlib.pyplot as plt

# Define the main function of the program
def main():
    try:
        # Initialize two empty lists: labels for category names, and sizes for expense amounts
        labels = []
        sizes = []

        # Open the file with expenses data in read mode
        with open(r'C:\Users\Sasha\Downloads\expenses.txt', 'r') as file:
            # Iterate through each line in the file
            for line in file:
                try:
                    # Split each line at the tab character into label and value
                    label, value = line.split('\t')
                    # Append the label to the labels list
                    labels.append(label)
                    # Convert the value to integer and append it to the sizes list
                    sizes.append(int(value))
                # Handle ValueError which occurs if the value part is not a number
                except ValueError:
                    # Print an error message showing the problematic line
                    print(f"Error converting data: {line.strip()}")

        # Create a pie chart with the sizes as values, labels as categories, and display percentages
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        # Ensure that the pie chart is circular by setting an equal aspect ratio
        plt.axis('equal')
        # Display the pie chart
        plt.show()

    # Handle IOError which occurs if there is an issue opening the file
    except IOError:
        # Print an error message if the file cannot be opened
        print("Error opening file")

# Check if the script is being run directly (not imported as a module in another script)
if __name__ == "__main__":
    main()
    # If the script is
