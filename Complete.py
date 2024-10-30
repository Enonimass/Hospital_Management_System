import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Patient:
    def __init__(self, patient_number, one_name, two_name, insurance, email, telephone, registration):
        self.patient_number = patient_number
        self.one_name = one_name
        self.two_name = two_name
        self.insurance = insurance
        self.email = email
        self.telephone = telephone
        self.registration = registration


class Staff:
    def __init__(self, staff_number, firsta_name, lasta_name, practicing_id, address, phone, registration_date,
                 professional):
        self.staff_number = staff_number
        self.firsta_name = firsta_name
        self.lasta_name = lasta_name
        self.practicing_id = practicing_id
        self.address = address
        self.phone = phone
        self.registration_date = registration_date
        self.professional = professional


class Appointment:
    def __init__(self, appointment_number, patient_name, patient_num, staff_name, staff_num,
                 profession, appointment_date, appointment_time):
        self.appointment_number = appointment_number
        self.patient_name = patient_name
        self.patient_num = patient_num
        self.staff_name = staff_name
        self.staff_num = staff_num
        self.profession = profession
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("St.Mark Hospital Management System")

        # Create container for sections
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # Define home and finance frames
        self.home_frame = tk.Frame(self.container, bg="#2c3e50")
        self.finance_frame = tk.Frame(self.container, bg="#2c3e50")
        self.staff_frame = tk.Frame(self.container, bg="#2c3e50")
        self.patient_frame = tk.Frame(self.container, bg="#2c3e50")
        self.appointment_frame = tk.Frame(self.container, bg="#2c3e50")
        self.sign_frame = tk.Frame(self.container, bg="#2c3e50")

        # ########          H           O               M           E           #######
        # Create home content (replace with your desired widgets)
        self.navbar = tk.Frame(self.home_frame, bg="skyblue")
        self.navbar.pack(side=tk.TOP, fill=tk.X)
        self.label_title = tk.Label(self.navbar, text="St. Mark Hospital - ", bg="skyblue", fg="black",
                                    font=("Arial", 24))
        self.label_title.pack(side=tk.TOP, padx=10, pady=5)

        #Sign in/out Button
        self.sign_button = tk.Button(self.navbar, text="Sign Out", command=self.show_sign, bg="#2c3e50", fg="black")
        self.sign_button.pack(side=tk.LEFT, padx=10)

        home_label = tk.Label(self.home_frame, text="Welcome to the Home Section!")
        home_label.pack()
        # Content Frame with Light Blue Background
        self.content_frame = tk.Frame(self.home_frame, bg="#b2e0f0")  # Light blue background
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Buttons at home page
        patient_button = tk.Button(self.content_frame, text="PATIENTS", command=self.show_patient, bg="skyblue",
                                   fg="black")
        patient_button.pack(pady=20)
        staff_button = tk.Button(self.content_frame, text="STAFF", command=self.show_staff, bg="skyblue",
                                 fg="black")
        staff_button.pack(pady=20)
        finance_button = tk.Button(self.content_frame, text="Finance", command=self.show_finance, bg="skyblue",
                                   fg="black")
        finance_button.pack(pady=20)
        appointment_button = tk.Button(self.content_frame, text="APPOINTMENT", command=self.show_appointment,
                                       bg="skyblue", fg="black")
        appointment_button.pack(pady=20)

        ##########################
        #####################_____________           S      I       G       N       I       N       G       ____________###

        self.navbar = tk.Frame(self.sign_frame, bg="skyblue")
        self.navbar.pack(side=tk.TOP, fill=tk.X)
        self.label_title = tk.Label(self.navbar, text="St. Mark Hospital -  ", bg="skyblue", fg="black",
                                    font=("Arial", 24))
        self.label_title.pack(side=tk.TOP, padx=10, pady=5)

        sign_label = tk.Label(self.sign_frame, text="Every Step of the Way")
        sign_label.pack()

        #Enter the user and credentials
        users = {
            "shaddy": "shaddy123",
            "mark": "mark123",
            "nurse": "nurse123"
        }

        # Function to validate sign-in credentials
        def validate_signin():
            username = self.entry_username.get()
            password = self.entry_password.get()

            if username in users and users[username] == password:
                messagebox.showinfo("Success", "Successfully Signed In" )
                show_dashboard()

                self.clear_staff_fields()
            else:
                self.clear_sign_fields()
                messagebox.showerror("Login Error", "Invalid username or password.")


        def show_dashboard():
            # Hide finance frame
            self.finance_frame.pack_forget()
            self.appointment_frame.pack_forget()
            self.patient_frame.pack_forget()
            self.staff_frame.pack_forget()
            self.sign_frame.pack_forget()

            # Show home frame
            self.home_frame.pack(side="top", fill="both", expand=True)

        # Sign Entry Form
        self.entry_frame = tk.Frame(self.sign_frame, bg="#b2e0f0")  # Light blue background
        self.entry_frame.pack(pady=10)

        self.label_username = tk.Label(self.entry_frame, text="Username:")
        self.label_username.grid(row=1, column=0, padx=5, pady=5)
        self.entry_username = tk.Entry(self.entry_frame)
        self.entry_username.grid(row=1, column=1, padx=5, pady=5)

        self.label_password = tk.Label(self.entry_frame, text="Password:")
        self.label_password.grid(row=2, column=0, padx=5, pady=5)
        #self.entry_password = tk.Entry(self.entry_frame, font="Arial", width=30, show="*")
        #  self.entry_password.pack(pady=10)
        # self.entry_password.insert(0, "Password")
        self.entry_password = tk.Entry(self.entry_frame)
        self.entry_password.grid(row=2, column=1, padx=5, pady=5)

        button_signin = tk.Button(self.sign_frame, text="Sign In", font="Arial", bg="Red", fg="white",
                                  command=validate_signin)
        button_signin.pack(pady=20)



        ####        F       I       N       A       N       C       E       ######

        # Create finance content (replace with your desired widgets)
        # TITLE
        self.navbar = tk.Frame(self.finance_frame, bg="skyblue")
        self.navbar.pack(side=tk.TOP, fill=tk.X)
        self.label_title = tk.Label(self.navbar, text="St. Mark Hospital -  FINANCE", bg="skyblue", fg="black",
                                    font=("Arial", 24))
        self.label_title.pack(side=tk.TOP, padx=10, pady=5)
        # Home Button
        self.home_button = tk.Button(self.navbar, text="Home", command=self.show_home, bg="#2c3e50", fg="black")
        self.home_button.pack(side=tk.LEFT, padx=10)

        finance_label = tk.Label(self.finance_frame, text="This is the Finance Section!")
        finance_label.pack()

        ##################

        ####____________A       P       P       O       I       N       T       M       E       N       T_____________#####
        self.appointment = []
        self.appointment_count = 0
        # Create Appointment content (replace with your desired widgets)
        self.navbar = tk.Frame(self.appointment_frame, bg="skyblue")
        self.navbar.pack(side=tk.TOP, fill=tk.X)
        self.label_title = tk.Label(self.navbar, text="St. Mark Hospital -  Appointment Page", bg="skyblue", fg="black",
                                    font=("Arial", 24))
        self.label_title.pack(side=tk.TOP, padx=10, pady=5)

        # Home Button
        self.home_button = tk.Button(self.navbar, text="Home", command=self.show_home, bg="#2c3e50", fg="black")
        self.home_button.pack(side=tk.LEFT, padx=10)

        appointment_label = tk.Label(self.appointment_frame, text="This is the Appointment!")
        appointment_label.pack()
        self.label_head = tk.Label(self.navbar, text="We Treat, The Lord Heals.", bg="#b2e0f0", fg="black",
                                   font=("Old Times Roman", 24))
        self.label_head.pack(side=tk.TOP, padx=10, pady=5)

        # APPOINTMENT Entry Form
        self.entry_frame = tk.Frame(self.appointment_frame, bg="#b2e0f0")  # Light blue background
        self.entry_frame.pack(pady=10)

        self.label_patient_name = tk.Label(self.entry_frame, text="Patient Name:")
        self.label_patient_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_patient_name = tk.Entry(self.entry_frame)
        self.entry_patient_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_patient_num = tk.Label(self.entry_frame, text="Patient Number:")
        self.label_patient_num.grid(row=1, column=0, padx=5, pady=5)
        self.entry_patient_num = tk.Entry(self.entry_frame)
        self.entry_patient_num.grid(row=1, column=1, padx=5, pady=5)

        self.label_staff_name = tk.Label(self.entry_frame, text="Doctor's Name:")
        self.label_staff_name.grid(row=2, column=0, padx=5, pady=5)
        self.entry_staff_name = tk.Entry(self.entry_frame)
        self.entry_staff_name.grid(row=2, column=1, padx=5, pady=5)

        self.label_profession = tk.Label(self.entry_frame, text="Professional:")
        self.label_profession.grid(row=3, column=0, padx=5, pady=5)
        self.entry_profession = tk.Entry(self.entry_frame)
        self.entry_profession.grid(row=3, column=1, padx=5, pady=5)

        self.label_staff_num = tk.Label(self.entry_frame, text="Staff Number:")
        self.label_staff_num.grid(row=4, column=0, padx=5, pady=5)
        self.entry_staff_num = tk.Entry(self.entry_frame)
        self.entry_staff_num.grid(row=4, column=1, padx=5, pady=5)

        self.label_appointment_date = tk.Label(self.entry_frame, text="Appointment Date:")
        self.label_appointment_date.grid(row=5, column=0, padx=5, pady=5)
        self.entry_appointment_date = tk.Entry(self.entry_frame)
        self.entry_appointment_date.grid(row=5, column=1, padx=5, pady=5)

        self.label_appointment_time = tk.Label(self.entry_frame, text="Appointment Time:")
        self.label_appointment_time.grid(row=6, column=0, padx=5, pady=5)
        self.entry_appointment_time = tk.Entry(self.entry_frame)
        self.entry_appointment_time.grid(row=6, column=1, padx=5, pady=5)

        # Add Appointment Button
        self.add_appointment_button = tk.Button(self.appointment_frame, text="Add Appointment",
                                                command=self.add_appointment, bg="#e74c3c",
                                                fg="white")
        self.add_appointment_button.pack(pady=10)

        # Delete Staff Button
        self.delete_appointment_button = tk.Button(self.appointment_frame, text="Delete Staff",
                                                   command=self.delete_appointment,
                                                   bg="#e74c3c", fg="white")
        self.delete_appointment_button.pack(pady=10)

        # Table to Display
        self.appointment_table = ttk.Treeview(self.appointment_frame, columns=(
            "Appointment Number", "First Name", "Patient Name", "Patient Number", "Staff Name", "Staff Number",
            "Profession", "Appointment Date",
            "Appointment Time"), show='headings')
        self.appointment_table.heading("Appointment Number", text="Appointment Number", anchor=tk.W)
        self.appointment_table.heading("Patient Name", text="Patient Name", anchor=tk.W)
        self.appointment_table.heading("Patient Number", text="Patient Number", anchor=tk.W)
        self.appointment_table.heading("Staff Name", text="Staff Name", anchor=tk.W)
        self.appointment_table.heading("Staff Number", text="Staff Number", anchor=tk.W)
        self.appointment_table.heading("Profession", text="Profession", anchor=tk.W)
        self.appointment_table.heading("Appointment Date", text="Appointment Date", anchor=tk.W)
        self.appointment_table.heading("Appointment Time", text="Appointment Time", anchor=tk.W)

        # Set the style for the headings
        style = ttk.Style()
        style.configure("Treeview.Heading", background="#2c3e50", foreground="black", font=("Arial", 10, "bold"))

        # Pack the appointment table
        self.appointment_table.pack(fill=tk.BOTH, expand=True)

        # Initially show home frame
        self.sign_frame.pack(side="top", fill="both", expand=True)

        ############

        ######      P       A       T       I       E       N       T       #########

        # ###Patient####
        # Create staff
        patient_frame = tk.Frame(self.container, bg="#2c3e50")
        self.patient = []
        self.patient_count = 243  # Initialize patient count

        # navbar
        self.navbar = tk.Frame(self.patient_frame, bg="skyblue")
        self.navbar.pack(side=tk.TOP, fill=tk.X)

        # title
        self.label_title = tk.Label(self.navbar, text="St. Mark Hospital -  Patient-PAGE", bg="skyblue", fg="black",
                                    font=("Arial", 24))
        self.label_title.pack(side=tk.TOP, padx=10, pady=5)

        # Home Button
        self.home_button = tk.Button(self.navbar, text="Home", command=self.show_home, bg="#2c3e50", fg="black")
        self.home_button.pack(side=tk.LEFT, padx=10)

        patient_label = tk.Label(self.patient_frame, text="Every Life Matters")
        patient_label.pack()

        # patient Entry Form
        self.entry_frame = tk.Frame(self.patient_frame, bg="#b2e0f0")  # Light blue background
        self.entry_frame.pack(pady=10)

        self.label_one_name = tk.Label(self.entry_frame, text="First Name:")
        self.label_one_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_one_name = tk.Entry(self.entry_frame)
        self.entry_one_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_two_name = tk.Label(self.entry_frame, text="Last Name:")
        self.label_two_name.grid(row=1, column=0, padx=5, pady=5)
        self.entry_two_name = tk.Entry(self.entry_frame)
        self.entry_two_name.grid(row=1, column=1, padx=5, pady=5)

        self.label_insurance = tk.Label(self.entry_frame, text=" Insurance No:")
        self.label_insurance.grid(row=3, column=0, padx=5, pady=5)
        self.entry_insurance = tk.Entry(self.entry_frame)
        self.entry_insurance.grid(row=3, column=1, padx=5, pady=5)

        self.label_email = tk.Label(self.entry_frame, text="Email:")
        self.label_email.grid(row=4, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(self.entry_frame)
        self.entry_email.grid(row=4, column=1, padx=5, pady=5)

        self.label_telephone = tk.Label(self.entry_frame, text="Phone Number:")
        self.label_telephone.grid(row=5, column=0, padx=5, pady=5)
        self.entry_telephone = tk.Entry(self.entry_frame)
        self.entry_telephone.grid(row=5, column=1, padx=5, pady=5)

        self.label_registration = tk.Label(self.entry_frame, text="Registration Date:")
        self.label_registration.grid(row=6, column=0, padx=5, pady=5)
        self.entry_registration = tk.Entry(self.entry_frame)
        self.entry_registration.grid(row=6, column=1, padx=5, pady=5)

        # Add Patient Button
        self.add_patient_button = tk.Button(self.patient_frame, text="Add Patient", command=self.add_patient,
                                            bg="#e74c3c",
                                            fg="white")
        self.add_patient_button.pack(pady=10)

        # Delete patient Button
        self.delete_patient_button = tk.Button(self.patient_frame, text="Delete Patient", command=self.delete_patient,
                                               bg="#e74c3c", fg="white")
        self.delete_patient_button.pack(pady=10)

        # Table to Display Staff
        self.patient_table = ttk.Treeview(self.patient_frame, columns=(
            "Patient Number", "First Name", "Last Name", "Insurance", "Email", "Telephone", "Registration ",
            "Professional"), show='headings')
        self.patient_table.heading("Patient Number", text="Patient Number", anchor=tk.W)
        self.patient_table.heading("First Name", text="First Name", anchor=tk.W)
        self.patient_table.heading("Last Name", text="Last Name", anchor=tk.W)
        self.patient_table.heading("Insurance", text="Insurance", anchor=tk.W)
        self.patient_table.heading("Email", text="Email", anchor=tk.W)
        self.patient_table.heading("Telephone", text="Telephone", anchor=tk.W)
        self.patient_table.heading("Registration ", text="Registration ", anchor=tk.W)

        # Set the style for the headings
        style = ttk.Style()
        style.configure("Treeview.Heading", background="#2c3e50", foreground="black", font=("Arial", 10, "bold"))
        # Pack the staff table
        self.patient_table.pack(fill=tk.BOTH, expand=True)
        # Initially show home frame
        self.sign_frame.pack(side="top", fill="both", expand=True)

        ############
        ###____________S        T       A       F       F _________  ###########
        # ###Stafff####
        # Create staff
        staff_frame = tk.Frame(self.container, bg="#2c3e50")
        self.staff = []
        self.staff_count = 243  # Initialize staff count
        # TITLE

        self.navbar = tk.Frame(self.staff_frame, bg="skyblue")
        self.navbar.pack(side=tk.TOP, fill=tk.X)
        self.label_title = tk.Label(self.navbar, text="St. Mark Hospital -  STAFF-PAGE", bg="skyblue", fg="black",
                                    font=("Arial", 24))
        # Home Button
        self.home_button = tk.Button(self.navbar, text="Home", command=self.show_home, bg="#2c3e50", fg="black")
        self.home_button.pack(side=tk.LEFT, padx=10)
        self.label_title.pack(side=tk.TOP, padx=10, pady=5)

        staff_label = tk.Label(self.staff_frame, text="This is Staff Section!")
        staff_label.pack()

        # Staff Entry Form
        self.entry_frame = tk.Frame(self.staff_frame, bg="#b2e0f0")  # Light blue background
        self.entry_frame.pack(pady=10)

        self.label_firsta_name = tk.Label(self.entry_frame, text="First Name:")
        self.label_firsta_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_firsta_name = tk.Entry(self.entry_frame)
        self.entry_firsta_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_lasta_name = tk.Label(self.entry_frame, text="Last Name:")
        self.label_lasta_name.grid(row=1, column=0, padx=5, pady=5)
        self.entry_lasta_name = tk.Entry(self.entry_frame)
        self.entry_lasta_name.grid(row=1, column=1, padx=5, pady=5)

        self.label_practicing_number = tk.Label(self.entry_frame, text="Practicing No:")
        self.label_practicing_number.grid(row=3, column=0, padx=5, pady=5)
        self.entry_practicing_number = tk.Entry(self.entry_frame)
        self.entry_practicing_number.grid(row=3, column=1, padx=5, pady=5)

        self.label_address = tk.Label(self.entry_frame, text="Address:")
        self.label_address.grid(row=4, column=0, padx=5, pady=5)
        self.entry_address = tk.Entry(self.entry_frame)
        self.entry_address.grid(row=4, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(self.entry_frame, text="Phone Number:")
        self.label_phone.grid(row=5, column=0, padx=5, pady=5)
        self.entry_phone = tk.Entry(self.entry_frame)
        self.entry_phone.grid(row=5, column=1, padx=5, pady=5)

        self.label_registration_date = tk.Label(self.entry_frame, text="Registration Date:")
        self.label_registration_date.grid(row=6, column=0, padx=5, pady=5)
        self.entry_registration_date = tk.Entry(self.entry_frame)
        self.entry_registration_date.grid(row=6, column=1, padx=5, pady=5)

        self.label_professional = tk.Label(self.entry_frame, text="Professional:")
        self.label_professional.grid(row=7, column=0, padx=5, pady=5)
        self.entry_professional = tk.Entry(self.entry_frame)
        self.entry_professional.grid(row=7, column=1, padx=5, pady=5)

        # Add Staff Button
        self.add_staff_button = tk.Button(self.staff_frame, text="Add Staff", command=self.add_staff, bg="#e74c3c",
                                          fg="white")
        self.add_staff_button.pack(pady=10)

        # Delete Staff Button
        self.delete_staff_button = tk.Button(self.staff_frame, text="Delete Staff", command=self.delete_staff,
                                             bg="#e74c3c", fg="white")
        self.delete_staff_button.pack(pady=10)

        # Table to Display Staff
        self.staff_table = ttk.Treeview(self.staff_frame, columns=(
            "Staff Number", "First Name", "Last Name", "Practicing ID", "Address", "Phone", "Registration Date",
            "Professional"), show='headings')
        self.staff_table.heading("Staff Number", text="Staff Number", anchor=tk.W)
        self.staff_table.heading("First Name", text="First Name", anchor=tk.W)
        self.staff_table.heading("Last Name", text="Last Name", anchor=tk.W)
        self.staff_table.heading("Practicing ID", text="Practicing ID", anchor=tk.W)
        self.staff_table.heading("Address", text="Address", anchor=tk.W)
        self.staff_table.heading("Phone", text="Phone", anchor=tk.W)
        self.staff_table.heading("Registration Date", text="Registration Date", anchor=tk.W)
        self.staff_table.heading("Professional", text="Professional", anchor=tk.W)

        # Set the style for the headings
        style = ttk.Style()
        style.configure("Treeview.Heading", background="#2c3e50", foreground="black", font=("Arial", 10, "bold"))

        # Pack the staff table
        self.staff_table.pack(fill=tk.BOTH, expand=True)

        # Initially show Sign_Frame frame
        self.sign_frame.pack(side="top", fill="both", expand=True)

    def show_home(self):
        # Hide finance frame
        self.finance_frame.pack_forget()
        self.appointment_frame.pack_forget()
        self.patient_frame.pack_forget()
        self.staff_frame.pack_forget()
        self.sign_frame.pack_forget()

        # Show sign frame
        self.home_frame.pack(side="top", fill="both", expand=True)

    def show_appointment(self):
        self.finance_frame.pack_forget()
        self.home_frame.pack_forget()
        self.patient_frame.pack_forget()
        self.staff_frame.pack_forget()
        self.sign_frame.pack_forget()

        self.appointment_frame.pack(side="top", fill="both", expand=True)

    def show_finance(self):
        # Hide home frame
        self.home_frame.pack_forget()
        self.appointment_frame.pack_forget()
        self.patient_frame.pack_forget()
        self.staff_frame.pack_forget()
        self.sign_frame.pack_forget()

        # Show finance frame
        self.finance_frame.pack(side="top", fill="both", expand=True)

    def show_patient(self):
        # Hide home frame
        self.home_frame.pack_forget()
        self.appointment_frame.pack_forget()
        self.finance_frame.pack_forget()
        self.staff_frame.pack_forget()
        self.sign_frame.pack_forget()

        # Show finance frame
        self.patient_frame.pack(side="top", fill="both", expand=True)

    def show_sign(self):
        # Hide Sign frame
        self.home_frame.pack_forget()
        self.appointment_frame.pack_forget()
        self.finance_frame.pack_forget()
        self.staff_frame.pack_forget()
        self.sign_frame.pack_forget()

        # Show finance frame
        self.sign_frame.pack(side="top", fill="both", expand=True)

    def show_staff(self):
        # Hide home frame
        self.home_frame.pack_forget()
        self.appointment_frame.pack_forget()
        self.patient_frame.pack_forget()
        self.finance_frame.pack_forget()
        self.sign_frame.pack_forget()

        # Show finance frame
        self.staff_frame.pack(side="top", fill="both", expand=True)

    def add_patient(self):
        one_name = self.entry_one_name.get()
        two_name = self.entry_two_name.get()
        insurance = self.entry_insurance.get()
        email = self.entry_email.get()
        telephone = self.entry_telephone.get()
        registration = self.entry_registration.get()

        if (one_name and two_name and insurance
                and email and telephone and registration):
            self.patient_count += 1  # Increment staff count
            patient = Patient(self.staff_count, one_name, two_name, insurance, email, telephone, registration)
            self.patient.append(patient)
            self.patient_table.insert("", "end", values=(
                patient.patient_number, patient.one_name, patient.two_name, patient.insurance, patient.email,
                patient.telephone, patient.registration))
            self.clear_patient_fields()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

        messagebox.showinfo("Success", " Successfully Added patient")

    def delete_patient(self):
        selected_item = self.patient_table.selection()
        if selected_item:
            self.patient_table.delete(selected_item)
            messagebox.showinfo("Success", "Successfully Deleted a patient")
        else:
            messagebox.showwarning("Selection Error", "Please select a patient to delete.")

    def clear_patient_fields(self):
        self.entry_one_name.delete(0, tk.END)
        self.entry_two_name.delete(0, tk.END)
        self.entry_insurance.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telephone.delete(0, tk.END)
        self.entry_registration.delete(0, tk.END)

    def add_staff(self):
        firsta_name = self.entry_firsta_name.get()
        lasta_name = self.entry_lasta_name.get()
        # registration_number = self.entry_registration_number.get()
        practicing_number = self.entry_practicing_number.get()
        address = self.entry_address.get()
        phone = self.entry_phone.get()
        registration_date = self.entry_registration_date.get()
        professional = self.entry_professional.get()

        if (firsta_name and lasta_name and practicing_number
                and address and phone and registration_date and professional):
            self.staff_count += 1  # Increment staff count
            staff = Staff(self.staff_count, firsta_name, lasta_name, practicing_number, address, phone,
                          registration_date,
                          professional)
            self.staff.append(staff)
            self.staff_table.insert("", "end", values=(
                staff.staff_number, staff.firsta_name, staff.lasta_name, staff.practicing_id, staff.address,
                staff.phone,
                staff.registration_date, staff.professional))
            self.clear_staff_fields()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

        messagebox.showinfo("Success", " Successfully Added staff")

    def delete_staff(self):
        selected_item = self.staff_table.selection()
        if selected_item:
            self.staff_table.delete(selected_item)
            messagebox.showinfo("Success", "Successfully Deleted a Staff")
        else:
            messagebox.showwarning("Selection Error", "Please select a staff member to delete.")

    def clear_staff_fields(self):
        self.entry_firsta_name.delete(0, tk.END)
        self.entry_lasta_name.delete(0, tk.END)
        self.entry_practicing_number.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_registration_date.delete(0, tk.END)
        self.entry_professional.delete(0, tk.END)

    def add_appointment(self):
        patient_name = self.entry_patient_name.get()
        patient_num = self.entry_patient_num.get()
        staff_name = self.entry_staff_name.get()
        profession = self.entry_profession.get()
        staff_num = self.entry_staff_num.get()
        appointment_date = self.entry_appointment_date.get()
        appointment_time = self.entry_appointment_time.get()

        if (patient_name and patient_num and staff_name and profession and
                staff_num and appointment_date and appointment_time):
            self.appointment_count += 1  # Increment appointment count
            appointment = Appointment(self.appointment_count, patient_name, patient_num,
                                      staff_name, profession, staff_num, appointment_date, appointment_time)
            self.appointment.append(appointment)
            self.appointment_table.insert("", "end", values=(
                appointment.appointment_number, appointment.patient_name, appointment.patient_num,
                appointment.staff_name,
                appointment.profession, appointment.staff_num, appointment.appointment_date,
                appointment.appointment_number))
            self.clear_appointment_fields()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

        messagebox.showinfo("Success", " Successfully Added an Appointment")

    def delete_appointment(self):
        selected_item = self.appointment_table.selection()
        if selected_item:
            self.appointment_table.delete(selected_item)
            messagebox.showinfo("Success", "Successfully Deleted an Appointment")
        else:
            messagebox.showwarning("Selection Error", "Please select an appointment to delete.")

    def clear_appointment_fields(self):
        self.entry_patient_name.delete(0, tk.END)
        self.entry_patient_num.delete(0, tk.END)
        self.entry_staff_name.delete(0, tk.END)
        self.entry_professional.delete(0, tk.END)
        self.entry_staff_num.delete(0, tk.END)
        self.entry_appointment_date.delete(0, tk.END)
        self.entry_appointment_time.delete(0, tk.END)

    def clear_sign_fields(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
