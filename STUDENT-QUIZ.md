# 社區護理三單元線上小考：學生版

純 HTML / CSS / JavaScript 靜態頁，可使用 GitHub Pages 發布。20 題、每題 5 分；沿用已核對的原始試題，不含標準答案或教師資料。

## 學生操作

輸入學號、姓名（班級選填），選擇答案後按「下載答案卷」。將下載的 `<學號>.json` 依老師指定方式繳交。這個靜態網站不會自動收卷，也不顯示答案或成績。可按「修改後重新下載」再次產生答案卷，以老師最後收到的一份為準。作答進度只暫存在目前瀏覽器。

## GitHub Pages

將本資料夾的 index.html、.nojekyll、.gitignore、README.md 上傳到儲存庫根目錄。在 Settings → Pages，選擇 Deploy from a branch，分支選 main，資料夾選 / (root)，按 Save。使用 GitHub 顯示的正式網址分享給學生。

不要上傳教師版、題目答案資料、學員答案或成績。這個資料夾只包含發布所需檔案。

## 教師批改

將收回的 JSON 檔依學號存放到原本小考資料夾的 submissions，再使用原本的批改工具。相同學號重新繳交時，保留最後一份作為有效卷，先前檔案可另存至 _superseded。

題組：護理師 111–115 年，長期照護與居家護理 7 題、家庭衛生護理 7 題、學校衛生護理 6 題，抽題種子 20261018。題目依原出題年度作答。

題目來源：考選部考畢試題查詢平臺 https://wwwq.moex.gov.tw/exam/wFrmExamQandASearch.aspx 。官方聲明：「本網站資料，歡迎朋友連結使用。但引用時，請註明資料來源並請確保資料之完整（包括本項宣示在內），均不得任意增刪」2018 Ministry of Examination R.O.C.(Taiwan) All rights reserved.
