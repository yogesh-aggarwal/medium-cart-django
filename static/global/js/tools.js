let data;

convertCurrency = (_base = "inr", _target = "usd", _amount = 0) => {
  fetch(
    `https://free.currconv.com/api/v7/convert?q=${_base}_${_target}&compact=ultra&apiKey=09cd7709b9a23624774b`
    )
    .then(response => {
      return response.text();
    })
    .then(data => {
      localStorage.setItem("rate", JSON.parse(data)[`${_base.toUpperCase()}_${_target.toUpperCase()}`])
    });
  return true
};

setupStorage = () => {};
