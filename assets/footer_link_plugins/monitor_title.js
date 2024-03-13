function getTitleFromUrl() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('title');
}

window.onload = function () {
    const title = getTitleFromUrl();
    if (title) {
        const targetTitle = document.getElementById(title);
        if (targetTitle) {
            window.scrollTo({
                top: targetTitle.offsetTop - 100,
                behavior: 'smooth'
            });
        }
    }
};

function scrollToTitle(titleId) {
    const targetTitle = document.getElementById(titleId);
    if (targetTitle) {
        window.scrollTo({
            top: targetTitle.offsetTop - 100,
            behavior: 'smooth'
        });
    }
}