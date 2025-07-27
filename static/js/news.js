function filterNews() {
    let input = document.getElementById("search-box").value.toLowerCase();
    let cards = document.querySelectorAll(".news-card");

    cards.forEach(card => {
        let title = card.querySelector(".news-title").textContent.toLowerCase();
        if (title.includes(input)) {
            card.removeAttribute("hidden");
        } else {
            card.setAttribute("hidden", "hidden");
        }
    });
}

function speakTitle(title) {
    if ('speechSynthesis' in window) {
        var utterance = new SpeechSynthesisUtterance(title);
        window.speechSynthesis.speak(utterance);
    } else {
        alert("Sorry, your browser does not support speech synthesis.");
    }
}