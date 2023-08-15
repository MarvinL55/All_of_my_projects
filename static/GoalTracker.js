function createNewGoal() {
    var title = prompt("Enter goal title:");
    var description = prompt("Enter goal description:");
    var deadline = prompt("Enter goal deadline:");

    if (title && description && deadline) {
        var goalsContainer = document.querySelector(".goals-container");

        var goalElement = document.createElement("div");
        goalElement.className = "goal-content";
        goalElement.innerHTML = `
            <h2 class="goal-title">${title}</h2>
            <p>${description}</p>
            <p>Deadline: ${deadline}</p>
            <button class="edit-button">Edit</button>
        `;

        goalsContainer.appendChild(goalElement);
    }
}
