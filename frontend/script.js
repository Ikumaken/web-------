// ボタン（背番号 calc-btn）を取得する
const button = document.getElementById('calc-btn');

// 結果を表示する箱（背番号 result）を取得する
const resultDiv = document.getElementById('result');

// ボタンがクリックされたときの動きを登録する
button.addEventListener('click',() => {
    // ひとまず画面の文字を書き換える
    resultDiv.innerText = 'ボタンが押されました！バックエンドと通信する準備をします。';
})
