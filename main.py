import customtkinter as ctk

from model_and_methods.user_method import UserMethod
from ui_pages.signup_login_ui import UI

# Set GUI theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self, user_model):
        super().__init__()
        self.geometry("800x600")
        self.title("User Management and Safety Gear Detection")

        self.user_model = user_model
        self.ui = UI(self, self.user_model)
        self.ui.create_login_frame()


if __name__ == "__main__":
    user_model = UserMethod()
    app = App(user_model)
    app.mainloop()
    user_model.close()
