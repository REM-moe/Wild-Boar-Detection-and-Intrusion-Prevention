import requests
import os

# Directory to save received images
save_dir = "received_images"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

class ESP_CAM:
    def __init__(self, cam_ip) -> None:
        self.ip_address = cam_ip

    def is_server_reachable(self):
        try:
            response = requests.get(f"http://{self.ip_address}/")
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def capture_photo(self):
        try:
            if not self.is_server_reachable():
                print("Server is not reachable.")
                return None

            # Send command to capture photo
            response = requests.get(f"http://{self.ip_address}/capture")
            if response.status_code != 200:
                print("Failed to capture photo.")
                return None
            else:
                response = requests.get(f"http://{self.ip_address}/saved-photo")
                if response.status_code == 200:
                    # Save the received image
                    with open(os.path.join(save_dir, "photo.jpg"), "wb") as f:
                        f.write(response.content)
                        print("Photo saved successfully")
                        return os.path.join(save_dir, "photo.jpg")
        except Exception as e:
            print("Exception occurred:", e)
            return None
    
    def toggle_pin_on(self):
        try:
            response = requests.get(f"http://{self.ip_address}/toggle-pin-on")
            if response.status_code == 200:
                print("Pin toggled ON successfully.")
            else:
                print("Failed to toggle pin ON.")
        except requests.exceptions.RequestException as e:
            print("Error toggling pin ON:", e)

    def toggle_pin_off(self):
        try:
            response = requests.get(f"http://{self.ip_address}/toggle-pin-off")
            if response.status_code == 200:
                print("Pin toggled OFF successfully.")
            else:
                print("Failed to toggle pin OFF.")
        except requests.exceptions.RequestException as e:
            print("Error toggling pin OFF:", e)
