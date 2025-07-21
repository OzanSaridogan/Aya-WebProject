document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('login-form');
    
    if (form) {
        form.addEventListener('submit', function (event) {
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value.trim();

            // Basic empty check
            if (!username || !password) {
                event.preventDefault(); // Stop form from submitting
                alert("Kullanıcı adı ve şifre boş bırakılamaz.");
                return;
            }

            // For debugging (will show in browser's developer console)
            console.log("Giriş bilgileri:", { username, password });
        });
    }
});
