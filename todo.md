
# 智慧廊道資料系統整合規劃

1. 架設工102 SQL伺服器 v
   - 使用MySQL v
   - 確認MySQL Client 可透過 Global IP連線 v
     - IP: 140.134.76.145:3306 v


2. 向各實驗室確認SQL Table型態，大致分為低採樣率與高採樣率資料
   - 低採樣率/離散，例如溫度、機器目前的狀態、flags...
     - 資料格式
       - properties format: machine_ID, all_data_name, physical_unit, data: sensor_model, data: DAQ model
       - ex: properties: [data_name_1,data_name_2], [None, degree_C], [None, TMP1826], [None, DAQ_1]
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

   - 高採樣率資料，因應讀取速度，建議採用datastore形式
     - 資料格式
       - properties format: machine_ID, data_name, sample_rate, physical_unit, sensor_model, DAQ model
        - ex: properties: data_name, sample_rate, g, 35C233, NI9234
      
      | Timestamp(segment start time) | data path            |
      | ----------------------------- | -------------------- |
      | IsoTimeFormat                 | \timestamp_data1.csv |
      | IsoTimeFormat                 | \ttimstamp_data2.csv |

   - properties 寫在對應的 config(*.json)
  - 如果一台機器同時擁有連續與離散的資料，則融合前面兩種資訊

3. 在各實驗室架設SQL伺服器
   - 101
   - 107
   - 109
  
4. 整合各實驗室的SQL伺服器，上傳或連線至工102 SQL伺服器

5. 討論圖形化的方式