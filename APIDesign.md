## API Design

> Draft v3.0.   
> Would be transferred to webpages with django-rest-framework after revisions.

### User

- [x] ``POST``  /login
- [x] ``GET`` /logout
- [ ] ``POST`` /register

* #### ``POST``  /login 

  ##### Explanation: 

  ​	User login.

  ##### Example:

  ```python
  {
      "password":"12345",
      "username":"WWWlab"
  }
  ```


* #### ``GET`` /logout

  ##### Explanation: 

  ​	User log out

* #### ``POST`` /register

  ##### Explanation:

  ​	User sign up.

  ##### Example:

  ```python
  {
      "email":"abc@seu.edu.cn",
      "first_name":"abc",
      "last_name":"def",
      "username":"WWWlab",
      "password":"12345"
  }
  ```
  ​



### Game

- [x] ``POST`` /game/{GameTypeID}/create-new-game-room/
- [x] ``POST`` /game/{GameID}/
- [x] ``GET`` /game/{GameID}/
- [ ] ``POST`` /game/{GameID}/record/
- [ ] ``GET`` /game/{GameID}/record/

* #### ``POST`` /game/{GameTypeID}/create-new-game-room/

  ##### Explanation:

  ​	Create a new game room with user's ***port*** and gametype ***GameID***, return the generated room number. Login required.

  ##### Example:

  ```python
  {
    "port":"1234",
  }
  ```

  ​


* #### ``POST`` /game/{GameID}

  ##### Explanation:

  ​	Join a new game. Login required.

  ​	Need further implementation when interacting with game server.

* #### ``GET`` /game/{GameID}

  ##### Explanation:

  ​	Get the status of game with id = {GameID}

  ​	Return the game record in JSON if the game is over.

  **Example:**

  ```python
  {
    "game.status": "1", 
    "game.owner": "WWWlab", 
    "game.created_time": "2018-07-18T03:00:28.771623+00:00"
  }
  ```

  ​

* #### ``POST`` /game/{GameID}/record/

  ##### Explanation:

  ​	If the game is on, send user's current decision on the game to back end. 

  ​	Use operation ID to determine what kind of operation is being performed.

  ​	For default, ID = 0.

* #### ``GET`` /game/{GameID}/record/

  ##### Explanation:

  ​	Return the whole record of the game with ID {gameID} till the current time.		

------------------

## 前后端、后端与游戏服务器交互逻辑简记

#### 创建游戏并开始

1. 前端收到房主请求，调用后端CreateNewGameRoomAPI``POST`` (req,GameTypeID)

   返回新游戏id,房主自动加入新游戏

2. 前端显示新房间情况，调用后端``GameInfoAPI(req,GameID)``

   Post:

   将post的用户加入新房间，	

   若用户满足开启游戏条件则向服务器发消息

   GET:

   ​	显示当前房间信息

   ```python
   {
       'game.status':...
       'game.created_time':...
       'game.players':...
   }
   ```

3. 