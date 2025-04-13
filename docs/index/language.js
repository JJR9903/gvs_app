  // Language content stored in a JSON-like structure for scalability
  const languageContent = {
    es: {
      about:"Acerca",
      services:"Servicios",
      contact:"Contacto",
      about_menu:"Acerca",
      services_menu:"Servicios",
      contact_menu:"Contacto",
      current_lang:"ES",
      main_heading:"GVS App de Gestion & Data Analytics Ganadera",
      desc1: "Gestión Ganadera Inteligente, mayor Productividad",
      desc2: "Libere el poder de los datos para optimizar la salud, la reproducción y el rendimiento de su ganado.",
      bullet1: "<b>Monitoree la salud de sus animales</b>",
      bullet2: "<b>Optimice los programas de reproducción</b>",
      bullet3: "<b>Realice un seguimiento del crecimiento y el rendimiento</b>",
      bullet4: "<b>Acceda a sus datos en cualquier lugar, en cualquier momento</b>",
      sign_in: "Iniciar sesión",
      label_email: "Correo Electrónico",
      email: "Correo Electrónico",
      label_password: "Contraseña",
      password: "Contraseña",
      sign_in_email_text: "Iniciar sesión con E-mail",
      sign_in_google_text: "Iniciar sesión con Google",
      sign_in_apple_text: "Iniciar sesión con Apple",
      support: "Soporte",
      privacy_policy: "Política de privacidad",
      terms_of_service: "Términos de servicio"
    },
    en: {
      about:"About",
      services:"Services",
      contact:"Contact",
      about_menu:"About",
      services_menu:"Services",
      contact_menu:"Contact",
      current_lang:"EN",
      main_heading:"GVS Cattle Management & Data Analytics App",
      desc1: "Smart Livestock Management, Increased Productivity",
      desc2: "Unlock the power of data to optimize livestock health, reproduction, and performance.",
      bullet1: "<b>Monitor your animals' health</b>",
      bullet2: "<b>Optimize breeding programs</b>",
      bullet3: "<b>Track growth and performance</b>",
      bullet4: "<b>Access your data anytime, anywhere</b>",
      sign_in: "Sign In",
      label_email: "E-mail Address",
      email: "E-mail Address",
      label_password: "Password",
      password: "Password",
      sign_in_email_text: "Sign in with E-mail",
      sign_in_google_text: "Sign in with Google",
      sign_in_apple_text: "Sign in with Apple",
      support: "Support",
      privacy_policy: "Privacy Policy",
      terms_of_service: "Terms of Service"
    }
  };

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
        e.stopPropagation(); // Prevent this click from closing the dropdown immediately
        dropdown.classList.toggle("show");
      });
    }

    // Close the dropdown if clicking outside
    document.addEventListener("click", () => {
      dropdown.classList.remove("show");
    });
  });