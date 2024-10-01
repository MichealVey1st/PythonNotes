# PythonNotes
 
Hello! Welcome to my notes taking application! Sometimes I found it hard to take notes during class so I decided to find a different way. By taking advatage of AI of course! So in order to use this you must understand how this works. 

## Usage

Begin by copying the repo to your local machine. In the folder you copied this repo to create a folder called "notes". This folder will be where the resulting files are stored including the transcript and audio files. To use this first you must run the __speach-to-text.py__ file. This file will initialize the recording software. You must press the **ESC** key when you are ready to start recording. Once finished press **ESC** again to end the recording. At this time whisper from openai will then transcribe the audio to a text file.

After you have gotten the text file you want to plug in the file to GPT or some other AI solution and give this prompt or something similar. Then take your new notes and use them well!

```
Alright. I need you to take a step back. Think deeply. I will be giving you some text, I want you to go through it and take notes entirely in Markdown format. I want these to be divided into sections as you see fit. Each section should include at LEAST the following but you are welcome to add more as needed. First should be a long summary of the section with details so that I can understand it. This will generally be around 3-4 paragraphs but can be shorter depending on the sections size. Second, I want a list of main points from the section to highlight the key points of the section. This should ideally be at least 5 items. Third, I want a couple important quotes. This should ideally be a smaller number however exceptions can be made if the quotes are really important. Then Fourth, I want questions that could be best asked to further understand the text. Again please ensure that this is done ENTIRELY done in MD format to ensure that when plugged into obsidian it will function properly.
```