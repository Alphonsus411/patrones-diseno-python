

class PayPalGateway:
    def process_payment(self, amount):
        print(f"Processing payment of {amount} with PayPal")
        return True


class PayPalTransactionLogger:
   def log_transaction(self, message):
       print(f"Registering transaction in PayPal {message}")


class StripeGateway:
    def process_payment(self, amount):
        print(f"Processing payment of {amount} with Stripe")
        return True


class StripeTransactionLogger:
    def log_transaction(self, message):
        print(f"Registering transaction in Stripe {message}")


class PayPalGatewayFactory:
    def create_payment_gateway(self):
        return PayPalGateway()

    def create_transaction_logger(self):
        return PayPalTransactionLogger()


class StripeGatewayFactory:
    def create_payment_gateway(self):
        return StripeGateway()

    def create_transaction_logger(self):
        return StripeTransactionLogger()


class PaymentService:
    def __init__(self, payment_gateway_factory):
        self.payment_gateway = payment_gateway_factory.create_payment_gateway()
        self.transaction_logger = payment_gateway_factory.create_transaction_logger()

    def process_payment(self, amount):
        if self.payment_gateway.process_payment(amount):
            self.transaction_logger.log_transaction(f"Payment of {amount} was successful")
        else:
            self.transaction_logger.log_transaction(f"Payment of {amount} was failed")


payment_gateway_factory = PayPalGatewayFactory()
payment_service = PaymentService(payment_gateway_factory)

amount = 100
payment_service.process_payment(amount)


another_payment_gateway_factory = StripeGatewayFactory()
another_payment_service = PaymentService(another_payment_gateway_factory)

another_payment_service.process_payment(amount)