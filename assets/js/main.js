window.onload = function() {
    ["header", "footer"].forEach(id => {
        fetch(`./assets/html/${id}.html`)
            .then(response => response.text())
            .then(data => {
                document.getElementById(id).innerHTML = data;
            });
    });
};