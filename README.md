# Nearby-Service :round_pushpin:
Project นี้เป็นส่วนหนึ่งของรายวิชา Service-Oriented Programming<br />
Faculty of Information Technology, KMITL

## About Service :page_facing_up:
    จะเป็น service ที่เก็บข้อมูลของผู้ใช้ ว่ามีพฤติกรรมชอบไปในสถานที่ใด
    แล้วจะแนะนำสถานที่ที่ผู้ใช้อาจจะสนใจเดินทางไป
  
## Service Architecture :hammer:
   ![architecture2](img_readme/architecture2.jpg)
   
## API :pencil:
    {
    "ip_address" : "String",
    "might_go_places" : [
        {
            "place" : {
                "place_name" : "String",
                "location" : {
                    "lat":"Double",
                    "long":"Double",
                 },
                "visit_count" : "int",
                "place_tag" : [],
                "avg_spending_time" : "Double",
            }
        },
        {
            "place" : {
                "place_name" : "String",
                "location" : {
                    "lat":"Double",
                    "long":"Double",
              
              },
                "visit_count" : "int",
                "place_tag" : [],
                "avg_spending_time" : "Double",
            }
        },
        .
        .
        .
    ],
    "status" : "String"
    }
## Database in Service :file_folder:
   ![db2](img_readme/db2.png)
### Schema
   User(**user_id**, ip)<br>
   Place(**tag_id**, place_name, latitude, longitude)<br>
   Tag(**tag_id**, tag_name)<br>
   Place_User(**place_id**, **user_id**, avg_spending_time, visit_count)<br>
   Place_Tag(**place_id**, **tag_id**)
    
## Team Members :busts_in_silhouette:

Name | StudentID | Github Username | Position
------------ | ------------- | ------------- | -------------
นายตฤณภัทร ปลั่งศรี | 60070028 | @Tintinap | Developer
นายนนท์ นิลขำ | 60070036 | @naive555 | Developer
นางสาวพัณณิตา เหมโก | 60070061 | @Pannita2212 | Business
นายภูมิ เนตราคม | 60070074 | @xzsawq47 | Developer
นางสาวสุธาทิพย์ ศรีโกษะบาล | 60070104 | @yves99 | Business
