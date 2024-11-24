## Scrape the Web using LLMs.....

This is an AI web scraper that uses LLM to scrape the desired data given the instructions of the user in the prompt as well as the url of the website to be scraped

Tech stack-
ollama for running LLMs locally , brightdata ( virtual  browser to bypass captchas, proxy blocking etc etc...), selenium and other libraries.


Running instructions:

1. Download Ollama
2. Using 'Ollama pull' download your preferred LLM
3. Get the API key by signing up on brightdata (for a virtual scraping browser), this is enable us to navigate around captcha and proxy blocking
4. Run the app using 'streamlit run main.py'


UI interface and running example to the get the data about properties and their rent, scraped from a property listing website:-

![Query space](<images/Screenshot from 2024-11-24 19-20-34.png>)

![Answer space](<images/Screenshot from 2024-11-24 19-21-12.png>)
