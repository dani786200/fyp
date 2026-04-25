import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add IDs to elements for dynamic styling
content = content.replace('<div class="login-card">', '<div class="login-card" id="loginCard" style="border-top: 4px solid #8B5CF6;">')
content = content.replace('style="position:absolute;width:200px;height:200px;background:radial-gradient(circle,rgba(139,92,246,0.08),transparent);top:20%;left:10%;border-radius:50%;animation:pulse-glow 4s infinite;"',
                          'id="orb1" style="position:absolute;width:200px;height:200px;background:radial-gradient(circle,rgba(139,92,246,0.08),transparent);top:20%;left:10%;border-radius:50%;animation:pulse-glow 4s infinite;"')
content = content.replace('style="position:absolute;width:150px;height:150px;background:radial-gradient(circle,rgba(6,182,212,0.06),transparent);bottom:30%;right:15%;border-radius:50%;animation:pulse-glow 5s infinite 1s;"',
                          'id="orb2" style="position:absolute;width:150px;height:150px;background:radial-gradient(circle,rgba(6,182,212,0.06),transparent);bottom:30%;right:15%;border-radius:50%;animation:pulse-glow 5s infinite 1s;"')
content = content.replace('style="width:64px;height:64px;border-radius:16px;background:linear-gradient(135deg,#6366F1,#8B5CF6);display:inline-flex;align-items:center;justify-content:center;margin-bottom:16px;"',
                          'id="logoBg" style="width:64px;height:64px;border-radius:16px;background:linear-gradient(135deg,#6366F1,#8B5CF6);display:inline-flex;align-items:center;justify-content:center;margin-bottom:16px;transition:background 0.3s ease;"')
content = content.replace('Uni<span style="color:#818CF8;">GO</span>',
                          'Uni<span id="logoText" style="color:#818CF8;transition:color 0.3s ease;">GO</span>')

# 2. Update JavaScript to toggle colors globally
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
            
            // Global color elements
            const loginCard = document.getElementById('loginCard');
            const logoBg = document.getElementById('logoBg');
            const logoText = document.getElementById('logoText');
            const orb1 = document.getElementById('orb1');
            const orb2 = document.getElementById('orb2');

            errorMsg.style.display = 'none';

            if(role === 'admin') {
                // Purple Theme (Admin)
                tabAdmin.style.background = 'rgba(139, 92, 246, 0.1)';
                tabAdmin.style.color = 'var(--text-primary)';
                tabAdmin.style.border = 'none';
                
                tabDriver.style.background = 'var(--bg-card)';
                tabDriver.style.color = 'var(--text-muted)';
                tabDriver.style.border = '1px solid var(--border-light)';

                label.innerText = 'Email Address';
                input.type = 'text';
                input.placeholder = 'admin@must.edu.pk';
                btn.style.background = '#8B5CF6';
                btn.style.borderColor = '#8B5CF6';
                icon.innerHTML = '<path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />';
                
                // Global Accents
                loginCard.style.borderTop = '4px solid #8B5CF6';
                logoBg.style.background = 'linear-gradient(135deg,#6366F1,#8B5CF6)';
                logoText.style.color = '#818CF8';
                if(orb1) orb1.style.background = 'radial-gradient(circle,rgba(139,92,246,0.08),transparent)';
                if(orb2) orb2.style.background = 'radial-gradient(circle,rgba(6,182,212,0.06),transparent)';
            } else {
                // Emerald Theme (Driver)
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
                
                // Global Accents
                loginCard.style.borderTop = '4px solid #10B981';
                logoBg.style.background = 'linear-gradient(135deg,#059669,#10B981)';
                logoText.style.color = '#10B981';
                if(orb1) orb1.style.background = 'radial-gradient(circle,rgba(16,185,129,0.08),transparent)';
                if(orb2) orb2.style.background = 'radial-gradient(circle,rgba(52,211,153,0.06),transparent)';
            }
        }
"""

content = re.sub(r'<script>\s*function selectRole.*?}\s*', script_new, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
