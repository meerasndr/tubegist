document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const urlInput = document.getElementById('urlInput').value;
    const resultDiv = document.getElementById('result');

    fetch(`http://0.0.0.0:8000/video_url/?url=${urlInput}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: urlInput })
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        console.log(data.message)
        resultDiv.innerHTML = "<b>Here is the gist of the video:</b> <br>" + data.message;
    })
    .catch(function(error) {
        console.error('Error:', error);
        resultDiv.textContent = "Server Error. Try again later!"
    });
});


document.getElementById('myForm').addEventListener('reset', function(event){
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';
});