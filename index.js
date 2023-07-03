document.addEventListener("DOMContentLoaded", function () {
    var filmsList = document.getElementById("films");
  
    // Remove the placeholder li element from the films ul
    var placeholderElement = document.getElementById("placeholder");
    if (placeholderElement) {
      filmsList.removeChild(placeholderElement);
    }
  
    // Fetch the movies data from the JSON file
    fetch("http://localhost:3000/films")
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        // Populate the movie menu with all movies
        data.forEach(function (movie, index) {
          var li = document.createElement("li");
          li.className = "film-item";
          li.textContent = movie.title;
  
          // Add a click event listener to each movie item
          li.addEventListener("click", function (event) {
            var movieIndex = event.target.getAttribute("data-movie-index");
            displayMovieDetails(data[movieIndex]);
          });
  
          // Set a custom attribute to store the movie index
          li.setAttribute("data-movie-index", index);
  
          filmsList.appendChild(li);
        });
  
        // Display the details of the first movie by default
        displayMovieDetails(data[0]);
      })
      .catch(function (error) {
        console.log("An error occurred while fetching the movies data:", error);
      });
  });
  
  function displayMovieDetails(movie) {
    var poster = movie.poster;
    var title = movie.title;
    var runtime = movie.runtime;
    var showtime = movie.showtime;
    var ticketsSold = movie.tickets_sold;
    var capacity = movie.capacity;
  
    // Calculate the number of available tickets
    var availableTickets = capacity - ticketsSold;
  
    // Update the HTML elements with movie details
    document.getElementById("movie-poster").src = poster;
    document.getElementById("movie-title").textContent = title;
    document.getElementById("movie-runtime").textContent =
      "Runtime: " + runtime + " minutes";
    document.getElementById("movie-showtime").textContent =
      "Showtime: " + showtime;
    document.getElementById("available-tickets").textContent =
      "Available Tickets: " + availableTickets;
  
    // Add click event listener to the "Buy Ticket" button
    var buyTicketButton = document.getElementById("buy-ticket");
    buyTicketButton.addEventListener("click", function () {
      if (availableTickets > 0) {
        // Decrease the available tickets count
        availableTickets--;
        // Update the available tickets text
        document.getElementById("available-tickets").textContent =
          "Available Tickets: " + availableTickets;
      } else {
        // Show an alert if the showing is sold out
        alert("Sorry, the showing is sold out.");
      }
    });
  }