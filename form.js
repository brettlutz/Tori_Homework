let selectPopulate = document.getElementById("productSelect");
if (selectPopulate) {
  // Check if this exists because if not you get an error
  const products = [
    {
      id: "fc-1888",
      name: "flux capacitor",
      averagerating: 4.5,
    },
    {
      id: "fc-2050",
      name: "power laces",
      averagerating: 4.7,
    },
    {
      id: "fs-1987",
      name: "time circuits",
      averagerating: 3.5,
    },
    {
      id: "ac-2000",
      name: "low voltage reactor",
      averagerating: 3.9,
    },
    {
      id: "jj-1969",
      name: "warp equalizer",
      averagerating: 5.0,
    },
  ];

  products.forEach((product) => {
    let option = document.createElement("option");
    option.text = product.name;
    option.value = product.id;

    option.setAttribute("data-rating", product.averagerating);
    if (selectPopulate) {
      selectPopulate.appendChild(option);
    }
  });

  selectPopulate.onchange = function () {
    const selectedOption = selectPopulate.options[selectPopulate.selectedIndex];
    const selectedRating = selectedOption.getAttribute("data-rating");
    const selectedId = selectedOption.value;
    const selectedName = selectedOption.text;

    console.log(
      `Selected: ${selectedName}, ID: ${selectedId}, Rating: ${selectedRating}`
    );
  };
} // if end

document.addEventListener("DOMContentLoaded", () => {
  const reviewForm = document.getElementById("reviewForm");
  const reviewInput = document.getElementById("review");
  const clickSpan = document.querySelector(".clicks"); // add a variable for the span.click

  if (reviewForm) {
    // check if the reviewForm exists before setting event listener to prevent error
    reviewForm.addEventListener("submit", (event) => {
      event.preventDefault();

      const reviewText = reviewInput.value.trim();

      if (reviewText) {
        let numReviews = parseInt(localStorage.getItem("numReviews-ls")) || 0;
        numReviews++;
        localStorage.setItem("numReviews-ls", numReviews); // you have to pass the value in you want to write to localstorage

        window.location.href = "review.html";
      } else {
        alert("please enter a review. ");
      }
    });
  }

  if (clickSpan) {
    // check if the span exists, and if so read localstorage and write it to the innerHTML
    // you also need to add style for this span because the color is black and you won't see the
    // number if you don't add css
    const reviews = parseInt(
      JSON.parse(localStorage.getItem("numReviews-ls")),
      10
    );
    clickSpan.innerHTML = reviews;
  }
});
