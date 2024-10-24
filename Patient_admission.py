import tkinter as tk
from tkinter import messagebox, ttk


class Patient:
    def __init__(self, patient_number, first_name, last_name, insurance, address, phone, registration_date):
        self.patient_number = patient_number
        self.first_name = first_name
        self.last_name = last_name
        self.insurance = insurance
        self.address = address
        self.phone = phone
        self.registration_date = registration_date


class PatientPage:
    def __init__(self, root, switch_to_home):
        self.root = root
        self.switch_to_home = switch_to_home
        self.root.title("St. Mark Hospital - Patient Page")
        self.root.geometry("600x400")
        self.patients = []
        self.patient_count = 0  # Initialize patient count

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

        # Patient Entry Form
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

        self.label_insurance = tk.Label(self.entry_frame, text="Insurance No:")
        self.label_insurance.grid(row=2, column=0, padx=5, pady=5)
        self.entry_insurance = tk.Entry(self.entry_frame)
        self.entry_insurance.grid(row=2, column=1, padx=5, pady=5)

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

        # Add Patient Button
        self.add_patient_button = tk.Button(self.content_frame, text="Add Patient", command=self.add_patient,
                                            bg="#e74c3c", fg="white")
        self.add_patient_button.pack(pady=10)

        # Delete Patient Button
        self.delete_patient_button = tk.Button(self.content_frame, text="Delete Patient", command=self.delete_patient,
                                               bg="#e74c3c", fg="white")
        self.delete_patient_button.pack(pady=10)

        # Table to Display Patients
        self.table = ttk.Treeview(self.content_frame, columns=(
        "Patient Number", "First Name", "Last Name", "Insurance", "Address", "Phone", "Registration Date"),
                                  show='headings')
        self.table.heading("Patient Number", text="Patient Number", anchor=tk.W)
        self.table.heading("First Name", text="First Name", anchor=tk.W)
        self.table.heading("Last Name", text="Last Name", anchor=tk.W)
        self.table.heading("Insurance", text="Insurance", anchor=tk.W)
        self.table.heading("Address", text="Address", anchor=tk.W)
        self.table.heading("Phone", text="Phone", anchor=tk.W)
        self.table.heading("Registration Date", text="Registration Date", anchor=tk.W)

        # Set the style for the headings
        style = ttk.Style()
        style.configure("Treeview.Heading", background="#2c3e50", foreground="black", font=("Arial", 10, "bold"))

        # Pack the table
        self.table.pack(fill=tk.BOTH, expand=True)

    def add_patient(self):
        first_name = self.entry_first_name.get().strip()
        last_name = self.entry_last_name.get().strip()
        insurance = self.entry_insurance.get().strip()
        address = self.entry_address.get().strip()
        phone = self.entry_phone.get().strip()
        registration_date = self.entry_registration_date.get().strip()

        if not all([first_name, last_name, insurance, address, phone, registration_date]):
            messagebox.showwarning("Input Error", "All fields must be filled out!")
            return

        self.patient_count += 7  # Increment patient count for unique number
        new_patient = Patient(self.patient_count, first_name, last_name, insurance, address, phone, registration_date)
        self.patients.append(new_patient)
        self.update_table()

        # Clear entry fields
        self.entry_first_name.delete(0, tk.END)
        self.entry_last_name.delete(0, tk.END)
        self.entry_insurance.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_registration_date.delete(0, tk.END)

        messagebox.showinfo("Success", f"Patient added successfully with Patient Number: {self.patient_count}!")

    def delete_patient(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showerror("Selection Error", "Please select a patient to delete!")
            return

        # Get the patient number from the selected item
        item_values = self.table.item(selected_item)['values']
        patient_number = item_values[0]

        # Remove the patient from the list
        self.patients = [patient for patient in self.patients if patient.patient_number != patient_number]
        self.update_table()
        messagebox.showinfo("Success", f"Patient {patient_number} deleted successfully!")

    def update_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        for patient in self.patients:
            self.table.insert("", "end", values=(
            patient.patient_number, patient.first_name, patient.last_name, patient.insurance, patient.address,
            patient.phone, patient.registration_date))


# Switch to Home Page (stub for now)
def switch_to_home():
    root.destroy()
    import home_page_script  # Assuming home_page_script is the file containing the home page


if __name__ == "__main__":
    root = tk.Tk()
    patient_page = PatientPage(root, switch_to_home)
    root.mainloop()
