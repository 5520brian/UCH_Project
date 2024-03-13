var password1 = document.getElementById("password1");
var password2 = document.getElementById("password2");

var submitButton = document.getElementById("submitButton");
var errorText = document.getElementById("errorText");

password1.addEventListener("input", validatePassword);
password2.addEventListener("input", validatePassword);

function validatePassword() {
    if (password1.value === password2.value) {
        submitButton.disabled = false;
        errorText.style.display = "none";
    }
    else {
        if (password2.value.length > 0) {
            errorText.style.display = "block";
        }
        else {
            errorText.style.display = "none";
        }
        submitButton.disabled = true;
    }
}