import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties before adding anything to speak
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)   # Volume 0-1

# Get the list of voices and set to a male voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index for male/female voice

# Create audio files
engine.save_to_file("Please drink coffee.", "please_drink_coffee.mp3")
engine.save_to_file("Please wake up.", "please_wake_up.mp3")

# Run the speech engine
engine.runAndWait()

print("Audio files created successfully.")
