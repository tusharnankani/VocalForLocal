console.log("ok");

let submitbtn = document.getElementById("Submit");
let phone = get("#Number");
console.log(phone);

submitbtn.onclick = function() {generate()};


function generate() {
    // if()
    let otp = "";
    for(let i = 0; i < 4; i++)
        otp += Math.floor(10 * Math.random()).toString();
    
    console.log("OTP:", otp);
    alert("(Only for live demo)\nOTP: " + otp);

}

function isValid(phone, inputOtp){
    let otp = Otp.otps[phone];
    if(!otp)
        return false;
    
    return otp.otp == inputOtp && !Util.hasExpired(otp.expiry);
}

