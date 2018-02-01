## API Design

> Draft v2.0. 
>
> (Changed user api based on QingdaoOJ designs.)
>
> Would be transferred to webpages with django-rest-framework after revisions.

### User

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
      "captcha":"abcd",
      "username":"WWWlab",
      "password":"12345"
  }
  ```

* #### ``GET`` /captcha

* #### ``GET`` /profile

* #### ``PUT`` /profile

* #### ....


> SEE OnlineJudgeFE/src/pages/oj/api.js & OnlineJudgeFE/src/pages/admin/api.js & 


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