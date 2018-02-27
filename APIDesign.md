## API Design

> Draft v3.0.   
> Would be transferred to webpages with django-rest-framework after revisions.

### User

- [x] ``POST``  /login
- [x] ``GET`` /logout
- [x] ``POST`` /register

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

- [x] ``GET`` /game/Othello/
- [x] ``POST`` /game/{GameID}/
- [x] ``GET`` /game/{GameID}/
- [x] ``POST`` /game/{GameID}/record/
- [x] ``GET`` /game/{GameID}/record/

* #### ``GET`` /game/Othello

  ##### Explanation:

  ​	Create a new game of Othello, return the new game ID to user


* #### ``POST`` /game/{GameID}

  ##### Explanation:

  ​	Join a new game.

* #### ``GET`` /game/{GameID}

  ##### Explanation:

  ​	Get the status of game with id = {GameID}

  ​	Return the game record in JSON if the game is over.

* #### ``POST`` /game/{GameID}/record/

  ##### Explanation:

  ​	If the game is on, send user's current decision on the game to back end. 

  ​	Use operation ID to determine what kind of operation is being performed.

  ​	For default, ID = 0.

* #### ``GET`` /game/{GameID}/record/

  ##### Explanation:

  ​	Return the whole record of the game with ID {gameID} till the current time.		

