class Project:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.chapter = []

    def add_chapter(self, chapter):
        self.chapter.append(chapter)