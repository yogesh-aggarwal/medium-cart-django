let data;

fetch(`https://api.exchangeratesapi.io/latest`)
  .then(response => {
    return response.text();
  })
  .then(data => {
    localStorage.setItem("currencyRates", data);
  });

convertCurrency = _target = {
  return: localStorage.getItem("currencyRates")
};
