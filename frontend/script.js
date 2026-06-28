const button = document.getElementById('calc-btn');
const resultDiv = document.getElementById('result');

// ボタンがクリックされたときの動き
button.addEventListener('click', async () => {
    resultDiv.innerText = '計算中（バックエンドと通信中）...';

    try {
        // バックエンド（FastAPI）のURLにデータを貰いに行く（Fetch通信）
        const response = await fetch('http://127.0.0.1:8000/');
        // 返ってきたデータをJSON形式として解析する
        const data = await response.json();
        
        // バックエンドから届いた message を画面に表示する
        resultDiv.innerText = data.message;
    } catch (error) {
        // 通信が失敗した場合のエラー処理
        resultDiv.innerText = 'エラー：バックエンドと通信できませんでした。';
        console.error(error);
    }
});