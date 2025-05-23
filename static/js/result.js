function copyToClipboard() {
    const responseText = document.getElementById('responseText').textContent;
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(responseText).then(() => {
            alert('Resposta copiada para a área de transferência!');
        }).catch((err) => {
            console.error('Erro ao copiar para a área de transferência:', err);
        });
    } else {
        const textarea = document.createElement('textarea');
        textarea.value = responseText;
        document.body.appendChild(textarea);
        textarea.select();
        try {
            document.execCommand('copy');
            alert('Resposta copiada para a área de transferência!');
        } catch (err) {
            console.error('Erro ao copiar para a área de transferência:', err);
        }
        document.body.removeChild(textarea);
    }
}