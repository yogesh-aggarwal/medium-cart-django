let data;

/*
fetch(
  `https://api.currconv.com/api/v7/convert?q=USD_PHP,PHP_USD&compact=ultra&apiKey=YOUR_API_KEY`
)
  .then(response => {
    return response.text();
  })
  .then(data => {
    localStorage.setItem("currencyRates", data);
  });
*/

convertCurrency = (_target="usd") => {
  return JSON.parse(localStorage.getItem("currencyRates"));
};


setupStorage = () => {}
