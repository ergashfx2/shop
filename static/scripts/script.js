const form = document.querySelector("form");
eField = form.querySelector(".username"),
eInput = eField.querySelector("input"),
pField = form.querySelector(".password"),
pInput = pField.querySelector("input");

form.onsubmit = (e)=>{
  e.preventDefault(); //preventing from form submitting
  //if email and password is blank then add shake class in it else call specified function
  (eInput.value == "") ? eField.classList.add("shake", "error") : checkUsername();
  (pInput.value == "") ? pField.classList.add("shake", "error") : checkPass();

  setTimeout(()=>{ //remove shake class after 500ms
    eField.classList.remove("shake");
    pField.classList.remove("shake");
  }, 500);

  eInput.onkeyup = ()=>{checkUsername();} //calling checkEmail function on email input keyup
  pInput.onkeyup = ()=>{checkPass();} //calling checkPassword function on pass input keyup

function checkUsername() {
  const pattern = /^[a-zA-Z0-9_]{3,20}$/; // Pattern for validating the username
  const usernameInput = document.getElementById("username"); // Replace "eInput" with your actual input element's ID
  const usernameField = document.getElementById("username-field"); // Replace "eField" with your actual field element's ID

  if (!pattern.test(usernameInput.value)) {
    // If the pattern is not matched, add an error class and remove the valid class
    usernameField.classList.add("error");
    usernameField.classList.remove("valid");

    const errorTxt = usernameField.querySelector(".error-txt");

    // If the username value is not empty, show "Enter a valid username" else show "Username can't be blank"
    usernameInput.value !== ""
      ? (errorTxt.innerText = "Enter a valid username")
      : (errorTxt.innerText = "Username can't be blank");
  } else {
    // If the pattern is matched, remove the error class and add the valid class
    usernameField.classList.remove("error");
    usernameField.classList.add("valid");
  }
}


  function checkPass(){ //checkPass function
    if(pInput.value == ""){ //if pass is empty then add error and remove valid class
      pField.classList.add("error");
      pField.classList.remove("valid");
    }else{ //if pass is empty then remove error and add valid class
      pField.classList.remove("error");
      pField.classList.add("valid");
    }
  }

  //if eField and pField doesn't contains error class that mean user filled details properly
  if(!eField.classList.contains("error") && !pField.classList.contains("error")){
    window.location.href = form.getAttribute("action"); //redirecting user to the specified url which is inside action attribute of form tag
  }
}
