# tubegist

Summarizes YouTube videos based on YouTube generated transcripts and OpenAI's GPT API.

### Example:
Summarizing [Steve Jobs' Stanford commencement speech](https://www.youtube.com/watch?v=UF8uR6Z6KLc) here:

`python3 main.py https://www.youtube.com/watch?v=UF8uR6Z6KLc`

One output:
```
Steve Jobs' 2005 Stanford Commencement Address focused on three topics: connecting the dots, love and loss, and death. 
He encouraged the graduates to trust in something, to find what they love, and to remember that they will die soon to 
avoid the trap of thinking they have something to lose. He concluded with the message to stay hungry and stay foolish.
```

Here's another one:
```
Steve Jobs' 2005 Stanford Commencement Address was about connecting the dots, finding love and loss, and accepting death. 
He discussed the importance of following your heart, even when it leads you off the well-worn path, and how getting fired 
from Apple was the best thing that had ever happened to him. He also urged the audience to live each day
as if it were their last, and to never settle for anything less than what they love.
Finally, he encouraged them to stay hungry and stay foolish.
```

### WIP:
1. Longer videos with more tokens
	- Possible solutions: use a tokenizer based workaround for multiple calls or try using GPT-4 APIs)
2. Non-English videos
