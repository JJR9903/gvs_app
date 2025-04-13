
  // Check if there is a saved language preference in localStorage
  const savedLanguage = localStorage.getItem("language");

  // Detect the user's browser language
  const userLanguage = navigator.language || navigator.userLanguage;

  // Set default language based on browser settings if no saved language
  let currentLanguage = savedLanguage || (userLanguage.startsWith("es") ? "es" : "en");

  // Function to update content based on the selected language
  function setLanguage(language) {
    localStorage.setItem("language", language);
    const content = languageContent[language];

    for (const key in content) {
      const el = document.getElementById(key);
      if (el) {
        el.innerHTML = content[key];
        el.placeholder = content[key];
        el.style.display = "block";
      }
    }
    document.getElementById("language_dropdown").classList.remove("show");    
  }

  // Set the language based on currentLanguage variable
  setLanguage(currentLanguage);


  const buttons = document.querySelectorAll("[data-lang]");
  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const lang = button.getAttribute("data-lang");
      setLanguage(lang);
      const dropdown = document.getElementById("language_dropdown");
      dropdown.classList.remove("show");
      
    });
  });



// Toggle dropdown visibility on button click
  document.addEventListener("DOMContentLoaded", () => {
    const dropBtn = document.querySelector(".dropbtn");
    const dropdown = document.getElementById("language_dropdown");

    if (dropBtn && dropdown) {
      dropBtn.addEventListener("click", (e) => {
        console.log("Language button clicked");
        e.stopPropagation(); // Prevent this click from closing the dropdown immediately
        dropdown.classList.toggle("show");
      });
    }

    // Close the dropdown if clicking outside
    document.addEventListener("click", () => {
      dropdown.classList.remove("show");
    });
  });