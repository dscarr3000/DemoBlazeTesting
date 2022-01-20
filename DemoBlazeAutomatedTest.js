// Call this function from whatever function starts the automated tests
function testLogIn() {
	document.getElementById("loginpassword").value = "testPassword"
	document.getElementById("loginusername").value = "testUser"
	logIn()
}