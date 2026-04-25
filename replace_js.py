import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

script_new = """<script>
        function selectRole(role) {
            document.getElementById('selectedRole').value = role;
            const tabAdmin = document.getElementById('tabAdmin');
            const tabDriver = document.getElementById('tabDriver');
            const label = document.getElementById('userIdLabel');
            const input = document.getElementById('email');
            const icon = document.getElementById('userIdIcon');
            const btn = document.getElementById('loginBtn');
            const errorMsg = document.getElementById('errorMessage');

            errorMsg.style.display = 'none';

            if(role === 'admin') {
                tabAdmin.style.background = 'rgba(99, 102, 241, 0.1)';
                tabAdmin.style.color = 'var(--text-primary)';
                tabAdmin.style.border = 'none';
                
                tabDriver.style.background = 'var(--bg-card)';
                tabDriver.style.color = 'var(--text-muted)';
                tabDriver.style.border = '1px solid var(--border-light)';

                label.innerText = 'Email Address';
                input.type = 'email';
                input.placeholder = 'admin@must.edu.pk';
                btn.style.background = '';
                btn.style.borderColor = '';
                icon.innerHTML = '<path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />';
            } else {
                tabDriver.style.background = 'rgba(16, 185, 129, 0.1)';
                tabDriver.style.color = 'var(--text-primary)';
                tabDriver.style.border = 'none';
                
                tabAdmin.style.background = 'var(--bg-card)';
                tabAdmin.style.color = 'var(--text-muted)';
                tabAdmin.style.border = '1px solid var(--border-light)';

                label.innerText = 'Driver License No.';
                input.type = 'text';
                input.placeholder = 'e.g. HTV-1234';
                btn.style.background = '#10B981';
                btn.style.borderColor = '#10B981';
                icon.innerHTML = '<path d="M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.89l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.11l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4zm-6 3h8l.778 7H3.222L6 10z"/>';
            }
        }

        function togglePassword() {
            const pwdInput = document.getElementById('password');
            const eyeIcon = document.getElementById('eyeIcon');
            if (pwdInput.type === 'password') {
                pwdInput.type = 'text';
                eyeIcon.innerHTML = '<path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24M1 1l22 22"/>';
            } else {
                pwdInput.type = 'password';
                eyeIcon.innerHTML = '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>';
            }
        }

        function handleLogin(e) {
            e.preventDefault();
            const role = document.getElementById('selectedRole').value;
            const inputVal = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            const text = document.getElementById('loginText');
            const spinner = document.getElementById('loginSpinner');
            const errorMsg = document.getElementById('errorMessage');

            errorMsg.style.display = 'none';

            if(role === 'admin') {
                if (!inputVal.endsWith('@must.edu.pk') || password.length < 6) {
                    errorMsg.innerText = 'Invalid Admin Email or Password. Minimum 6 characters required.';
                    errorMsg.style.display = 'block';
                    return;
                }
            } else {
                let driversList = JSON.parse(localStorage.getItem('uniGoDrivers')) || [
                    { id: 'HTV-001', name: 'Saran Zafar', bus: 'None' },
                    { id: 'HTV-002', name: 'Imran Khan', bus: 'MUST-01' }
                ];
                const foundDriver = driversList.find(d => d.id === inputVal);
                if(!foundDriver || password.length < 4) {
                    errorMsg.innerText = 'Invalid Driver License No. or Password.';
                    errorMsg.style.display = 'block';
                    return;
                }
                localStorage.setItem('uniGoCurrentDriver', JSON.stringify(foundDriver));
            }

            text.style.display = 'none';
            spinner.style.display = 'block';

            setTimeout(() => {
                if(role === 'admin') {
                    window.location.href = 'views/admin/dashboard.html';
                } else {
                    window.location.href = 'views/driver/dashboard.html';
                }
            }, 800);
        }
    </script>"""

content = re.sub(r'<script>\s*function togglePassword.*?</script>', script_new, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
