// Hamburger Menu
function hamburger() {
    var menu = document.getElementById("menu-links");

    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else { 
        menu.style.display = "block"; 
    }
}

// Get the modal element
var modal = document.getElementById("product-modal");

// Get all the "View Details" buttons
var buttons = document.querySelectorAll(".view-details");

// Get the close button for the modal
var closeButton = document.getElementsByClassName("close")[0];

// Product data
var productData = {
    1: {
        title: "Smart Thermostat",
        description: "Adjust your home’s temperature from anywhere using your smartphone. Compatible with all smart home systems.",
        price: "$199.99"
    },
    2: {
        title: "Smart Security Camera",
        description: "Keep your home safe with real-time video monitoring, night vision, and motion detection alerts.",
        price: "$149.99"
    },
    3: {
        title: "Smart Light Bulb",
        description: "Control the lighting in your home remotely. Choose colors and adjust brightness to set the perfect ambiance.",
        price: "$29.99"
    },
    4: {
        title: "Smart Door Lock",
        description: "Lock and unlock your door remotely with keyless entry and an automatic locking system.",
        price: "$249.99"
    },
    5: {
        title: "Smart Fridge",
        description: "Connect to the internet and get food recipes you can cook from the ingredients inside your fridge.",
        price: "$1649.99"
    },
    6: {
        title: "Smart Doorbell",
        description: "Monitor your door 24/7 with our new doorbell!",
        price: "$79.99"
    }
};

// When a "View Details" button is clicked
buttons.forEach(function(button) {
    button.addEventListener("click", function() {
        var productId = button.getAttribute("data-product");

        // Fill the modal with product details
        document.getElementById("modal-title").textContent = productData[productId].title;
        document.getElementById("modal-description").textContent = productData[productId].description;
        document.getElementById("modal-price").textContent = productData[productId].price;

        // Show the modal
        modal.style.display = "block";
    });
});

// Close the modal when the close button is clicked
closeButton.onclick = function() {
    modal.style.display = "none";
}

// Close the modal if the user clicks outside the modal
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}