import tkinter as tk  # Import tkinter for GUI
from calculator_functions import calculate_expression, clear_entry, perform_function  # Import necessary functions

class ScientificCalculator:
    def __init__(self, root):
        self.root = root  # Initialize main window
        self.root.title("Scientific Calculator")  # Set title
        self.root.geometry("450x700")  # Set window size
        self.root.configure(bg="#2C3E50")  # Set background color
        
        self.create_entry()  # Create entry field
        self.create_buttons()  # Create calculator buttons
        
    def create_entry(self):
        # Create input field where users enter expressions
        self.entry = tk.Entry(self.root, font=("Arial", 20), bd=10, relief=tk.FLAT, justify='right', bg="#ECF0F1", fg="#2C3E50", state="normal")
        self.entry.grid(row=0, column=0, columnspan=5, ipadx=10, ipady=15, pady=10)  # Position input field
    
    def create_buttons(self):
        # List of buttons with text, row, and column position
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('(', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), (')', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('^2', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('sqrt', 4, 4),
            ('C', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('tan', 5, 3), ('%', 5, 4),
            ('asin', 6, 0), ('acos', 6, 1), ('atan', 6, 2), ('log', 6, 3), ('ln', 6, 4)
        ]
        
        for (text, row, col) in buttons:
            self.create_button(text, row, col)  # Create button for each value
    
    def create_button(self, text, row, col):
        # Create buttons with specific styling and place them in the grid
        tk.Button(self.root, text=text, font=("Arial", 16, "bold"), width=6, height=3, 
                  bg="#34495E", fg="white", relief=tk.RAISED, bd=4,
                  command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)
    
    def on_button_click(self, char):
        # Handle button click events
        if char == '=':
            calculate_expression(self.entry)  # Evaluate expression when '=' is clicked
        elif char == 'C':
            clear_entry(self.entry)  # Clear entry when 'C' is clicked
        elif char in ('sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log', 'ln', 'sqrt', '^2'):
            perform_function(self.entry, char)  # Perform function for trigonometry, log, etc.
        else:
            self.entry.insert(tk.END, char)  # Insert clicked button text into entry field

if __name__ == "__main__":
    root = tk.Tk()  # Initialize tkinter window
    calc = ScientificCalculator(root)  # Create calculator instance
    root.mainloop()  # Run the application
