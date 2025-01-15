from models.project import Project
from utils.file_manager import save_project, load_project

project = Project("My Novel", "Fantasy")

def add_chapter(title):
    chapter = {"title": title, "content": ""}
    project.chapters.append(chapter)
    save_project(project, "data/my_novel.json")