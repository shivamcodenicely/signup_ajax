function login() {
    alert("hellloooooooooo");
    var pwd = document.getElementById('pwd').value;
    var email = document.getElementById('email').value;

    $.ajax({
        url: '/signup/validate/',
        type: 'POST',
        data: {
            'email': email, 'pwd': pwd,
        },
        dataType: 'json',
        success: function (contxt) {
            {
                console.log(contxt)
                alert("Successful");
                console.log(contxt.success)
                Email=contxt.email
                console.log(Email)
                if(contxt.success==true){


                    window.location.href='m?Email='+email;
                    }

                else{
                    alert("Email ID OR Password Incorrect")
                }
            }

        }
    });
}


function forget() {
    alert("hellloooooooooo");
//    var pwd = document.getElementById('contact').value;
    var email = document.getElementById('email').value;

    $.ajax({
        url: '/signup/forget_function/',
        type: 'POST',
        data: {
            'email': email,
        },
        dataType: 'json',
        success: function (contxt) {
            {
                console.log(contxt)
                alert("Forget Successful");
                window.location.href = 'loginajax';
            }
         }

    });
}


