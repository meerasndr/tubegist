document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const urlInput = document.getElementById('urlInput').value;

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
        const resultDiv = document.getElementById('result');
        console.log(data.message)
        resultDiv.textContent = 'Result: ' + data.message;
    })
    .catch(function(error) {
        console.error('Error:', error);
    });
});


document.getElementById('myForm').addEventListener('reset', function(event){
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';
});