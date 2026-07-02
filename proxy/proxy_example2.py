from abc import ABC, abstractmethod


class ISecurityCamera:
    @abstractmethod
    def display_live_feed(self):
        pass


class SecurityCamera(ISecurityCamera):
    def __init__(self, camera_location):
        self._camera_location = camera_location

    def display_live_feed(self):
        print(f"Displaying live feed from the {self._camera_location} camera.")



class SecurityCameraProxy(ISecurityCamera):
    def __init__(self, camera_location, has_access):
        self._security_camera = SecurityCamera(camera_location)
        self._has_access = has_access

    def display_live_feed(self):
        if not self._has_access:
            print(f"No access. You do not have permission to view this camera.")

        else:
            self._security_camera.display_live_feed()


bedroom_camera = SecurityCameraProxy("bedroom", False)
bedroom_camera.display_live_feed()

living_room_camera = SecurityCameraProxy("living_room", True)
living_room_camera.display_live_feed()



