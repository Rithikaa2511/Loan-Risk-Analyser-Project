// Loan Prediction Form Validation

const form = document.querySelector("form");

form.addEventListener("submit", function (event) {

    let name = document.getElementById("name").value.trim();
    let age = document.getElementById("age").value;
    let income = document.getElementById("income").value;
    let loan = document.getElementById("loan").value;
    let score = document.getElementById("score").value;
    let existing = document.getElementById("existing").value;

    if (
        name === "" ||
        age === "" ||
        income === "" ||
        loan === "" ||
        score === "" ||
        existing === ""
    ) {
        alert("Please fill all fields.");
        event.preventDefault();
        return;
    }

    if (age < 18 || age > 100) {
        alert("Age should be between 18 and 100.");
        event.preventDefault();
        return;
    }

    if (score < 300 || score > 900) {
        alert("Credit Score should be between 300 and 900.");
        event.preventDefault();
        return;
    }

    alert("Prediction is being processed...");
});