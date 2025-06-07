document.addEventListener("DOMContentLoaded", function () {
  const togglePassword = document.querySelector("#togglePassword");
  const passwordInput = document.querySelector("#password");

  togglePassword.addEventListener("click", function () {
      const type = passwordInput.type === "password" ? "text" : "password";
      passwordInput.type = type;
      this.classList.toggle("fa-eye");
      this.classList.toggle("fa-eye-slash");
  });
});

let currentIndex = 0;
const feedbacks = [
  {
    photo: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGVyc29ufGVufDB8fDB8fHww",
    message: "Glowify's products transformed my skin! I love the personalized skincare plan.",
    name: "- Sarah T."
  },
  {
    photo: "https://images.unsplash.com/flagged/photo-1570612861542-284f4c12e75f?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGVyc29ufGVufDB8fDB8fHww",
    message: "I feel more confident with my new routine. Highly recommend the consultation!",
    name: "- John D."
  },
  {
    photo: "https://plus.unsplash.com/premium_photo-1671656349322-41de944d259b?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cGVyc29ufGVufDB8fDB8fHww",
    message: "Fantastic customer service, and my skin has never felt better!",
    name: "- Emily R."
  },
  {
    photo: "https://images.unsplash.com/photo-1499952127939-9bbf5af6c51c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fHBlcnNvbnxlbnwwfHwwfHx8MA%3D%3D",
    message: "A game-changer! My skin has improved drastically thanks to Glowify.",
    name: "- Olivia W."
  }
];

const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
const feedbackPhoto = document.querySelector('.feedback-photo img');
const feedbackMessage = document.querySelector('.feedback-message');
const customerName = document.querySelector('.customer-name');

function updateFeedback() {
  const currentFeedback = feedbacks[currentIndex];
  feedbackPhoto.src = currentFeedback.photo;
  feedbackMessage.textContent = currentFeedback.message;
  customerName.textContent = currentFeedback.name;
}

prevBtn.addEventListener('click', () => {
  currentIndex = (currentIndex > 0) ? currentIndex - 1 : feedbacks.length - 1;
  updateFeedback();
});

nextBtn.addEventListener('click', () => {
  currentIndex = (currentIndex < feedbacks.length - 1) ? currentIndex + 1 : 0;
  updateFeedback();
});

// Initialize with the first feedback
updateFeedback();

// Scroll hero-btn function
function scrollToConsult() {
  document.getElementById("skincare-consult").scrollIntoView({
      behavior: "smooth"
  });
}
