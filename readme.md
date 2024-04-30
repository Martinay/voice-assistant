To run the script, simply execute the main.py file. The script will listen to the microphone, convert the spoken words to text using the Google Speech-to-Text API, and respond accordingly based on the user's input. The assistant will greet the user with "Hello, how can I help you?" if the user says "Hello Itero", and provide a weather forecast if the user asks "What is the weather today?". If the user says something else, the assistant will respond with "I'm sorry, I didn't understand that.". The script uses the SpeechRecognition library to capture audio from the microphone and the pyttsx3 library to convert text to speech for the assistant's responses.

install pyhton dependencies with
pip install -r requirements.txt
