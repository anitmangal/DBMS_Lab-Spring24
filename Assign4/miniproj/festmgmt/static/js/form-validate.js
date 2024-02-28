function validate() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var dob = document.getElementById('dob').value;
    var mgen = document.getElementById('male');
    var fgen = document.getElementById('female');
    var ogen = document.getElementById('other');
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var cnfrmpass = document.getElementById('cnfrmpass').value;
    if (validateName(name) && validateEmail(email) && validatePhone(phone) && validateDOB(dob) && validateGender(mgen, fgen, ogen) && validateUsername(username) && validatePassword(password) && validateCnfrmPass(password, cnfrmpass)) {
        return true;
    }
    return false;
}

function validateName(name) {
    var nameRegex = /^[a-zA-Z ]{2,30}$/;
    if (nameRegex.test(name)) {
        return true;
    } else {
        alert("Name should contain only alphabets and should be between 2 to 30 characters");
        return false;
    }
}

function validateEmail(email) {
    var emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (emailRegex.test(email)) {
        return true;
    }
    else {
        alert("Enter a valid email address");
        return false;
    }
}

function validatePhone(phone) {
    var phoneRegex = /^[0-9]{10}$/;
    if (phoneRegex.test(phone)) {
        return true;
    } else {
        alert("Phone number should contain exactly 10 digits");
        return false;
    }
}

function validateDOB(dob) {
    if (dob == "") {
        alert("Enter Date of Birth");
        return false;
    }
    var eighteenYearsAgo = moment().subtract(18, 'years');
    if (moment(dob).isBefore(eighteenYearsAgo)) {
        return true;
    } else {
        alert("You should be atleast 18 years old to register");
        return false;
    }
}

function validateGender(mgen, fgen, ogen) {
    if (mgen.checked || fgen.checked || ogen.checked) {
        return true;
    }
    else {
        alert("Choose a gender");
        return false;
    }
}

function validateUsername(username) {
    var usernameRegex = /^[a-zA-Z0-9]{5,20}$/;
    if (usernameRegex.test(username)) {
        return true;
    } else {
        alert("Username should contain only alphabets and numbers and should be between 5 to 20 characters");
        return false;
    }
}

function validatePassword(password) {
    var passwordRegex = /^[a-zA-Z0-9!@#$%^&*]{8,20}$/;
    if (passwordRegex.test(password)) {
        return true;
    } else {
        alert("Password should contain only alphabets, numbers and special characters and should be between 8 to 20 characters");
        return false;
    }
}

function validateCnfrmPass(password, cnfrmpass) {
    if (password == cnfrmpass) {
        return true;
    } else {
        alert("Passwords do not match");
        return false;
    }
}