console.log("ok");

let submit = document.getElementById("Submit");
let login = document.getElementById("Login");
let loginDiv = document.getElementById("LoginDiv");
let otp;

window.addEventListener("load", (e) => {
	entities = Array.from(document.querySelectorAll(".entity"));
	document
		.getElementById("EntitySelect")
		.addEventListener("click", selectEntity);

	submit.addEventListener("click", handleSubmit);
});

function selectEntity(e) {
	if (!e.target.matches("button:not(.disabled)")) return;

	for (let i of entities) i.classList.remove("selected");
	e.target.classList.add("selected");
}

function handleSubmit() {
	let phone = document.getElementById("Number");
	let phoneWrapper = document.getElementById("NumberWrapper");
	let otpWrapper = document.getElementById("OtpWrapper");
	let entSel = document.getElementById("EntitySelect");

	otp = "";
	for (let i = 0; i < 4; i++)
		otp += Math.floor(10 * Math.random()).toString();

	console.log("OTP:", otp);
	alert("(Only for live demo)\nOTP: " + otp);

	otpWrapper.classList.remove("hide");
	phoneWrapper.classList.add("hide");
	// entSel.classList.add("hide");
	entSel.classList.add("disable");

	submit.classList.add('hide');
	loginDiv.classList.remove('hide');

}




login.addEventListener('click',(e) => {
	let otpEntered = document.getElementById("Otp").value;
	console.log(otpEntered);
	if(otpEntered === otp) {
		console.log('OTP RIGHT!!');
	} else {
		e.preventDefault();
		alert("Wrong OTP! Please Try Again.");
		window.history.back();
	}
});


// temp