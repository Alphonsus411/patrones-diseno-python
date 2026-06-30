

class EnglishSpeaker:
    def ask(self, question):
        return f"Question in English: {question}"

    def reply(self, answer):
        return f"Answer in English: {answer}"


class SpanishSpeaker:
    def pregunta(self, question):
        return f"Pregunta en español: {question}"

    def reply(self, answer):
        return f"Respuesta en español: {answer}"


class Translator:
    def __init__(self, spanish_speaker):
        self._spanish_speaker = spanish_speaker

    def ask(self, question):
        return self._spanish_speaker.pregunta(question)

    def reply(self, answer):
        return self._spanish_speaker.reply(answer)

class CommunicationSystem:
    def start_conversation(self, communicator, question, answer):
        print(communicator.ask(question))
        print(communicator.reply(answer))


communication_system = CommunicationSystem()
english_speaker = EnglishSpeaker()
communication_system.start_conversation(english_speaker, "How are you?", "I´m fine, thanks")

spanish_speaker = SpanishSpeaker()
translator = Translator(spanish_speaker)
communication_system.start_conversation(translator, "Cómo estás?", "Estoy bien, gracias")
