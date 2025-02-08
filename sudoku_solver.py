import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_x, box_y = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_x + i][box_y + j] == num:
                return False
    return True

def is_valid_input(board):
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                board[row][col] = 0
                if not is_valid(board, row, col, num):
                    return False
                board[row][col] = num
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def solve_button():
    global grid
    board = [[grid[row][col].get() for col in range(9)] for row in range(9)]
    try:
        board = [[int(board[row][col]) if board[row][col] else 0 for col in range(9)] for row in range(9)]
        if not is_valid_input(board):
            messagebox.showwarning("Invalid Input", "The given Sudoku input is incorrect!")
            return
        if solve_sudoku(board):
            for row in range(9):
                for col in range(9):
                    grid[row][col].delete(0, tk.END)
                    grid[row][col].insert(0, str(board[row][col]))
                    grid[row][col].config(fg='blue')  # Set solved numbers to blue
        else:
            messagebox.showerror("Error", "No solution exists!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Only numbers 1-9 are allowed.")

def create_gui():
    global grid
    root = tk.Tk()
    root.title("Sudoku Solver")
    grid = [[tk.Entry(root, width=3, font=('Arial', 18), justify='center', bd=2, relief='ridge', fg='red') for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            entry = grid[row][col]
            entry.grid(row=row, column=col, padx=2, pady=2)
            if (row // 3 + col // 3) % 2 == 0:
                entry.config(bg='#D3D3D3')
            if row % 3 == 2:
                entry.grid(pady=(2, 6))
            if col % 3 == 2:
                entry.grid(padx=(2, 6))
    solve_btn = tk.Button(root, text="Solve", command=solve_button, font=('Arial', 14))
    solve_btn.grid(row=9, column=0, columnspan=9, pady=10)
    root.mainloop()

if __name__ == "__main__":
    create_gui()
