##News Summarizer

Small test project using OpenAI free trial.
Summarizer scapres the italian news site ```https://ansa.it/``` for the most recent news, feeds them to the ChatGPT 3.5 turbo model and produces a translated and summarized version of them, saving them to the ```translated_articles.txt``` file.

Additionally, a non-translated version is available in the ```articles.txt``` file.

###How to use

set your OpenAI API key as an environment variable using:

```bash
setx OPENAI_API_KEY <key_value>
```

I'm relying on a free OpenAI plan, so the output will be truncated depending on the maximum request rate allowed. 
