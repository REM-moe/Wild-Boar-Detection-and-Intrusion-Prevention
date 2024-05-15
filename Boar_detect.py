from ultralytics import YOLO
import os

class WildBoarDetect:

    def detect(self):
        model = YOLO('3000_20.pt')  # or model = YOLO('3000_45.pt') for your custom model

        # Path to the black.jpg file
        black_image_path = "black.jpg"

        try:
            # Predict with the model
            results = model.predict(source="received_images/photo.jpg", show=False, save=False)
        except FileNotFoundError:
            # Load the black image
            results = model.predict(source=black_image_path, show=False, save=False)

        for result in results:
            if result.boxes:
                for box in result.boxes:
                    class_id = int(box.cls)
                    object_name = model.names[class_id]
                    if object_name == 'wild_boar':

                        return True
                    else:

                        return False
