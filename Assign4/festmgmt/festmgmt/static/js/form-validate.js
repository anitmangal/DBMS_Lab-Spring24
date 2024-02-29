showDiv();

function showDiv() {
    var stud = document.getElementById('isStudent');
    var org = document.getElementById('isOrganiser');
    var isWhat = document.getElementById('isWhat');

    if (stud.checked && org.checked) {
        stud.checked = false;
        org.checked = false;
        isWhat.value = "participant";
    }

    if (stud.checked) {
        document.getElementById('studentPart').style.display = "block";
        document.getElementById('organiserPart').style.display = "none";
        isWhat.value = "student";
    }
    else if (org.checked) {
        document.getElementById('organiserPart').style.display = "block";
        document.getElementById('studentPart').style.display = "none";
        isWhat.value = "organiser";
    }
    else {
        document.getElementById('studentPart').style.display = "none";
        document.getElementById('organiserPart').style.display = "none";
        isWhat.value = "participant";
    }
}

function validate() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var dob = document.getElementById('dob').value;
    var mgen = document.getElementById('male');
    var fgen = document.getElementById('female');
    var ogen = document.getElementById('other');
    var collegeName = document.getElementById('collegeName').value;
    var collegeLocation = document.getElementById('collegeLocation').value;
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var cnfrmpass = document.getElementById('cnfrmpass').value;
    var stud = document.getElementById('isStudent');
    var rollNo = document.getElementById('rollno').value;
    var dept = document.getElementById('dept').value;
    var yearOfStudy = document.getElementById('yearofstudy').value;
    var org = document.getElementById('isOrganiser');
    var por = document.getElementById('por').value;
    if (validateName(name) && validateEmail(email) && validatePhone(phone) && validateDOB(dob) && validateGender(mgen, fgen, ogen) && validateCollegeName(collegeName) && validateCollegeLocation(collegeLocation) && validateUsername(username) && validatePassword(password) && validateCnfrmPass(password, cnfrmpass) && validateRollNo(stud, rollNo) && validateDept(stud, dept) && validateYearOfStudy(stud, yearOfStudy) && validatePOR(org, por)) {
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

function validateCollegeName(collegeName) {
    var collegeNameRegex = /^[a-zA-Z ]{2,50}$/;
    if (collegeNameRegex.test(collegeName)) {
        return true;
    } else {
        alert("College name should contain only alphabets and should be between 2 to 50 characters");
        return false;
    }
}

function validateCollegeLocation(collegeLocation) {
    var collegeLocationRegex = /^.*,[ ]{1}.*$/;
    if (collegeLocationRegex.test(collegeLocation)) {
        return true;
    } else {
        alert("Enter a valid college location: City, State");
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

function validateRollNo(stud, rollNo) {
    if (stud.checked) {
        var rollNoRegex = /^[0-9a-zA-Z]{2,10}$/;
        if (rollNoRegex.test(rollNo)) {
            return true;
        } else {
            alert("Enter a valid roll number (2 to 10 characters)");
            return false;
        }
    }
    return true;
}

function validateDept(stud, dept) {
    if (stud.checked) {
        var deptRegex = /^[A-Z ]{2}$/;
        if (deptRegex.test(dept)) {
            return true;
        } else {
            alert("Department should contain only contain uppercase alphabets and should be 2 characters long");
            return false;
        }
    }
    return true;
}

function validateYearOfStudy(stud, yearOfStudy) {
    if (stud.checked) {
        if (yearOfStudy >= 1 && yearOfStudy <= 5) {
            return true;
        } else {
            alert("Enter a valid year of study (1 to 5)");
            return false;
        }
    }
    return true;
}

function validatePOR(org, por) {
    if (org.checked) {
        var porRegex = /^[a-zA-Z ]{2,30}$/;
        if (porRegex.test(por)) {
            return true;
        } else {
            alert("Enter a valid position of responsibility (2 to 30 characters)");
            return false;
        }
    }
    return true;
}