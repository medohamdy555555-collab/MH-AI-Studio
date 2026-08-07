// طريق الهدى - MH AI Studio

function saveLastPage() {
    localStorage.setItem("lastPage", window.location.pathname);
}

function getLastPage() {
    return localStorage.getItem("lastPage");
}

window.addEventListener("load", () => {
    saveLastPage();
});
