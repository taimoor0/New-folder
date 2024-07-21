import customtkinter as ctk
from PIL import Image, ImageTk
from image_processing.image_processing import Camera


class CustomMessageBox(ctk.CTkToplevel):
    def __init__(self, app, title, message):
        super().__init__(app)
        self.title(title)
        self.geometry("350x250")
        # self.resizable(False, False)

        label = ctk.CTkLabel(self, text=message, font=("Arial", 16))
        label.pack(pady=20)

        button = ctk.CTkButton(self, text="OK", command=self.destroy)
        button.pack(pady=10)


class UI:
    def __init__(self, app, user_model):
        self.app = app
        self.user_model = user_model
        self.camera = Camera(app, self)
        self.camera_running = self.camera.camera_running

    def create_login_frame(self):
        self.clear_frame()

        # Configure the grid for the main app to have two columns
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_columnconfigure(1, weight=1)

        self.main_frame = ctk.CTkFrame(self.app, fg_color="transparent")
        self.main_frame.grid(row=0, column=0, columnspan=2, padx=60, pady=20, sticky="nsew")

        # Configure the main_frame to have two columns
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Create and configure the image frame
        self.image_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.image_frame.grid(row=0, column=0, sticky="nsew")

        # * Add an image to the image_frame
        image_path = "image2.jpg"
        image = Image.open(image_path)

        def resize_image(event):
            new_width = 1000
            new_height = event.height
            resized_image = image.resize((new_width, new_height))
            self.image_label.configure(image=ImageTk.PhotoImage(resized_image))
            self.image_label.image = ImageTk.PhotoImage(resized_image)

        self.image_frame.bind("<Configure>", resize_image)
        self.image_label = ctk.CTkLabel(self.image_frame)
        self.image_label.grid(row=0, column=0, sticky="nsew")

        # * Create and configure the login frame
        self.login_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.login_frame.grid(row=0, column=1, pady=300, sticky="nsew")

        self.login_label = ctk.CTkLabel(self.login_frame, text="Login", font=("Arial", 24))
        self.login_label.grid(row=0, column=0, columnspan=2, pady=12, padx=10, sticky="nsew")

        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="User Name", width=200)
        self.username_entry.grid(row=1, column=0, columnspan=2, pady=12, padx=10, sticky="nsew")

        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*", width=200)
        self.password_entry.grid(row=2, column=0, columnspan=2, pady=12, padx=10, sticky="nsew")

        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=3, column=0, pady=12, padx=30, sticky="nsew")

        self.signup_button = ctk.CTkButton(self.login_frame, text="Sign Up", command=self.create_signup_frame)
        self.signup_button.grid(row=3, column=1, pady=12, padx=10, sticky="nsew")

    def create_signup_frame(self):
        self.clear_frame()

        # Configure the grid for the main app to have two columns
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_columnconfigure(1, weight=1)

        self.main_frame = ctk.CTkFrame(self.app, width=800, height=600, fg_color="transparent")
        self.main_frame.grid(row=0, column=0, columnspan=2, padx=60, pady=20, sticky="nsew")

        # Configure the main_frame to have two columns
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Create and configure the image frame
        self.image_frame = ctk.CTkFrame(self.main_frame, width=400, height=600, fg_color="transparent")
        self.image_frame.grid(row=0, column=0, sticky="nsew")

        # Add an image to the image_frame
        image_path = "image3.jpg"
        image = Image.open(image_path)

        # Resize the image to fit the image_frame
        def resize_image(event):
            new_width = 900
            new_height = event.height
            resized_image = image.resize((new_width, new_height))
            self.image_label.configure(image=ImageTk.PhotoImage(resized_image))
            self.image_label.image = ImageTk.PhotoImage(resized_image)

        # Bind the resize event to the image_frame
        self.image_frame.bind("<Configure>", resize_image)

        self.image_label = ctk.CTkLabel(self.image_frame)
        self.image_label.grid(row=0, column=0, sticky="nsew")

        # Create and configure the signup frame
        self.signup_frame = ctk.CTkFrame(self.main_frame, width=400, height=600, fg_color="transparent")
        self.signup_frame.grid(row=0, column=1, pady=60, padx=30, sticky="nsew")

        # Add signup label
        self.signup_label = ctk.CTkLabel(self.signup_frame, text="Sign Up", font=("Arial", 24))
        self.signup_label.grid(row=0, column=0, columnspan=2, pady=12, padx=10, sticky="nsew")

        # Add username entry
        self.signup_username_entry = ctk.CTkEntry(self.signup_frame, placeholder_text="User Name", width=300)
        self.signup_username_entry.grid(row=1, column=0, columnspan=2, pady=12, padx=10, sticky="nsew")

        # Add password entry
        self.signup_password_entry = ctk.CTkEntry(self.signup_frame, placeholder_text="Password", show="*", width=300)
        self.signup_password_entry.grid(row=2, column=0, columnspan=2, pady=12, padx=10, sticky="nsew")

        # Add full name entry
        self.signup_full_name_entry = ctk.CTkEntry(self.signup_frame, placeholder_text="Full Name", width=300)
        self.signup_full_name_entry.grid(row=3, column=0, columnspan=2, pady=12, padx=10, sticky="nsew")

        # Add contact number entry
        self.signup_contact_number_entry = ctk.CTkEntry(self.signup_frame, placeholder_text="Contact Number", width=300)
        self.signup_contact_number_entry.grid(row=4, column=0, columnspan=2, pady=12, padx=10, sticky="nsew")

        # Add national ID entry
        self.signup_national_id_entry = ctk.CTkEntry(self.signup_frame, placeholder_text="National ID", width=300)
        self.signup_national_id_entry.grid(row=5, column=0, columnspan=2, pady=12, padx=10, sticky="nsew")

        # Add signup button
        self.signup_button = ctk.CTkButton(self.signup_frame, text="Sign Up", command=self.signup, width=140)
        self.signup_button.grid(row=6, column=0, pady=12, padx=10, sticky="nsew")

        # Add back to login button
        self.back_to_login_button = ctk.CTkButton(self.signup_frame, text="Back to Login", command=self.create_login_frame, width=140)
        self.back_to_login_button.grid(row=6, column=1, pady=12, padx=10, sticky="nsew")

    def clear_frame(self):
        for widget in self.app.winfo_children():
            widget.destroy()

    def login(self):
        self.username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.user_model.get_user(self.username)
        if user and user.password == password:
            if user.is_admin:
                self.create_logout_frame_for_admin()
            else:
                if user.total_violation_count >= 10:
                    CustomMessageBox(
                        self.app, "Gear Detection Result", "You are blacklisted and cannot login because you have exceeded the violation limit."
                    )
                else:
                    self.create_logout_frame_for_employee()
                    self.toggle_camera()
        else:
            CustomMessageBox(self.app, "Login Failed", "Login Failed, User does not exist.")

    def signup(self):
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()
        full_name = self.signup_full_name_entry.get()
        contact_number = self.signup_contact_number_entry.get()
        national_id = self.signup_national_id_entry.get()
        if self.user_model.create_user(
            username=username,
            password=password,
            full_name=full_name,
            contact_number=contact_number,
            national_id=national_id,
        ):
            self.create_login_frame()
        else:
            CustomMessageBox(self.app, "Signup Failed", "Signup Failed, username already exist")

    # * ----------------------------------------------------------------
    # *             ADMIN
    # * ----------------------------------------------------------------

    def create_logout_frame_for_admin(self):
        self.clear_frame()
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)

        # Create the main logout frame
        self.main_content_for_admin_frame = ctk.CTkFrame(self.app, fg_color="transparent")
        self.main_content_for_admin_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew")
        self.main_content_for_admin_frame.grid_rowconfigure(0, weight=0)
        self.main_content_for_admin_frame.grid_rowconfigure(1, weight=1)
        self.main_content_for_admin_frame.grid_columnconfigure(0, weight=1)

        # Create the header frame
        self.header_frame = ctk.CTkFrame(self.main_content_for_admin_frame, fg_color="lightgrey", corner_radius=10)
        self.header_frame.grid(row=0, column=0, sticky="ew", pady=(10, 20))
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=1)

        # self.logout_label = ctk.CTkLabel(self.header_frame, text=f"Welcome {self.username}", font=("Arial", 18, "bold"))
        self.logout_label = ctk.CTkLabel(self.header_frame, text=f"Welcome Admin", font=("Arial", 18, "bold"))
        self.logout_label.grid(row=0, column=0, pady=12, padx=30, sticky="nsw")

        self.logout_button = ctk.CTkButton(self.header_frame, text="Sign Out", command=self.create_login_frame)
        self.logout_button.grid(row=0, column=1, pady=12, padx=10, sticky="nse")

        # Create the content frame
        self.content_frame = ctk.CTkFrame(self.main_content_for_admin_frame, fg_color="transparent", corner_radius=10)
        self.content_frame.grid(row=1, column=0, sticky="nsew")

        self.content_frame.grid_rowconfigure(0, weight=0)
        self.content_frame.grid_rowconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        # Fetch the user list
        user_list = self.user_model.get_all_user()

        self.employee_detail_label = ctk.CTkLabel(self.content_frame, text=f"User Detail", font=("Arial", 18, "bold"))
        self.employee_detail_label.grid(row=0, column=0, pady=12, padx=10, sticky="nsew")

        self.add_new_user_label = ctk.CTkButton(self.content_frame, text="Add New User", command=self.create_new_user_by_admin)
        self.add_new_user_label.grid(row=0, column=0, pady=12, padx=30, sticky="nse")

        # Create a new frame for the table
        self.table_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent", corner_radius=10)
        self.table_frame.grid(row=1, column=0, pady=12, padx=10, sticky="nsew")

        # Create the table header
        headers = [
            "User ID",
            "User Name",
            "Full Name",
            "Contact Number",
            "National ID",
            "Role",
            "Total Violations",
            "Is Helmet Check",
            "Is Vest Check",
            "Is Googles Check",
            "Is Gloves Check",
            "Is Boots Check",
            "Update User",
            "Delete User",
        ]
        for col, header in enumerate(headers):
            header_label = ctk.CTkLabel(self.table_frame, text=header, font=("Arial", 12, "bold"), text_color="black", fg_color="pink", height=50)
            header_label.grid(row=0, column=col, pady=5, sticky="nsew")

        # Populate the table with user data
        for row, user in enumerate(user_list, start=1):
            user_id_label = ctk.CTkLabel(self.table_frame, text=user.user_id, text_color="black")
            user_id_label.grid(row=row, column=0, pady=5, padx=5, sticky="nsew")

            name_label = ctk.CTkLabel(self.table_frame, text=user.username, text_color="black")
            name_label.grid(row=row, column=1, pady=5, padx=5, sticky="nsew")

            full_name_label = ctk.CTkLabel(self.table_frame, text=user.full_name, text_color="black")
            full_name_label.grid(row=row, column=2, pady=5, padx=5, sticky="nsew")

            contact_number_label = ctk.CTkLabel(self.table_frame, text=user.contact_number, text_color="black")
            contact_number_label.grid(row=row, column=3, pady=5, padx=5, sticky="nsew")

            national_id_label = ctk.CTkLabel(self.table_frame, text=user.national_id, text_color="black")
            national_id_label.grid(row=row, column=4, pady=5, padx=5, sticky="nsew")

            user_type_label = ctk.CTkLabel(self.table_frame, text=user.user_type, text_color="black")
            user_type_label.grid(row=row, column=5, pady=5, padx=5, sticky="nsew")

            total_violation_count = f"{user.total_violation_count} / 10"
            user_type_label = ctk.CTkLabel(
                self.table_frame, text=total_violation_count, text_color="black", fg_color="red" if user.total_violation_count >= 10 else "white"
            )
            user_type_label.grid(row=row, column=6, pady=5, padx=5, sticky="nsew")

            ctk.CTkLabel(
                self.table_frame,
                text="Active" if user.is_helmet_check.lower() == "active" else "Disable",
                text_color="black",
                fg_color="orange" if user.is_helmet_check.lower() == "active" else "red",
            ).grid(row=row, column=7, pady=5, padx=5, sticky="nsew")
            ctk.CTkLabel(
                self.table_frame,
                text="Active" if user.is_vest_check.lower() == "active" else "Disable",
                text_color="black",
                fg_color="orange" if user.is_vest_check.lower() == "active" else "red",
            ).grid(row=row, column=8, pady=5, padx=5, sticky="nsew")
            ctk.CTkLabel(
                self.table_frame,
                text="Active" if user.is_goggles_check.lower() == "active" else "Disable",
                text_color="black",
                fg_color="orange" if user.is_goggles_check.lower() == "active" else "red",
            ).grid(row=row, column=9, pady=5, padx=5, sticky="nsew")
            ctk.CTkLabel(
                self.table_frame,
                text="Active" if user.is_gloves_check.lower() == "active" else "Disable",
                text_color="black",
                fg_color="orange" if user.is_gloves_check.lower() == "active" else "red",
            ).grid(row=row, column=10, pady=5, padx=5, sticky="nsew")
            ctk.CTkLabel(
                self.table_frame,
                text="Active" if user.is_boots_check.lower() == "active" else "Disable",
                text_color="black",
                fg_color="orange" if user.is_boots_check.lower() == "active" else "red",
            ).grid(row=row, column=11, pady=5, padx=5, sticky="nsew")

            self.update_user_label = ctk.CTkButton(self.table_frame, text="Update", command=lambda u=user.user_id: self.update_user_by_admin(u))
            self.update_user_label.grid(row=row, column=12, pady=5, padx=5, sticky="nsew")

            self.delete_user_label = ctk.CTkButton(self.table_frame, text="Delete", command=lambda u=user.user_id: self.delete_user_by_admin(u))
            self.delete_user_label.grid(row=row, column=13, pady=5, padx=5, sticky="nsew")

        # Configure grid layout for proper resizing
        for col in range(len(headers)):
            self.table_frame.grid_columnconfigure(col, weight=1)

    # ? UPDATE A USER
    def update_user_by_admin(self, user_id):
        self.clear_frame()
        user = self.user_model.get_user_by_id(user_id)

        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self.app, width=800, height=1000, fg_color="transparent")
        self.main_frame.grid(row=0, column=0, columnspan=2, padx=60, pady=20, sticky="nsew")

        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Add form label
        self.form_label = ctk.CTkLabel(self.main_frame, text="Update a User", font=("Arial", 24))
        self.form_label.grid(row=0, column=0, pady=12, padx=10, sticky="nsew")

        # Create and configure the form frame
        self.form_frame = ctk.CTkFrame(self.main_frame, width=400, height=600, fg_color="transparent")
        self.form_frame.grid(row=1, column=0, padx=30, sticky="nsew")
        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_columnconfigure(1, weight=1)
        self.form_frame.grid_columnconfigure(2, weight=1)

        # Create input fields with the current user details pre-filled
        ctk.CTkLabel(self.form_frame, text="User Name", font=("Arial", 24)).grid(row=0, column=0, pady=10, padx=10, sticky="nsw")
        self.username_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Username",
            corner_radius=10,
            height=40,
        )
        self.username_entry.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")
        self.username_entry.insert(0, user.username)

        ctk.CTkLabel(self.form_frame, text="Full Name", font=("Arial", 24)).grid(row=0, column=1, pady=10, padx=10, sticky="nsw")
        self.full_name_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Full Name",
            corner_radius=10,
            height=40,
        )
        self.full_name_entry.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")
        self.full_name_entry.insert(0, user.full_name)

        ctk.CTkLabel(self.form_frame, text="Contact Number", font=("Arial", 24)).grid(row=0, column=2, pady=10, padx=10, sticky="nsw")
        self.contact_number_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Contact Number",
            corner_radius=10,
            height=40,
        )
        self.contact_number_entry.grid(row=1, column=2, pady=10, padx=10, sticky="nsew")
        self.contact_number_entry.insert(0, user.contact_number)

        ctk.CTkLabel(self.form_frame, text="National ID", font=("Arial", 24)).grid(row=2, column=0, pady=10, padx=10, sticky="nsw")
        self.national_id_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="National ID",
            corner_radius=10,
            height=40,
        )
        self.national_id_entry.grid(row=3, column=0, pady=10, padx=10, sticky="nsew")
        self.national_id_entry.insert(0, user.national_id)

        # Add user type combobox
        ctk.CTkLabel(self.form_frame, text="User Role", font=("Arial", 24)).grid(row=2, column=1, pady=10, padx=10, sticky="nsw")
        user_types = ["Guest", "Worker", "Employee"]
        self.user_type_combobox = ctk.CTkComboBox(
            self.form_frame,
            values=user_types,
            corner_radius=10,
            height=40,
        )
        self.user_type_combobox.grid(row=3, column=1, pady=10, padx=10, sticky="nsew")

        if user.user_type in user_types:
            self.user_type_combobox.set(user.user_type)
        else:
            self.user_type_combobox.set("Guest")

        self.gear_vars = {
            "Helmet": ctk.StringVar(value="active" if user.is_helmet_check == "active" else "disable"),
            "Vest": ctk.StringVar(value="active" if user.is_vest_check == "active" else "disable"),
            "Goggles": ctk.StringVar(value="active" if user.is_goggles_check == "active" else "disable"),
            "Gloves": ctk.StringVar(value="active" if user.is_gloves_check == "active" else "disable"),
            "Boots": ctk.StringVar(value="active" if user.is_boots_check == "active" else "disable"),
        }

        ctk.CTkLabel(self.form_frame, text="Verification Check", font=("Arial", 18, "bold")).grid(
            row=4, column=0, columnspan=2, pady=10, padx=10, sticky="w"
        )
        row_idx = 5
        for gear, var in self.gear_vars.items():
            ctk.CTkCheckBox(
                self.form_frame,
                text=gear,
                variable=var,
                onvalue="active",
                offvalue="disable",
            ).grid(row=row_idx, column=0, pady=10, padx=10, sticky="w")
            row_idx += 1

        # * Add Violation section
        violation_counts = {
            "Helmet": user.helmet_voilation_count,
            "Vest": user.vest_voilation_count,
            "Goggles": user.goggles_Voilation_count,
            "Gloves": user.gloves_voilation_count,
            "Boots": user.boots_voilation_count,
        }
        total_violations = sum(violation_counts.values())

        ctk.CTkLabel(self.form_frame, text="Violation", font=("Arial", 18, "bold")).grid(row=4, column=1, columnspan=2, pady=10, padx=10, sticky="w")
        row_idx = 5
        ctk.CTkLabel(self.form_frame, text="Name", font=("Arial", 14, "bold")).grid(row=row_idx, column=1, pady=10, padx=10, sticky="w")
        ctk.CTkLabel(self.form_frame, text="Count", font=("Arial", 14, "bold")).grid(row=row_idx, column=2, pady=10, padx=10, sticky="w")
        row_idx += 1

        for gear, count in violation_counts.items():
            ctk.CTkLabel(self.form_frame, text=gear, font=("Arial", 14)).grid(row=row_idx, column=1, pady=10, padx=10, sticky="w")
            ctk.CTkLabel(self.form_frame, text=str(count), font=("Arial", 14)).grid(row=row_idx, column=2, pady=10, padx=10, sticky="w")
            row_idx += 1

        # Display total violations
        ctk.CTkLabel(self.form_frame, text="Total", font=("Arial", 14, "bold")).grid(row=row_idx, column=1, pady=10, padx=10, sticky="w")
        ctk.CTkLabel(self.form_frame, text=str(total_violations), font=("Arial", 14, "bold")).grid(
            row=row_idx, column=2, pady=10, padx=10, sticky="w"
        )

        # Add back to admin dashboard button
        self.back_to_admin_dashboard_button = ctk.CTkButton(
            self.form_frame,
            text="Back to Dashboard",
            command=self.create_logout_frame_for_admin,
            width=140,
            fg_color="red",
            text_color="black",
            corner_radius=10,
            height=40,
        )
        self.back_to_admin_dashboard_button.grid(row=14, column=1, pady=(20, 0), padx=10, sticky="nsew")

        # Update user button
        self.add_user_button = ctk.CTkButton(
            self.form_frame,
            text="Update User",
            command=lambda: self.save_updated_user_details(user_id),
            width=140,
            fg_color="yellow",
            text_color="black",
            corner_radius=10,
            height=40,
        )
        self.add_user_button.grid(row=14, column=2, pady=(20, 0), padx=10, sticky="nsew")

    def save_updated_user_details(self, user_id):
        username = self.username_entry.get()
        full_name = self.full_name_entry.get()
        contact_number = self.contact_number_entry.get()
        national_id = self.national_id_entry.get()
        user_type = self.user_type_combobox.get()

        # Collect safety gear values
        is_helmet_check = self.gear_vars["Helmet"].get()
        is_vest_check = self.gear_vars["Vest"].get()
        is_goggles_check = self.gear_vars["Goggles"].get()
        is_gloves_check = self.gear_vars["Gloves"].get()
        is_boots_check = self.gear_vars["Boots"].get()

        if self.user_model.update_user_by_admin(
            user_id,
            username,
            full_name,
            contact_number,
            national_id,
            user_type,
            is_helmet_check,
            is_vest_check,
            is_goggles_check,
            is_gloves_check,
            is_boots_check,
        ):
            CustomMessageBox(self.app, "Success", "User updated successfully.")
            self.create_logout_frame_for_admin()
        else:
            CustomMessageBox(self.app, "Error", "Failed to update user. Please try again.")

    # ? DELETE A USER
    def delete_user_by_admin(self, user_id):
        # Attempt to delete the user via the UserModel
        if self.user_model.delete_user(user_id):
            CustomMessageBox(self.app, "Success", "User deleted successfully.")
        else:
            CustomMessageBox(self.app, "Error", "Failed to delete user. Please try again.")

        # Refresh the admin frame to show the updated user list
        self.create_logout_frame_for_admin()

    # ? CREATE NEW USER
    def create_new_user_by_admin(self):
        self.clear_frame()

        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self.app, width=600, height=400, fg_color="transparent")
        self.main_frame.grid(row=0, column=0, columnspan=2, padx=40, pady=20, sticky="nsew")

        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Add form label
        self.form_label = ctk.CTkLabel(self.main_frame, text="Add New User", font=("Arial", 18))
        self.form_label.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        # Create and configure the form frame
        self.form_frame = ctk.CTkFrame(self.main_frame, width=300, height=400, fg_color="transparent")
        self.form_frame.grid(row=1, column=0, pady=40, padx=20, sticky="nsew")
        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_columnconfigure(1, weight=1)

        # Add username entry
        ctk.CTkLabel(self.form_frame, text="User Name", font=("Arial", 18)).grid(row=1, column=0, pady=6, padx=5, sticky="nsw")
        self.username_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="User Name",
            corner_radius=10,
            height=30,
        )
        self.username_entry.grid(row=2, column=0, pady=6, padx=5, sticky="nsew")

        # Add password entry
        ctk.CTkLabel(self.form_frame, text="Password", font=("Arial", 18)).grid(row=1, column=1, pady=6, padx=5, sticky="nsw")
        self.password_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Password",
            show="*",
            corner_radius=10,
            height=30,
        )
        self.password_entry.grid(row=2, column=1, pady=6, padx=5, sticky="nsew")

        # Add full name entry
        ctk.CTkLabel(self.form_frame, text="Full Name", font=("Arial", 18)).grid(row=3, column=0, pady=6, padx=5, sticky="nsw")
        self.full_name_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Full Name",
            corner_radius=10,
            height=30,
        )
        self.full_name_entry.grid(row=4, column=0, pady=6, padx=5, sticky="nsew")

        # Add contact number entry
        ctk.CTkLabel(self.form_frame, text="Contact Number", font=("Arial", 18)).grid(row=3, column=1, pady=6, padx=5, sticky="nsw")
        self.contact_number_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="Contact Number",
            corner_radius=10,
            height=30,
        )
        self.contact_number_entry.grid(row=4, column=1, pady=6, padx=5, sticky="nsew")

        # Add national ID entry
        ctk.CTkLabel(self.form_frame, text="National ID", font=("Arial", 18)).grid(row=5, column=0, pady=6, padx=5, sticky="nsw")
        self.national_id_entry = ctk.CTkEntry(
            self.form_frame,
            placeholder_text="National ID",
            corner_radius=10,
            height=30,
        )
        self.national_id_entry.grid(row=6, column=0, pady=6, padx=5, sticky="nsew")

        # Add user type combobox
        ctk.CTkLabel(self.form_frame, text="User Role", font=("Arial", 18)).grid(row=5, column=1, pady=6, padx=5, sticky="nsw")
        self.user_type_combobox = ctk.CTkComboBox(
            self.form_frame,
            values=["Guest", "Worker", "Employee"],
            corner_radius=10,
            height=30,
        )
        self.user_type_combobox.grid(row=6, column=1, pady=6, padx=5, sticky="nsew")

        # Add safety gears checkboxes
        ctk.CTkLabel(self.form_frame, text="Safety Gears", font=("Arial", 18)).grid(row=7, column=0, pady=6, padx=5, sticky="nsw")
        self.gear_vars = {}
        gears = ["Helmet", "Vest", "Goggles", "Gloves", "Boots"]
        for i, gear in enumerate(gears):
            self.gear_vars[gear] = ctk.StringVar(value="Disable")
            ctk.CTkCheckBox(
                self.form_frame,
                text=gear,
                variable=self.gear_vars[gear],
                onvalue="Active",
                offvalue="Disable",
            ).grid(row=8 + i, column=0, pady=5, padx=5, sticky="w")

        # Add back to admin dashboard button
        self.back_to_admin_dashboard_button = ctk.CTkButton(
            self.form_frame,
            text="Back to Dashboard",
            command=self.create_logout_frame_for_admin,
            width=120,
            fg_color="red",
            text_color="black",
            corner_radius=10,
            height=30,
        )
        self.back_to_admin_dashboard_button.grid(row=14, column=0, pady=6, padx=5, sticky="nsew")

        # Add add user button
        self.add_user_button = ctk.CTkButton(
            self.form_frame,
            text="Add User",
            command=self.add_user_by_admin,
            width=120,
            fg_color="yellow",
            text_color="black",
            corner_radius=10,
            height=30,
        )
        self.add_user_button.grid(row=14, column=1, pady=6, padx=5, sticky="nsew")

    def add_user_by_admin(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        full_name = self.full_name_entry.get()
        contact_number = self.contact_number_entry.get()
        national_id = self.national_id_entry.get()
        user_type = self.user_type_combobox.get()

        # Collect safety gear values
        is_helmet_check = self.gear_vars["Helmet"].get()
        is_vest_check = self.gear_vars["Vest"].get()
        is_goggles_check = self.gear_vars["Goggles"].get()
        is_gloves_check = self.gear_vars["Gloves"].get()
        is_boots_check = self.gear_vars["Boots"].get()

        if self.user_model.create_user_by_admin(
            username,
            password,
            full_name,
            contact_number,
            national_id,
            user_type,
            is_helmet_check,
            is_vest_check,
            is_goggles_check,
            is_gloves_check,
            is_boots_check,
        ):
            CustomMessageBox(self.app, "Success", "User added successfully.")
            self.create_logout_frame_for_admin()
        else:
            CustomMessageBox(self.app, "Error", "Failed to add user. Please try again.")

    # * ----------------------------------------------------------------
    # *             EMPLOYEE
    # * ----------------------------------------------------------------

    def create_logout_frame_for_employee(self):
        self.clear_frame()

        self.logout_frame = ctk.CTkFrame(self.app, fg_color="transparent")
        self.logout_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew")

        # Welcome label
        self.logout_label = ctk.CTkLabel(self.logout_frame, text=f"Welcome {self.username}", font=("Arial", 24))
        self.logout_label.grid(row=0, column=0, pady=12, padx=10, sticky="nsew")

        # Logout button
        self.logout_button = ctk.CTkButton(self.logout_frame, text="Logout", command=self.create_login_frame)
        self.logout_button.grid(row=1, column=0, pady=12, padx=10, sticky="ew")

        # Camera control button
        self.camera_button = ctk.CTkButton(self.logout_frame, text="Stop Camera", command=self.toggle_camera)
        self.camera_button.grid(row=2, column=0, pady=12, padx=10, sticky="ew")

        # Camera frame
        self.camera_frame = ctk.CTkFrame(self.logout_frame, width=800, height=600, corner_radius=15, fg_color="transparent")
        self.camera_frame.grid(row=3, column=0, pady=12, padx=10, sticky="nsew")

        # Add image label for displaying camera feed
        self.image_label = ctk.CTkLabel(self.camera_frame, text="", width=780, height=400, fg_color="black", corner_radius=15)
        self.image_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Add result label for displaying detection results
        self.result_label = ctk.CTkLabel(self.logout_frame, text="Gear Status:", font=("Arial", 18))
        self.result_label.grid(row=4, column=0, padx=10, pady=(10, 5), sticky="w")

        # Add missing gears label for displaying missing gear information
        self.missing_gears_label = ctk.CTkLabel(self.logout_frame, text="Missing Gears:", font=("Arial", 18))
        self.missing_gears_label.grid(row=5, column=0, padx=10, pady=(5, 10), sticky="w")

        user = self.user_model.get_user_by_username(self.username)
        self.gear_status_labels = {}
        self.gear_violation_check_status = {}

        if user.is_helmet_check.lower() == "active":
            self.gear_status_labels["Helmet"] = ctk.CTkLabel(self.result_label, text="Helmet: No", font=("Arial", 16), fg_color="red")
            self.gear_violation_check_status["helmet"] = False

        if user.is_vest_check.lower() == "active":
            self.gear_status_labels["Vest"] = ctk.CTkLabel(self.result_label, text="Vest: No", font=("Arial", 16), fg_color="red")
            self.gear_violation_check_status["vest"] = False

        if user.is_goggles_check.lower() == "active":
            self.gear_status_labels["Goggles"] = ctk.CTkLabel(self.result_label, text="Goggles: No", font=("Arial", 16), fg_color="red")
            self.gear_violation_check_status["goggles"] = False

        if user.is_gloves_check.lower() == "active":
            self.gear_status_labels["Gloves"] = ctk.CTkLabel(self.result_label, text="Gloves: No", font=("Arial", 16), fg_color="red")
            self.gear_violation_check_status["gloves"] = False

        if user.is_boots_check.lower() == "active":
            self.gear_status_labels["Boots"] = ctk.CTkLabel(self.result_label, text="Boots: No", font=("Arial", 16), fg_color="red")
            self.gear_violation_check_status["boots"] = False

        for i, (gear, label) in enumerate(self.gear_status_labels.items()):
            label.grid(row=i + 1, column=0, padx=10, pady=(5, 0), sticky="w")

    def toggle_camera(self):
        if self.camera_running:
            self.camera.stop_camera()
            self.camera_button.configure(text="Start Camera")
            self.update_violation_count()
            # self.create_login_frame()
        else:
            self.camera.start_camera()
            self.camera_button.configure(text="Stop Camera")
        self.camera_running = not self.camera_running

    def update_violation_count(self):
        user = self.user_model.get_user_by_username(self.username)

        missing_gears_count = 0
        for gear in self.gear_status_labels:
            gear_name = self.gear_status_labels[gear].cget("text").lower()
            proper_gear_name = gear_name.split(":")[0]

            if self.gear_status_labels[gear].cget("fg_color") == "red":
                missing_gears_count += 1
                if gear.lower() == "helmet":
                    user.helmet_voilation_count += 1
                    self.gear_violation_check_status[proper_gear_name] = False
                elif gear.lower() == "vest":
                    user.vest_voilation_count += 1
                    self.gear_violation_check_status[proper_gear_name] = False
                elif gear.lower() == "goggles":
                    user.goggles_Voilation_count += 1
                    self.gear_violation_check_status[proper_gear_name] = False
                elif gear.lower() == "gloves":
                    user.gloves_voilation_count += 1
                    self.gear_violation_check_status[proper_gear_name] = False
                elif gear.lower() == "boots":
                    user.boots_voilation_count += 1
                    self.gear_violation_check_status[proper_gear_name] = False

                user.total_violation_count += 1

            else:
                self.gear_violation_check_status[proper_gear_name] = True

        user.total_violation_count += 1

        # Update gear verification status
        user.is_helmet_verify = self.gear_violation_check_status["helmet"] if "helmet" in self.gear_violation_check_status else False
        user.is_vest_verify = self.gear_violation_check_status["vest"] if "vest" in self.gear_violation_check_status else False
        user.is_goggles_verify = self.gear_violation_check_status["goggles"] if "goggles" in self.gear_violation_check_status else False
        user.is_gloves_verify = self.gear_violation_check_status["gloves"] if "gloves" in self.gear_violation_check_status else False
        user.is_boots_verify = self.gear_violation_check_status["boots"] if "boots" in self.gear_violation_check_status else False

        self.user_model.update_user(user)

        found_gears_count = len(self.gear_status_labels) - missing_gears_count
        # CustomMessageBox(self.app, "Gear Detection Result", f"Gears Found: {found_gears_count}\nGears Missing: {missing_gears_count}")
        message_box = CustomMessageBox(self.app, "Gear Detection Result", f"Gears Found: {found_gears_count}\nGears Missing: {missing_gears_count}")
        message_box.bind("<Destroy>", lambda event: self.create_login_frame())
