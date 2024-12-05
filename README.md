# PythonNotes
 
Hello! Welcome to my notes taking application! Sometimes I found it hard to take notes during class so I decided to find a different way. By taking advatage of AI of course! So in order to use this you must understand how this works. 

## Usage

Begin by copying the repo to your local machine. In the folder you copied this repo to create a folder called "notes". This folder will be where the resulting files are stored including the transcript and audio files. To use this first you must run the __speach-to-text.py__ file. This file will initialize the recording software. You must press the **ESC** key when you are ready to start recording. Once finished press **ESC** again to end the recording. At this time whisper from openai will then transcribe the audio to a text file.

After you have gotten the text file you want to plug in the file to GPT or some other AI solution and give this prompt or something similar. Then take your new notes and use them well!

```
Take a step back. Think deeply. I need you to carefully analyze the text I provide and take comprehensive notes in Markdown format, designed for use in Obsidian. Your notes should be structured as follows:  

1. **Overall Summary Section:**  
   - **Title:** Start with an overarching title for the entire document that captures the main topic or theme.  
   - **Summary:** Write an introductory paragraph that provides a high-level summary of the text. Include a brief overview of what the subsequent sections will detail.  

2. **Section Titles and Notes:** For each section in the text:  
   - **Title:** Provide a clear, concise title that reflects the content of the section.  
   - **Detailed Summary:** Write a long-form summary (3-4 paragraphs, or shorter if the section is brief) that captures the essential details and provides standalone understanding.  
   - **Key Points:** Create a concise bullet-point list of the main ideas or takeaways from the section, ideally 5 or more points.  
   - **Notable Quotes (Optional):** If you include quotes, they **must be used exactly as they appear in the transcription** without any alteration or paraphrasing. Use proper Markdown blockquote formatting and clearly associate the quote with its section (e.g., *“Quote from Section Title”*).  
   - **Questions for Understanding:** Formulate thoughtful questions that could help further explore or clarify the section's content.  

3. **Formatting Requirements:** Ensure the output is entirely in Markdown format, making proper use of headings for the overall summary, section titles, and notes. Use bullet points for key points and blockquotes for quotes. Structure the notes to allow for easy navigation in Obsidian.

```