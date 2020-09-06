
class YVideo:
    def __init__(self, title, id, channel=None):
        self.title = title
        self.id = id
        self.channel = channel
        self.url = f'https://www.youtube.com/watch?v={self.id}'

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.title} {self.url}'

    def __eq__(self, other):
        return self.id == other.id