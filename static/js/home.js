document.getElementById('analyzeBtn').addEventListener('click', function () {
  const stocks = document.querySelector('input[name="stockName"]').value;
  const budget = document.querySelector("input[name='budget'").value;
  if (budget != '' && stocks != '') {
    // Show loading state immediately
    document.querySelector('.output').innerHTML = '<span>Loading...</span>';

    fetch('/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ stocks: stocks, budgets: budget }),
    })
      .then((response) => response.json())
      .then((data) => {
        document.querySelector('.output').innerHTML = data.result;
      })
      .catch((error) => {
        document.querySelector('.output').innerHTML =
          'An error occurred while fetching the response.';
      });
  } else {
    alert('Please enter a budget or a stock');
  }
});

document.getElementById('trendingBtn').addEventListener('click', function () {
  // Show loading state immediately
  document.querySelector('.output').innerHTML = '<span>Loading...</span>';

  fetch('/trending')
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('.output').innerHTML = data.result;
    })
    .catch((error) => {
      document.querySelector('.output').innerHTML =
        'An error occurred while fetching the response.';
    });
});
