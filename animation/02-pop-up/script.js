const openButton = document.getElementById('trigger-modal');
const closeButton = document.getElementById('close-modal');

function toggleModal() {
  const modal = document.querySelector('.popup-modal');
  const backdrop = document.querySelector('.backdrop');
  modal.classList.toggle('show');
  backdrop.classList.toggle('show');
}

openButton.addEventListener('click', toggleModal);
closeButton.addEventListener('click', toggleModal);
