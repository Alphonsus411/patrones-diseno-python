from abc import ABC, abstractmethod


class INotification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self, message):
        pass


class EmailNotification(INotification):
    def send(self, message):
        print(f"Sending email notification: {message}")


class PushNotification(INotification):
    def send(self, message):
        print(f"Sending push notification: {message}")


class SmsNotification(INotification):
    def send(self, message):
        print(f"Sending sms notification: {message}")


class EmailNotificationFactory(NotificationFactory):
    def create_notification(self):
        return EmailNotification()

class PushNotificationFactory(NotificationFactory):
    def create_notification(self):
        return PushNotification()

class SmsNotificationFactory(NotificationFactory):
    def create_notification(self):
        return SmsNotification()


factory = EmailNotificationFactory()
notification = factory.create_notification()
notification.send("This is an email message!")

factory = PushNotificationFactory()
notification = factory.create_notification()
notification.send("This is an push message!")

factory = SmsNotificationFactory()
notification = factory.create_notification()
notification.send("This is an sms message!")

