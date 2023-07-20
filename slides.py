class Slide:
    def __init__(self, slide_type, title, content, configuration=None):
        self.slide_type = slide_type
        self.title = title
        self.content = content
        self.configuration = configuration