document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // In a real scenario, you would send this data to a server
    // For demonstration, we'll just log it to the console
    console.log(`Username: ${username}`);
    console.log(`Password: ${password}`);

    // Here you might redirect the user or show a success message
    alert("Login successful!");
  });
