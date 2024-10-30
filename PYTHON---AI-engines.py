import tkinter as tk
import webbrowser

# List of AI engines and their URLs
ai_engines = [
    ("OpenAI (ChatGPT, Codex)", "https://openai.com"),
    ("Google Bard", "https://bard.google.com"),
    ("Microsoft Azure AI", "https://azure.microsoft.com/en-us/services/cognitive-services/"),
    ("IBM Watson", "https://www.ibm.com/watson"),
    ("Hugging Face", "https://huggingface.co"),
    ("Amazon SageMaker", "https://aws.amazon.com/sagemaker/"),
    ("DataRobot", "https://www.datarobot.com"),
    ("H2O.ai", "https://www.h2o.ai"),
    ("DeepMind", "https://deepmind.com"),
    ("Anthropic", "https://www.anthropic.com"),
    ("Cerebras", "https://www.cerebras.net"),
    ("C3.ai", "https://c3.ai"),
    ("Clarifai", "https://www.clarifai.com"),
    ("Graphcore", "https://www.graphcore.ai"),
    ("UiPath AI Center", "https://www.uipath.com"),
    ("Fritz AI", "https://fritz.ai"),
    ("SAS Viya", "https://www.sas.com"),
    ("Salesforce Einstein", "https://www.salesforce.com/products/einstein/overview/"),
    ("RunwayML", "https://runwayml.com"),
    ("Seldon", "https://www.seldon.io"),
    ("Paperspace Gradient", "https://www.paperspace.com"),
    ("Spell", "https://www.spell.ml"),
    ("Veritone", "https://www.veritone.com"),
    ("KAI", "https://kasisto.com"),
    ("Petuum", "https://www.petuum.com"),
    ("Olive AI", "https://oliveai.com"),
    ("AI21 Labs", "https://www.ai21.com"),
    ("NVIDIA AI", "https://www.nvidia.com/en-us/ai-data-science/"),
    ("BigML", "https://bigml.com"),
    ("Abacus.AI", "https://abacus.ai"),
    ("Ayasdi", "https://www.ayasdi.com"),
    ("Darktrace", "https://www.darktrace.com"),
    ("Vectra AI", "https://www.vectra.ai"),
    ("Sentient.io", "https://sentient.io"),
    ("Suki AI", "https://www.suki.ai"),
    ("BioMind", "https://www.biomind.ai"),
    ("Zebra Medical Vision", "https://www.zebra-med.com"),
    ("PathAI", "https://www.pathai.com"),
    ("Tempus", "https://www.tempus.com"),
    ("Babylon Health", "https://www.babylonhealth.com"),
    ("Peltarion", "https://peltarion.com"),
    ("Lobe.ai", "https://lobe.ai"),
    ("Orbital Insight", "https://orbitalinsight.com"),
    ("Vicarious", "https://www.vicarious.com"),
    ("HawkEye 360", "https://www.he360.com"),
    ("Arize AI", "https://arize.com"),
    ("Sigma Computing", "https://www.sigmacomputing.com"),
    ("DotData", "https://www.dotdata.com"),
    ("GrokStyle", "https://www.grokstyle.com"),
    ("Intello Labs", "https://intellolabs.com"),
    ("Onfido", "https://onfido.com"),
    ("Behavox", "https://www.behavox.com")
]

# Function to open the URL in the browser
def open_url(url):
    webbrowser.open(url)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Popular AI Engines")
root.geometry("500x700")

# Create a frame to contain the list
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

# Label
header = tk.Label(frame, text="Top 50 AI Engines", font=("Arial", 16))
header.pack()

# Loop through the list of AI engines to create buttons
for engine_name, url in ai_engines:
    button = tk.Button(
        frame, text=engine_name, font=("Arial", 12), fg="blue", cursor="hand2",
        command=lambda url=url: open_url(url)
    )
    button.pack(anchor="w", pady=2)

# Run the application
root.mainloop()
