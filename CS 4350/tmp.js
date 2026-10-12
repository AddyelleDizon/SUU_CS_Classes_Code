window.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    // Get all URL params from previous submissions
    const params = new URLSearchParams(window.location.search);

    // Convert each into hidden fields
    for (const [key, value] of params.entries()) {
        if (key && value) {
            const hidden = document.createElement("input");
            hidden.type = "hidden";
            hidden.name = key;
            hidden.value = value;
            form.appendChild(hidden);
        }
    }

    // Set max for number field = current day of the month
    const numInput = form.querySelector('input[type="number"]');
    if (numInput) {
        const today = new Date();
        numInput.max = today.getDate(); // ensures no future days allowed
    }

    // Add validation before submit
    form.addEventListener("submit", (event) => {
        const inputs = form.querySelectorAll("input[type='email']");
        let valid = true;
        let message = "";

        if (inputs.length >= 2) {
            const schoolEmail = inputs[0].value.trim();
            const personalEmail = inputs[1].value.trim();

            // School email must end in .edu and contain a "."
            if (!schoolEmail.endsWith(".edu") || !schoolEmail.includes(".")) {
                valid = false;
                message += "School email must end in .edu and contain a period.\n";
            }

            // Personal email must NOT end in .edu and must contain a "."
            if (personalEmail.endsWith(".edu") || !personalEmail.includes(".")) {
                valid = false;
                message += "Personal email cannot end in .edu and must contain a period.\n";
            }
        }

        if (!valid) {
            alert(message);
            event.preventDefault(); // stop form submission
        }
    });
});



