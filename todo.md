
# 智慧廊道資料系統整合規劃

1. 架設工102 SQL伺服器 v
   - 使用MySQL v
   - 確認MySQL Client 可透過 Global IP連線 v
     - user: AIoTLab-MySQL
     - IP: 140.134.76.145:3306 v


2. 向各實驗室確認SQL Table型態，大致分為低採樣率與高採樣率資料
   - 低採樣率/離散，例如溫度、機器目前的狀態、flags...
     - 資料格式
       - properties format: machine_ID, all_data_name, physical_unit, data: sensor_model, data: DAQ_model
       - ex: properties: 107-CNC, [data_name_1,data_name_2], [None, degree_C], [None, TMP1826], [None, DAQ_1]
      - PS: 如果是從機台拉出來的資料不具備單位、sensor等屬性的話，則寫入None

      | Timestamp     | data_name   | value |
      | ------------- | ----------- | ----- |
      | IsoTimeFormat | data_name_1 | value |
      | IsoTimeFormat | data_name_2 | value |

    - 在分析之前需要另一個轉接程式變成以下型態

      | Timestamp     | data_name_1 | data_name_2 | data_name_3 |
      | ------------- | ----------- | ----------- | ----------- |
      | IsoTimeFormat | value       | value       | value       |
      | IsoTimeFormat | value       | value       | value       |

   - 高採樣率資料，因應讀取速度，採用datastore形式 (**以之前的DAQ軟體做測試**)
     - 資料格式
       - properties format: machine_ID, data_name, sample_rate, physical_unit, sensor_model, DAQ_model
        - ex: properties: 107-CNC, data_name, sample_rate, g, 35C233, NI9234
      
      | Timestamp(segment start time) | data path            |
      | ----------------------------- | -------------------- |
      | IsoTimeFormat                 | \timestamp_data1.npy |
      | IsoTimeFormat                 | \ttimstamp_data2.npy |

   - properties 寫在對應的 config(*.json)
  - 如果一台機器同時擁有連續與離散的資料，則融合前面兩種資訊

3. 在各實驗室架設SQL伺服器
   - 101
     - 目前狀況
       - 各機台有蒐集數據，放在各機台的操作電腦上
       - ~~沒有SQL伺服器~~ v 已架設 2023/5/10
       - 有Router(?)，但沒在用，機器基本上都是Global IP
       - 數據格式未設計
       - 大射出機和小射出機的控制器內部數據，可經由一台OPCUA server下載，先用這裡的數據呈現會比較快
         - OPCUA server後面接一台PC(PC內含SQL server)，可下載Server數據，同時上傳至SQL
     - 需要先做的事情
       - ~~確認Router IP, port設定~~ 使用Global IP，不需要
       - 訂定Table格式
     - suggestion
       - 每一個實驗室都架好server，且有獨立的戰情畫面(?)，102這邊再遠端(?)之類的
     - 已完成事宜
       - 已架設SQL伺服器
         - User: IMDMC-SQL
         - IP: 140.134.76.189:3306
   - 107
   - 109
  
4. 整合各實驗室的SQL伺服器，上傳或連線至工102 SQL伺服器

5. 討論圖形化的方式