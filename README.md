# Nearby-Service :round_pushpin:
Project นี้เป็นส่วนหนึ่งของรายวิชา Service-Oriented Programming<br />
Faculty of Information Technology, KMITL

## About Service :page_facing_up:
    เป็น service ที่เก็บข้อมูลของผู้ใช้ ว่ามีพฤติกรรมชอบเดินทางไปในสถานที่ใด
    จากนั้นจะแนะนำสถานที่ที่ผู้ใช้อาจจะสนใจเดินทางไปยังสถานที่นั้น
  
## Service Architecture :hammer:
   ![architecture](img_readme/architecture.png)
   
   
## API SAMPLE :pencil:
    [
        {
            "name": "place_name1",
            "geometry": {
                "location": {
                    "lat": 0.000000,
                    "lng": 0.000000
                },
                "viewport": {
                    "northeast": {
                        "lat": 0.000001,
                        "lng": 0.0000001
                    },
                    "southwest": {
                        "lat": 0.00000002,
                        "lng": 0.00000002
                    }
                }
            },
            "types": [
                "atm",
                "finance",
            ],
            "placeuser_id": 10,
            "place_idplace_id": 11,
            "user_iduser_id": 13,
            "avg_spending_time": 8.19,
            "visit_count": 10,
            "ranking": 9.638
        },
        {
            "name": "place_name2",
            "geometry": {
                "location": {
                    "lat": 0.000000,
                    "lng": 0.000000
                },
                "viewport": {
                    "northeast": {
                        "lat": 0.000001,
                        "lng": 0.0000001
                    },
                    "southwest": {
                        "lat": 0.00000002,
                        "lng": 0.00000002
                    }
                }
            },
            "types": [
                "atm"
            ],
            "placeuser_id": 6,
            "place_idplace_id": 7,
            "user_iduser_id": 13,
            "avg_spending_time": 4.587,
            "visit_count": 7,
            "ranking": 9.5478
        },
            .
            .
            .
        {
            "name": "place_name3",
            "geometry": {
                "location": {
                    "lat": 0.000000,
                    "lng": 0.000000
                },
                "viewport": {
                    "northeast": {
                        "lat": 0.000001,
                        "lng": 0.0000001
                    },
                    "southwest": {
                        "lat": 0.00000002,
                        "lng": 0.00000002
                    }
                }
            },
            "types": [
                "atm"
            ],
        },
        {
            "name": "place_name4",
            "geometry": {
                "location": {
                    "lat": 0.000000,
                    "lng": 0.000000
                },
                "viewport": {
                    "northeast": {
                        "lat": 0.000001,
                        "lng": 0.0000001
                    },
                    "southwest": {
                        "lat": 0.00000002,
                        "lng": 0.00000002
                    }
                }
            },
            "types": [
                "atm"
            ],
        },
            .
            .
            .
        ],
    }
## Database in Service :file_folder:
   ![new_db](img_readme/new_db.png)
### Schema
   User(**idUser**, ip, lat, lng, type)<br />
   Place(**idPlace**, place_name, latitude, longitude, image)<br />
   Tag(**idTag**, tag_name)<br />
   Place_User(**placeuser_id**, Place_idPlace, User_idUser, avg_spending_time, visit_count, ranking)<br />
   Tag_Place(**Place_idPlace**, **Tag_idTag**)
    
## Team Members :busts_in_silhouette:

Name | StudentID | Github Username | Position
------------ | ------------- | ------------- | -------------
นายตฤณภัทร ปลั่งศรี | 60070028 | @Tintinap | Developer
นายนนท์ นิลขำ | 60070036 | @naive555 | Developer
นางสาวพัณณิตา เหมโก | 60070061 | @Pannita2212 | Business
นายภูมิ เนตราคม | 60070074 | @xzsawq47 | Developer
นางสาวสุธาทิพย์ ศรีโกศะบาล | 60070104 | @yves99 | Business
