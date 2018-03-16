/**
 * Created by sony on 12/3/18.
 */


function signup() {

    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var uname = document.getElementById('uname').value;

    var pwd = document.getElementById('pwd').value;
    var email = document.getElementById('email').value;
    var contact = document.getElementById('contact').value;
    var profile_picture = document.getElementById('profile_picture').value;
    alert(fname);
    alert(profile_picture);

    $.ajax({
        url: '/signup/validate_username/',
        type: 'POST',
        data: {
            'email': email,
            'fname': fname,
            'lname': lname,
            'uname': uname,
            'contact': contact,
            'pwd': pwd,
            'profile_picture': profile_picture,


        },
        dataType: 'json',
        success: function (contxt) {
                console.log(contxt)
                alert("Successfully Signup");
                if(contxt.success==true){
                    window.location.href = 'Otp';

                    // document.getElementById("email").value=contxt.email;
                    // document.getElementById("otp").value=contxt.otp;
                }
                else{
                alert("This User is already exist");
                }


            }
    });
}



// JSON.stringify(fname);
// JSON.stringify(lname);
// JSON.stringify(uname);
// JSON.stringify(pwd);
// JSON.stringify(email);
// JSON.stringify(contact);

// callFacebook();
// $.ajax({
//     url: '/login/login',
//     type: 'POST', // This is the default though, you don't actually need to always mention it
//     data:{ "fname":fname,"lname":lname,"uname":uname,"pwd":pwd,"email":email,"contact":contact},
//     success: function (data) {
//         alert("success")
//     }
//
// });
// function js(){
//     alert("eryi");
//   $.ajax({
//         url: '/signup/ajax/validate_username/',
//         type: 'POST',
//         data: {
//           'email': email
//         },
//         dataType: 'json',
//         success: function (sign) {
//           if (sign.is_taken) {
//             alert("A user with this username already exists.");
//           }
//
//         }
//       });

function Otp() {
    var otp = document.getElementById('otp').value;
    var email = document.getElementById('email').value;

    $.ajax({
        url: '/signup/otp_validate/',
        type: 'POST',
        data: {
            'email': email, 'otp': otp,
        },
        dataType: 'json',
        success: function (contxt) {
            {
                alert("Successful");
                console.log(contxt)
                window.location.href='/signup/profile/';
            }
        }
    });
}



