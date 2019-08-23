buyNow = _id => {
  localStorage.setItem("productId", _id);
  location.href = "/checkout";
};
