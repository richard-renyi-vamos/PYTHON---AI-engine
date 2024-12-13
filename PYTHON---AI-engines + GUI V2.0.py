import tkinter as tk
from tkinter import ttk

# Define a list of popular AI engines with their features and use cases
ai_engines = [
    {"name": "OpenAI GPT", "features": "Natural Language Processing, Chatbots, Code Generation", "use_case": "General AI"},
    {"name": "Google DeepMind", "features": "Reinforcement Learning, Healthcare Solutions", "use_case": "Specialized AI"},
    {"name": "IBM Watson", "features": "Data Analysis, NLP, Business Insights", "use_case": "Enterprise AI"},
    {"name": "Microsoft Azure AI", "features": "Cloud AI, Vision, Speech, NLP", "use_case": "Scalable Cloud Solutions"},
    {"name": "Amazon SageMaker", "features": "Machine Learning Model Deployment", "use_case": "Cloud-based ML"},
    {"name": "Hugging Face Transformers", "features": "NLP Models, Open Source", "use_case": "Language-focused AI"},
    {"name": "OpenCV", "features": "Image and Video Processing", "use_case": "Computer Vision"},
    {"name": "TensorFlow", "features": "Deep Learning, ML Framework", "use_case": "Flexible AI Development"},
    {"name": "PyTorch", "features": "Deep Learning, Research", "use_case": "Custom AI Solutions"},
    {"name": "Stable Diffusion", "features": "Image Generation, Artistic AI", "use_case": "Creative AI"}
]

# Function to display the AI engines in a GUI
def display_top_ai_engines_gui():
    # Create the main application window
    root = tk.Tk()
    root.title("Top 10 AI Engines")

    # Create a Treeview widget to display the AI engines
    tree = ttk.Treeview(root, columns=("Features", "Use Case"), show="headings")
    tree.heading("#1", text="Name")
    tree.heading("#2", text="Features")
    tree.heading("#3", text="Use Case")
    tree.column("#1", anchor="w")
    tree.column("#2", anchor="w")
    tree.column("#3", anchor="w")

    # Insert AI engines into the Treeview
    for engine in ai_engines:
        tree.insert("", "end", values=(engine["name"], engine["features"], engine["use_case"]))

    # Pack the Treeview widget
    tree.pack(fill="both", expand=True)

    # Start the main event loop
    root.mainloop()

# Run the GUI application
display_top_ai_engines_gui()
