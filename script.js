(() => {
  const button = document.querySelector('.menu-button');
  const nav = document.querySelector('.site-nav');
  button?.addEventListener('click', () => { const open = nav.classList.toggle('is-open'); button.setAttribute('aria-expanded', String(open)); });
  nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => { nav.classList.remove('is-open'); button?.setAttribute('aria-expanded', 'false'); }));
  const photo = document.querySelector('.hero-photo img');
  photo?.addEventListener('error', () => photo.closest('.hero-photo').classList.add('image-missing'));
  document.querySelector('#year').textContent = new Date().getFullYear();
})();
