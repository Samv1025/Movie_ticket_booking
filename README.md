<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Movie Ticket Booking</title>
  <style>
    /* CSS styles here */
  </style>
</head>
<body>
  <header><h1>🎬 Movie Ticket Booking</h1></header>
  <nav><!-- navigation --></nav>
  <div class="container" id="home">
    <h2>Welcome to Movie Booking!</h2>
    <p>Book tickets for the latest movies in your city.</p>
  </div>
  <div class="container" id="movies">
    <h2>Now Showing</h2>
    <div class="movie"><h3>Avengers: Endgame</h3><p>Showtimes: 10:00 AM, 2:00 PM, 6:00 PM</p></div>
    <div class="movie"><h3>Jawan</h3><p>Showtimes: 11:30 AM, 3:30 PM, 7:30 PM</p></div>
    <div class="movie"><h3>Leo</h3><p>Showtimes: 9:00 AM, 1:00 PM, 5:00 PM</p></div>
  </div>
  <div class="container" id="book">
    <h2>Book Your Tickets</h2>
    <form onsubmit="alert('Booking Confirmed!'); return false;">
      <label>Select Movie:<select><option>Avengers: Endgame</option><option>Jawan</option><option>Leo</option></select></label>
      <label>Select Time:<select><option>10:00 AM</option><option>2:00 PM</option><option>6:00 PM</option></select></label>
      <label>Number of Tickets:<input type="number" min="1" max="10" /></label>
      <label>Your Name:<input type="text" required /></label>
      <button type="submit">Book Now</button>
    </form>
  </div>
  <div class="container" id="contact">
    <h2>Contact Us</h2>
    <p>Email: support@movietickets.com</p>
    <p>Phone: +91 9876543210</p>
  </div>
  <footer>&copy; 2025 Movie Ticket Booking. All rights reserved.</footer>
</body>
</html>
