// Check if game statistics are stored in local storage
const storedStatistics = JSON.parse(localStorage.getItem('gameStatistics')) || {
    guesses: 0,
    wins: 0,
    losses: 0
};

// Update and display game statistics
function updateStatistics() {
    document.getElementById('game').innerHTML = `
        <p>Number of Guesses: ${storedStatistics.guesses}</p>
        <p>Wins: ${storedStatistics.wins}</p>
        <p>Losses: ${storedStatistics.losses}</p>
    `;
}

// Example: Increase attempts and wins
//function makeGuess() {
//     storedStatistics.guesses++;
//     if (/* condition for winning the game */) {
//         storedStatistics.wins++;
//     } else {
//         storedStatistics.losses++;
//     }
//     localStorage.setItem('gameStatistics', JSON.stringify(storedStatistics));
//     updateStatistics();
// }

// Initialize game statistics display
updateStatistics();

/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */
function toggleHamburger() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }