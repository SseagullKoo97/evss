function validatePhoneNumber() {
    // 获取用户输入的手机号码
    var phoneNumber = document.getElementById('phone_number').value;

    // 获取显示错误消息的 HTML 元素
    var phoneError = document.getElementById('phone-error');

    // 检查手机号码是否包含非数字字符或是否超过10位
    if (!/^\d+$/.test(phoneNumber) || phoneNumber.length > 10) {
        // 如果包含非数字字符或超过10位，显示错误信息
        phoneError.style.display = 'block';
    } else {
        // 如果验证通过，隐藏错误信息
        phoneError.style.display = 'none';
    }
}
