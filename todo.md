1. 架設MySQL伺服器 v
   - 確認MySQL Client 可透過 Global IP連線 v
     - IP: 140.134.76.145:3306 v

---

2. 向各實驗室確認SQL Table型態
  - 低採樣率資料
    - 構想資料格式

| Timestamp     | data1 | data2 | physical unit1 | physical unit2 |
| ------------- | ----- | ----- | -------------- | -------------- |
| IsoTimeFormat | data  | data  | unit1          | unit2          |
| IsoTimeFormat | data  | data  | unit1          | unit2          |

  - 高採樣率資料，因應讀取速度，建議採用datastore形式
    - 構想資料格式

| Timestamp(starttime) | samplerate | physical unit | data path | sensor model | DAQ model |
| -------------------- | ---------- | ------------- | --------- | ------------ | --------- |
| IsoTimeFormat        | 12000      | unit1         | path1     | 35Q33        | NI9234    |
| IsoTimeFormat        | 6000       | unit1         | path2     | 13NQ         | NI9234    |

---
1. 在各實驗室架設SQL伺服器
  - 101 ?
  - 107
  - 109
  
2. 整合各實驗室的SQL伺服器，上傳或連線至工102 SQL伺服器