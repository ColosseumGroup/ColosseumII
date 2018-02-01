## API Design

> Draft v1.0. 
>
> Would be transferred to webpages with django-rest-framework after revisions.

### User

* #### ``POST``  /user/{id} 

  ##### Explanation:

  ​	User login.

  ##### Example:

  ```python
  {
      "userName":"WWWlab",
      "password":"12345"
  }
  ```

* #### ``GET`` /user/{id}

  ##### Explanation: 

  ​	User log out

* #### ``POST`` /user

  ##### Explanation:

  ​	User sign up.

  ##### Example:

  ```python
  {
      "userName":"WWWlab",
      "password":"12345",
      "eMail":"abc@seu.edu.cn"
  }
  ```


### Game

* #### ``POST`` /game/{gametype}

  ##### Explanation:

  ​	Start a new game of type {gametype}.

  ##### Example:

  ```python
  {
      "opponent1ID":"oppo1",
      "opponent2ID":"oppo2",
      "opponent3ID":"oppo3"
  }
  ```

* #### ``POST`` /game/{gametype}/{gameID}

  ##### Explanation:

  ​	If the game is on, send user's current decision on the game to back end. 

  ​	Use operation ID to determine what kind of operation is being performed.

  ​	For instance, ID=0 could idicate

  ##### Example:

  ```python
  {
      "operationID":0,
      "operation":
      {
          "step0":
          {
              "posX":1,
     			"posY":10
          }
      }
  }
  ```

* #### ``GET`` /game/{gametype}/{gameID}

  ##### Explanation:

  ​	Return the whole record of the game with ID {gameID} till the current time.


### General View

* #### ``GET`` /game

  ##### Explanation:

  ​	Return records for all games every type.

* #### ``GET`` /game/{gametype}

  ##### Explanation:

  ​	Return records for all games of type {gametype}