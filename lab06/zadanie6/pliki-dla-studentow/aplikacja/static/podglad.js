// Skrypt strony /podglad przeniesiony z szablonu (CSP: script-src 'self').
// textContent wstawia dane jako zwykly tekst, wiec HTML/atrybuty zdarzen nie sa interpretowane.
document.getElementById("podglad").textContent = decodeURIComponent(location.hash.slice(1));
