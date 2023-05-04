1. 架設MySQL伺服器 v
   - 確認MySQL Client 可透過 Global IP連線 v
     - IP: 140.134.76.145:3306 v


2. 向各實驗室確認SQL Table型態，大致分為低採樣率與高採樣率資料
  - 低採樣率資料，例如溫度、機器目前的狀態、flags...
    - 構想資料格式

| Timestamp     | data1 | data2 | physical unit1 | physical unit2 | status | flags |
| ------------- | ----- | ----- | -------------- | -------------- | ------ | ----- |
| IsoTimeFormat | data  | data  | unit1          | unit2          | run    | 0     |
| IsoTimeFormat | data  | data  | unit1          | unit2          | idle   | 1     |

  - 高採樣率資料，因應讀取速度，建議採用datastore形式
    - 構想資料格式
      - properties format: sample rate, physical unit, sensor model, DAQ model
        - ex: properties: sample rate, g, 35C233, NI9234
      - 這些 properties 寫在對應的 config 檔
    
| Timestamp(segment start time) | data path            |
| ----------------------------- | -------------------- |
| IsoTimeFormat                 | \timestamp_data1.csv |
| IsoTimeFormat                 | \ttimstamp_data2.csv |

3. 在各實驗室架設SQL伺服器
  - 101
  - 107
  - 109
  
4. 整合各實驗室的SQL伺服器，上傳或連線至工102 SQL伺服器