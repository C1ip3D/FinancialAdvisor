document.getElementById('analyzeBtn').addEventListener('click', function() {
    const stocks = document.querySelector('input[name="stockName"]').value;
    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({stocks: stocks})
    })
    .then(response => response.json())
    .then(data => {
        document.querySelector('.output').innerHTML = data.result;
    });
});

document.getElementById('trendingBtn').addEventListener('click', function() {
    fetch('/trending')
    .then(response => response.json())
    .then(data => {
        document.querySelector('.output').innerHTML = data.result;
    });
});