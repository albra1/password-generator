//load the buttons, send the requests when clicked
document.addEventListener('DOMContentLoaded', () => {

    gen_button = document.getElementById("generate-btn")
    gen_button.onclick = () => {
        data = new FormData(document.getElementById("generate_form"));
        const request = new XMLHttpRequest();
        request.open('POST', `/generate`);
        request.onload = () => {
            const response = request.responseText;
            document.getElementById('password').innerHTML = response;
        }; 
        request.send(data);
    };

    entropy_button = document.getElementById("entropy-btn")
    entropy_button.onclick = () => {
        data = new FormData(document.getElementById("entropy-form"));
        const request = new XMLHttpRequest();
        request.open('POST', `/check`);
        request.onload = () => {
            const response = request.responseText;
            document.getElementById('entropy-result').innerHTML = response;
        }; 
        request.send(data);
    };
 
});

//change the slider value
let change_slider = () => {
    var slider = document.getElementById("length-range");
    var output = document.getElementById("len-slider");
    output.innerHTML = slider.value;
}
