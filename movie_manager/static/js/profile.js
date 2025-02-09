function togglePassword() {
    var passwordField = document.getElementById("password");
    if (passwordField.classList.contains("hidden-password")) {
        passwordField.textContent = "mypassword";
        passwordField.classList.remove("hidden-password");
    } else {
        passwordField.textContent = "********";
        passwordField.classList.add("hidden-password");
    }
}
