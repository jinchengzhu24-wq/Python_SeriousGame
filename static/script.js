document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".choices-form");
    const overlay = document.getElementById("loadingOverlay");
    const selectedChoiceInput = document.getElementById("selectedChoice");

    if (!form || !overlay || !selectedChoiceInput) {
        return;
    }

    form.querySelectorAll(".choice-button").forEach((button) => {
        button.addEventListener("click", () => {
            selectedChoiceInput.value = button.dataset.choice || "";
        });
    });

    form.addEventListener("submit", (event) => {
        if (!selectedChoiceInput.value) {
            event.preventDefault();
            return;
        }

        document.body.classList.add("is-loading");
        overlay.classList.add("is-visible");
        overlay.setAttribute("aria-hidden", "false");

        form.querySelectorAll(".choice-button").forEach((button) => {
            button.disabled = true;
        });
    });
});
