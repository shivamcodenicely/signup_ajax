$('#logout-button').click(function() {
$.ajax({
    type: "POST",
    url: "logout.php",
    success: function() {
       alert("You have been successfully logged out");
       window.location.href = "home.php";
    },
    error: function() {
        alert("Error! Something unexpected happened");
    }
});
return false;
});