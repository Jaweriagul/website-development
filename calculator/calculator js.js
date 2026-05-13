function clearscreen(){
        document.getElementById("result").value="";
}
//append the clicked button's value to the input field
function setscreenvalue(value){
        const r = document.getElementById("result");
        if(r.value==="enter an expression" || r.value==="invalid expression" ) r.value="";
        r.value += value;
}
//calculate and display the result
function calculateresult(){
       const resultElement = document.getElementById("result");
       const expression = resultElement.value.trim();
       //check for empty inputs
       if (expression === "") {
       resultElement.value = "enter an expression";
       return;
       }
       //evaluate the expression and handle errors
       try {
       resultElement.value = eval(expression);
       }
       catch(error){
       resultElement.value = "invalid expression";
       }
}
