Novel Writing App

The Novel Writing App is a Python-based desktop application designed to support novelists in organizing and tracking their writing projects. This MVP focuses on providing core features such as chapter management, text editing, and project saving/loading.

Features

Project Creation: Start a new writing project by specifying a title and genre.

Chapter Management: Add, view, and edit chapters in your novel.

Text Editor: Write and save content for each chapter.

Word Count Tracking: View word counts for individual chapters and the entire project.

Save and Load Projects: Store projects locally in JSON format for easy retrieval.

Simple GUI: User-friendly interface built with Tkinter.

Requirements

Python 3.7+

Dependencies:

tkinter (bundled with most Python installations)

Installation

Clone the repository:

git clone https://github.com/your-username/novelist-app.git
cd novelist-app

(Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install tkinter

Usage

Run the application:

python main.py

Use the menu to:

Create a new project

Add chapters

Write and edit chapter content

Save or load projects

File Structure

novelist_app/
├── main.py          # Main application entry point
├── models/          # Data models (e.g., Project, Chapter)
├── views/           # GUI-related code
├── controllers/     # Logic connecting models and views
├── data/            # Folder to store saved projects
├── utils/           # Utility functions (e.g., file management)
└── README.md        # Project documentation

Future Enhancements

Advanced Editing: Text formatting and style suggestions.

World-Building Tools: Timelines, maps, and character profiles.

Cloud Sync: Backup and access projects online.

Export Options: Save as PDF, EPUB, or DOCX.

Contribution

Contributions are welcome! Feel free to fork the repository and submit pull requests.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For questions or suggestions, please contact:
