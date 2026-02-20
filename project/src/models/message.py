class Message:
    def __init__(self, role: str, message: str):
        self.role = role
        self.message = message

    def make_buffer(self) -> dict:
        return {
            'role': self.role,
            'message': self.message
        }