define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./main.js",
    "group": "D__18_19_1_colosseum_COLOSSEUM_ColosseumII_docs_main_js",
    "groupTitle": "D__18_19_1_colosseum_COLOSSEUM_ColosseumII_docs_main_js",
    "name": ""
  },
  {
    "name": "LoginAPI",
    "group": "User",
    "type": "POST",
    "url": "/user/login/",
    "title": "user sign in.",
    "parameter": {
      "examples": [
        {
          "title": "login-example:",
          "content": "{\n    \"username\":\"trial1\",\n    \"password\":\"trial1\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./apisrc.cpp",
    "groupTitle": "User"
  }
] });
