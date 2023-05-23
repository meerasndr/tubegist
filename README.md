# tubegist

Summarizes YouTube videos based on YouTube generated transcripts and OpenAI's GPT API.

### Example:
Summarizing [Steve Jobs' Stanford commencement speech](https://www.youtube.com/watch?v=UF8uR6Z6KLc) here:
`python3 main.py https://www.youtube.com/watch?v=UF8uR6Z6KLc`

One possible output:
```
Steve Jobs' 2005 Stanford Commencement Address focused on three topics: connecting the dots, love and loss, and death. He encouraged the graduates to trust in something, to find what they love, and to remember that they will die soon to avoid the trap of thinking they have something to lose. He concluded with the message to stay hungry and stay foolish.
```

WIP:
1. Longer videos with more tokens (Possible solutions: 1. use a tokenizer based workaround for multiple calls or 2. try using GPT-4 APIs)
2. Non-English videos
