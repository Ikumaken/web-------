const button = document.getElementById('calc-btn');
const numInput = document.getElementById('num-input');
const resultDiv = document.getElementById('result');

button.addEventListener('click', async () => {
    // 1. 入力された値を取得
    const inputValue = numInput.value;
    
    if (!inputValue) {
        resultDiv.innerText = '数値を入力してください。';
        return;
    }

    resultDiv.innerHTML = '計算中...';

    try {
        // 2. バックエンドの /calc エンドポイントに数値をのせてリクエストを送る
        const response = await fetch(`http://127.0.0.1:8000/calc?number=${inputValue}`);
        const data = await response.json();
        
        // 3. バックエンドから返ってきた結果を綺麗に整形して画面に表示
        if (data.status === 'success') {
            resultDiv.innerHTML = `
                <p><strong>入力値:</strong> ${data.input_value}</p>
                <p><strong>厳密な下限 (Lower):</strong> ${data.lower_bound}</p>
                <p><strong>厳密な上限 (Upper):</strong> ${data.upper_bound}</p>
                <p><strong>区間幅 (Width):</strong> ${data.width}</p>
            `;
        } else {
            resultDiv.innerText = 'エラー: ' + data.message;
        }
    } catch (error) {
        resultDiv.innerText = 'エラー：バックエンドと通信できませんでした。';
        console.error(error);
    }
});