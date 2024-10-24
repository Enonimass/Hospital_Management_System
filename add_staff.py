import tkinter as tk
from tkinter import messagebox, ttk
import Home


class Staff:
    def __init__(self, staff_number, first_name, last_name, practicing_id, address, phone, registration_date, professional):
        self.staff_number = staff_number
        self.first_name = first_name
        self.last_name = last_name
        self.practicing_id = practicing_id
        self.address = address
        self.phone = phone
        self.registration_date = registration_date
        self.professional = professional


class StaffPage:
    def __init__(self, root, switch_to_home):
        self.root = root
        self.switch_to_home = switch_to_home
        self.root.title("St. Mark Hospital - Staff Page")
        self.root.geometry("600x400")
        self.staff = []
        self.staff_count = 0  # Initialize staff count

        # Set the background color of the entire window
        self.root.configure(bg="#2c3e50")  # Darker blue background

        # Navbar
        self.navbar = tk.Frame(self.root, bg="skyblue")
        self.navbar.pack(side=tk.TOP, fill=tk.X)

        # Home Button
        self.home_button = tk.Button(self.navbar, text="Home", command=self.switch_to_home, bg="skyblue", fg="black")
        self.home_button.pack(side=tk.LEFT, padx=10)

        # Title Label (Centered)
        self.label_title = tk.Label(self.navbar, text="St. Mark Hospital", bg="skyblue", fg="black", font=("Arial", 24))
        self.label_title.pack(side=tk.TOP, padx=10, pady=5)

        # Content Frame with Light Blue Background
        self.content_frame = tk.Frame(self.root, bg="#b2e0f0")  # Light blue background for content
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Staff Entry Form
        self.entry_frame = tk.Frame(self.content_frame, bg="#b2e0f0")  # Light blue background
        self.entry_frame.pack(pady=10)

        self.label_first_name = tk.Label(self.entry_frame, text="First Name:")
        self.label_first_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_first_name = tk.Entry(self.entry_frame)
        self.entry_first_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_last_name = tk.Label(self.entry_frame, text="Last Name:")
        self.label_last_name.grid(row=1, column=0, padx=5, pady=5)
        self.entry_last_name = tk.Entry(self.entry_frame)
        self.entry_last_name.grid(row=1, column=1, padx=5, pady=5)

        self.label_practicing_id = tk.Label(self.entry_frame, text="Practicing ID:")
        self.label_practicing_id.grid(row=2, column=0, padx=5, pady=5)
        self.entry_practicing_id = tk.Entry(self.entry_frame)
        self.entry_practicing_id.grid(row=2, column=1, padx=5, pady=5)

        self.label_address = tk.Label(self.entry_frame, text="Address:")
        self.label_address.grid(row=3, column=0, padx=5, pady=5)
        self.entry_address = tk.Entry(self.entry_frame)
        self.entry_address.grid(row=3, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(self.entry_frame, text="Phone Number:")
        self.label_phone.grid(row=4, column=0, padx=5, pady=5)
        self.entry_phone = tk.Entry(self.entry_frame)
        self.entry_phone.grid(row=4, column=1, padx=5, pady=5)

        self.label_registration_date = tk.Label(self.entry_frame, text="Registration Date:")
        self.label_registration_date.grid(row=5, column=0, padx=5, pady=5)
        self.entry_registration_date = tk.Entry(self.entry_frame)
        self.entry_registration_date.grid(row=5, column=1, padx=5, pady=5)

        self.label_professional = tk.Label(self.entry_frame, text="Professional:")
        self.label_professional.grid(row=6, column=0, padx=5, pady=5)
        self.entry_professional = tk.Entry(self.entry_frame)
        self.entry_professional.grid(row=6, column=1, padx=5, pady=5)

        # Add Staff Button
        self.add_staff_button = tk.Button(self.content_frame, text="Add Staff", command=self.add_staff,
                                           bg="#e74c3c", fg="white")
        self.add_staff_button.pack(pady=10)

        # Delete Staff Button
        self.delete_staff_button = tk.Button(self.content_frame, text="Delete Staff", command=self.delete_staff,
                                              bg="#e74c3c", fg="white")
        self.delete_staff_button.pack(pady=10)

        # Table to Display Staff
        self.table = ttk.Treeview(self.content_frame, columns=(
            "Staff Number", "First Name", "Last Name", "Practicing ID",
            "Address", "Phone", "Registration Date", "Professional"),
            show='headings'
        )

        # Set column headings
        self.table.heading("Staff Number", text="Staff Number", anchor=tk.W)
        self.table.heading("First Name", text="First Name", anchor=tk.W)
        self.table.heading("Last Name", text="Last Name", anchor=tk.W)
        self.table.heading("Practicing ID", text="Practicing ID", anchor=tk.W)
        self.table.heading("Address", text="Address", anchor=tk.W)
        self.table.heading("Phone", text="Phone", anchor=tk.W)
        self.table.heading("Registration Date", text="Registration Date", anchor=tk.W)
        self.table.heading("Professional", text="Professional", anchor=tk.W)

        # Set column widths
        self.table.column("Staff Number", width=100)
        self.table.column("First Name", width=100)
        self.table.column("Last Name", width=100)
        self.table.column("Practicing ID", width=100)
        self.table.column("Address", width=150)
        self.table.column("Phone", width=100)
        self.table.column("Registration Date", width=120)
        self.table.column("Professional", width=100)

        # Set the style for the headings
        style = ttk.Style()
        style.configure("Treeview.Heading", background="#2c3e50", foreground="black", font=("Arial", 10, "bold"))

        # Enable horizontal scrolling
        self.scrollbar = ttk.Scrollbar(self.content_frame, orient="horizontal", command=self.table.xview)
        self.table.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(fill=tk.X, side=tk.BOTTOM)

        # Pack the table
        self.table.pack(fill=tk.BOTH, expand=True)

    def add_staff(self):
        first_name = self.entry_first_name.get().strip()
        last_name = self.entry_last_name.get().strip()
        practicing_id = self.entry_practicing_id.get().strip()
        address = self.entry_address.get().strip()
        phone = self.entry_phone.get().strip()
        registration_date = self.entry_registration_date.get().strip()
        professional = self.entry_professional.get().strip()

        if not all([first_name, last_name, practicing_id, address, phone, registration_date, professional]):
            messagebox.showwarning("Input Error", "All fields must be filled out!")
            return

        self.staff_count += 1  # Increment staff count for unique number
        new_staff = Staff(self.staff_count, first_name, last_name, practicing_id, address, phone, registration_date,
                          professional)
        self.staff.append(new_staff)
        self.update_table()

        # Clear entry fields
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_practicing_id.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_registration_date.delete(0, tk.END)
        self.entry_professional.delete(0, tk.END)

        messagebox.showinfo("Success", f"Staff added successfully with Staff Number: {self.staff_count}!")

    def delete_staff(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Selection Error", "Please select a Staff to delete!")
            return

        # Get the staff number from the selected item
        item_values = self.table.item(selected_item)['values']
        staff_number = item_values[0]

        # Remove the staff from the list
        self.staff = [staff for staff in self.staff if staff.staff_number != staff_number]
        self.update_table()
        messagebox.showinfo("Success", f"Staff {staff_number} deleted successfully!")

    def update_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        for staff in self.staff:
            self.table.insert("", "end", values=(
                staff.staff_number, staff.first_name, staff.last_name, staff.practicing_id,
                staff.address, staff.phone, staff.registration_date, staff.professional
            ))


# Switch to Home Page (stub for now)
def switch_to_home():
    root.destroy()
    import home_page_script  # Assuming home_page_script is the file containing the home page


if __name__ == "__main__":
    root = tk.Tk()
    staff_page = StaffPage(root, switch_to_home)
    root.mainloop()
