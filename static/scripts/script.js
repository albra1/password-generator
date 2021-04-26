document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = () => {
            data = new FormData(document.getElementById("generate_form"));
            const request = new XMLHttpRequest();
            request.open('POST', `/${button.id}`);
            request.onload = () => {
                const response = request.responseText;
                document.getElementById('password').innerHTML = response;
            }; 
            request.send(data);
        };
    });
});

let change_slider = () => {
    var slider = document.getElementById("length-range");
    var output = document.getElementById("len-slider");
    output.innerHTML = slider.value;
}
