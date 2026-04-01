const registerForm = document.getElementById('registerForm');
const formMessage = document.getElementById('formMessage');

registerForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(registerForm);
  const name = formData.get('name');

  formMessage.textContent = `Thanks, ${name}! You're registered for Shahothon 🎉`;
  registerForm.reset();
});
