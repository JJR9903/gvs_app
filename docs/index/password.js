
document.addEventListener("DOMContentLoaded", () => {
    const toggleIcon = document.querySelector(".toggle-password");
    const passwordInput = document.getElementById("password");
  
    if (toggleIcon && passwordInput) {
      toggleIcon.addEventListener("click", () => {
        const isPassword = passwordInput.type === "password";
        passwordInput.type = isPassword ? "text" : "password";
  
        // Optional: change icon if you have a different image
        toggleIcon.src = isPassword 
          ? "icons/visibility_off_gray.png" 
          : "icons/visibility_gray.png";
      });
    }
  });