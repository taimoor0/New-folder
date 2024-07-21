from PIL import Image, ImageTk
from ultralytics import YOLO
import customtkinter as ctk
import cv2


class Camera:
    def __init__(self, app, ui):
        self.app = app
        self.ui = ui
        self.camera_running = False
        self.model = self.load_model()

    def load_model(self):
        model_path = "./text.pt"
        model = YOLO(model_path)
        return model

    def start_camera(self):
        self.camera_running = True
        self.capture = cv2.VideoCapture(0)
        self.update_frame()

    def stop_camera(self):
        self.camera_running = False
        if hasattr(self, "capture") and self.capture.isOpened():
            self.capture.release()

    def update_frame(self):
        if not self.camera_running:
            return

        ret, frame = self.capture.read()
        if ret:
            results = self.model(frame)
            annotated_frame = results[0].plot()

            frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)

            # Configure or update the image_label
            if not hasattr(self.ui, "image_label") or not isinstance(self.ui.image_label, ctk.CTkLabel):
                self.ui.image_label = ctk.CTkLabel(self.ui.camera_frame, image=imgtk)
                self.ui.image_label.grid(row=0, column=0, padx=10, pady=10)
            else:
                self.ui.image_label.configure(image=imgtk)

            self.ui.image_label.imgtk = imgtk

            gear_status = {gear: False for gear in self.ui.gear_status_labels}

            for result in results[0].boxes:
                cls = result.cls
                cls_name = self.model.names[int(cls)]
                if cls_name in gear_status:
                    gear_status[cls_name] = True

            for gear, status in gear_status.items():
                if gear in self.ui.gear_status_labels:
                    self.ui.gear_status_labels[gear].configure(text=f"{gear}: {'Yes' if status else 'No'}", fg_color="orange" if status else "red")

            # Update missing gears label
            missing_gears = [gear for gear, status in gear_status.items() if not status]
            if len(missing_gears):
                self.ui.missing_gears_label.configure(text=f"Missing Gears: {', '.join(missing_gears)}")
            else:
                self.ui.missing_gears_label.configure(text="No Missing Gears Detected")

        if self.camera_running:
            self.app.after(10, self.update_frame)
