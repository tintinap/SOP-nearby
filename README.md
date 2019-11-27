# Nearby-Service :round_pushpin:
Project นี้เป็นส่วนหนึ่งของรายวิชา Service-Oriented Programming<br />
Faculty of Information Technology, KMITL

## About Service :page_facing_up:
    เป็น service ที่เก็บข้อมูลของผู้ใช้ ว่ามีพฤติกรรมชอบเดินทางไปในสถานที่ใดจากนั้นจะแนะนำสถานที่ที่ผู้ใช้อาจจะสนใจเดินทาง
    ไปยังสถานที่นั้น โดยหลักการทำงานของ API คือจะมีการเก็บ IP ของเครื่องๆนั้นเป็น ID ที่ทำหน้าที่เหมือน Username ของ
    แต่ละ user ตัว API จะทำการดึง ข้อมูลจำนวนมากสุด 60 queries มาจาก Places API ของ Google Platform และ
    จะทำการเรียงลำดับจากค่าความนิยมที่ตัว Places API ได้ทำการจัดไว้ให้ แต่ถ้าหาก User มีข้อมูลเก็บไว้ตาม Database 
    ของตัว API จะถูกจัด priority ขึ้นมาไว้อันดับต้นๆ โดยในชุดข้อมูลพวกนั้นก็จะมีการเรียงลำดับตามค่า ranking ที่ตัว API 
    นี้ได้คำนวณไว้ด้วย
  
## Service Architecture :hammer:
   ![architecture](img_readme/architecture.png)
   
## How to use :mag:
    สามารถเข้าถึงผ่าน Link
    
       http://35.240.160.115:8000/nearby/<TYPE>,<LAT>,<LNG>
       
    โดยจะมีตัวแปรที่เราต้องใส่อยู่ 3 ตัว คือ TYPE, LAT และ LNG
    
     - TYPE : Type ของสถานที่ตาม Place Types ของ Google Map Platform โดยอ่านเพิ่มได้จากรายละเอียด link ด้านล่าง
          Link: https://developers.google.com/places/web-service/supported_types
     - LAT  : Latitude ปัจจุบันของเรา
     - LNG  : Longitude ปัจจุบันของเรา
     
    นอกจากนี้ผู้ที่นำ API ตัวนี้ไปใช้จำเป็นต้องนำ JavaScript ด้านล่างไปใช้ใน Tag <script></script> ใน Website ของตนด้วย
    เพื่อให้ตัว API สามารถทำงานได้อย่างมีประสิทธิภาพ

    <script>
        var lat = 0.0;
        var lng = 0.0;
        var error = document.createElement("p");
        error.id = "errorMessage";
        $("body").append(error);
        var positionOptions = {
            timeout: Infinity,
            maximumAge: 0,
            enableHighAccuracy: true
        };
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.watchPosition(showPosition, showError, positionOptions);
            } else {
                error.innerHTML = "Geolocation is not supported by this browser.";
            }
        }
        function showPosition(position) {
            lat = position.coords.latitude.toString();
            lng = position.coords.longitude.toString();
        }
        function showError(e) {
            switch (e.code) {
                case error.PERMISSION_DENIED:
                    error.innerHTML = "User denied the request for Geolocation.";
                    break;
                case error.POSITION_UNAVAILABLE:
                    error.innerHTML = "Location information is unavailable.";
                    break;
                case error.TIMEOUT:
                    error.innerHTML = "The request to get user location timed out.";
                    break;
                default:
                    error.innerHTML = "An unknown error occurred.";
            }
        }
        function autoSubmit() {
            const http = new XMLHttpRequest();
            const url = 'http://35.240.160.115/update/' + lat + ',' + lng;
            http.open("GET", url, true);
            http.send();
        }
        getLocation();
        setInterval(autoSubmit, 10000);
    </script>
   
## API SAMPLE :pencil:
   หากไม่มีข้อมูลเก็บไว้ก่อนจะไม่มี placeuser_id, place_idplace_id, user_iduser_id, avg_spending_time,
   visit_count, ranking ตาม place 2 ตัวแรกของตัว sample
   
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
## Database in the Service :file_folder:
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
