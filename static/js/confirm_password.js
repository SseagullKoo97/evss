function validatePasswords() {
    // 获取密码和确认密码字段的值
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm_password').value;

    // 获取密码不匹配和长度错误的错误信息元素
    var passwordError = document.getElementById('password-error');

    // 检查密码长度
    if (password.length < 6) {
        passwordError.textContent = 'Password must be at least 6 characters.';
        passwordError.style.display = 'block';
    } else if (password !== confirmPassword) {
        // 如果密码不匹配，显示密码不匹配错误信息
        passwordError.textContent = 'Passwords do not match.';
        passwordError.style.display = 'block';
    } else {
        // 如果密码匹配并且长度合适，隐藏错误信息
        passwordError.style.display = 'none';
    }
}


