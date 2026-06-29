

class EmailNotification:
    def send(self, message):
        print(f"Sending email notification: {message}")


class PushNotification:
    def send(self, message):
        print(f"Sending push notification: {message}")


class SmsNotification:
    def send(self, message):
        print(f"Sending sms notification: {message}")


class EmailNotificationFactory:
    def create_notification(self):
        return EmailNotification()

class PushNotificationFactory:
    def create_notification(self):
        return PushNotification()

class SmsNotificationFactory:
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