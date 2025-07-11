const clickMe = document.getElementById("column");
clickMe.addEventListener("click", () => {
  const businesses = document.getElementById("cards");
  businesses.classList.toggle("flex-direction-column");
});

const url =
  "https://raw.githubusercontent.com/ToriLutz/wdd231/main/chamber/scripts/data/members.json";
const cards = document.getElementById("cards");

async function getBusinessData() {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    displayBusinesses(data); // assuming data is an array
  } catch (error) {
    console.error("Error fetching data:", error);
    cards.innerHTML = "<p>Failed to load business data.</p>";
  }
}

getBusinessData();

const displayBusinesses = (businesses) => {
  businesses.forEach((business) => {
    const card = document.createElement("div");
    card.classList.add("business-card", "padding-none");

    const businessCardHeader = document.createElement("div");
    businessCardHeader.classList.add("business-card-header", "width-100");

    const name = document.createElement("h3");
    name.textContent = business.name;
    name.classList.add("margin-bottom-3", "padding-bottom-0");

    const membership = document.createElement("p");
    membership.textContent = `Membership Level: ${business.membership_level}`;
    membership.classList.add("margin-y-2");

    const industry = document.createElement("p");
    industry.textContent = `Industry: ${business.industry}`;
    industry.classList.add("margin-y-2");

    const businessCardBody = document.createElement("div");
    businessCardBody.classList.add("business-card-body");

    const businessAddressContainer = document.createElement("div");

    const address = document.createElement("p");
    address.textContent = `Address: ${business.address}`;

    const phoneNumber = document.createElement("p");
    phoneNumber.textContent = `Phone: ${business.phone_number}`;
    phoneNumber.classList.add("small-margin-bottom", "large-top-margin");
    phoneNumber.classList.remove("big-top-margin");

    const websiteLink = document.createElement("a");
    websiteLink.href = business.website_url;
    websiteLink.textContent = business.website_url;
    websiteLink.target = "_blank";

    const email = document.createElement("p");
    email.textContent = `Email: ${business.contact_email}`;

    const imageurl = document.createElement("img");
    imageurl.setAttribute("src", business.image_file);
    imageurl.setAttribute("alt", `Image of ${business.name}`);
    imageurl.setAttribute("loading", "lazy");
    imageurl.setAttribute("width", "150");
    imageurl.setAttribute("height", "150");

    card.appendChild(businessCardHeader);
    card.appendChild(businessCardBody);
    businessCardHeader.appendChild(name);
    businessCardHeader.appendChild(membership);
    businessCardHeader.appendChild(industry);

    businessCardBody.appendChild(imageurl);
    businessCardBody.appendChild(businessAddressContainer);
    businessAddressContainer.appendChild(address);
    businessAddressContainer.appendChild(phoneNumber);
    businessAddressContainer.appendChild(websiteLink);
    businessAddressContainer.appendChild(email);

    cards.appendChild(card);
  });
};

// commented out classes here. To use flex need to add flex-direction: row to .bussinesses class in styles.css
// .business-card {
//   display: flex;
//   flex-direction: column;
//   border: 1px solid black;
//   margin: 3px;
//   width: 25%;
// }

// .business-card-header {
//   text-align: center;
//   border-bottom: 1px solid;
// }

// .business-card-body {
//   display: flex;
//   flex-direction: row;
//   padding: 4px;
//   justify-content: space-between;
// }

// .text-center {
//   text-align: center;
// }

// .margin-bottom-3 {
//   margin-bottom: 3px;
// }

// .padding-bottom-0 {
//   padding-bottom: 0;
// }

// .padding-none {
//   padding: 0 !important;
// }

// .margin-y-2 {
//   margin-top: 2px;
//   margin-bottom: 2px;
// }

// .width-100 {
//   width: 100%;
// }

// .flex-direction-column {
//   flex-direction: column !important;
// }
