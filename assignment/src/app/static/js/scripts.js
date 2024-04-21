document.querySelector('.hero-button').addEventListener('click', function() {
    var mainElement = document.getElementById('main');

    var topPosition = mainElement.offsetTop;

    window.scrollTo({
        top: topPosition,
        behavior: 'smooth'
    });
});

function toggleDropdown() {
    document.getElementById("language-dropdown").classList;
}

window.onclick = function(event) {
    if (!event.target.matches('.dropdown-button')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
} 