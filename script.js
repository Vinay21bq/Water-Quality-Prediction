document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const values = {};
    formData.forEach((value, key) => {
        values[key] = parseFloat(value);
    });

    // Send form data to the backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(values)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictionText').innerText = `Prediction: ${data.prediction}`;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error predicting the water quality');
    });
});
