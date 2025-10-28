document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("pre").forEach(pre => {
    const code = pre.querySelector("code");
    if (!code) return;

    const btn = document.createElement("button");
    btn.textContent = "copy";
    btn.className = "copy-btn";
    btn.addEventListener("click", () => {
      navigator.clipboard.writeText(code.innerText).then(() => {
        btn.textContent = "copied";
        setTimeout(() => btn.textContent = "copy", 2000);
      });
    });

    pre.appendChild(btn);
  });
});

// pantalla
function activarPantallaCompleta() {
  const elem = document.documentElement;

  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.webkitRequestFullscreen) { // Safari
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) { // IE11
    elem.msRequestFullscreen();
  }
}

// box
document.addEventListener("DOMContentLoaded", () => {
  // Obtener el div .box-input que ya está en el HTML
  const boxInput = document.querySelector('.box-input');

  // Crear input
  const input = document.createElement('input');
  input.type = 'number';
  input.placeholder = 'Margen en px';
  input.style.marginRight = '8px';

  // Crear botón
  const boton = document.createElement('button');
  boton.textContent = 'Aplicar margen';

  // Insertar input y botón dentro del div .box-input
  boxInput.appendChild(input);
  boxInput.appendChild(boton);

  // Acción botón para aplicar margen a todos los .box-tt
  boton.addEventListener('click', () => {
    const valor = input.value;
    if (valor !== '') {
      const cajas = document.querySelectorAll('.box-tt');
      cajas.forEach(caja => {
        caja.style.marginTop = valor + 'px';
        caja.style.marginBottom = valor + 'px';
      });
    }
  });
});