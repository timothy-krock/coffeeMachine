    var steve_info_url = "https://api.myjson.com/bins/mfqd5";
    /*{
        "status": -1,
        "sound": -1,
        "temp": -1,
        "ip": -1,
        "motion": -1,
        "lights": -1
        "lastConnected": -1
      }*/
    var steve_commands_url = "https://api.myjson.com/bins/iop95/?pretty";
    /*{
        "attribute": 0,
        "value": 0
    }*/

    var coffee_info_url = "https://api.myjson.com/bins/qfc49";
    /*{
      "status": -1,
      "ip": -1,
      "updated": -1,
      "coffeeTime": -1
    }*/

    var coffee_commands_url = "https://api.myjson.com/bins/1g0z4p/";
    //{"coffeeTime":-1}

    var message_url = "https://api.myjson.com/bins/14rvsp";
    /*{
        "message": -1,
        "messageBacklog": [

        ]
    }*/
    function refresh(){
        //Steve Info
        $.get(steve_info_url, function(data, textStatus, jqXHR) {
          console.log(data);
          var steve_info = data;
          document.getElementById("motion").innerHTML = (steve_info.motion);
          document.getElementById("updated").innerHTML = (steve_info.lastConnected);
          document.getElementById("ip").innerHTML = (steve_info.ip);
          document.getElementById("temp").innerHTML = (steve_info.temp);
          document.getElementById("lights").innerHTML = (steve_info.lights);
          document.getElementById("sound").innerHTML = (steve_info.sound);
        });
        //Coffee Info
        $.get(coffee_info_url, function(data, textStatus, jqXHR) {
          console.log(data);
          var coffee_info = data;
          document.getElementById("coffee-ip").innerHTML = (coffee_info.ip);
          document.getElementById("coffee-status").innerHTML = (coffee_info.status);
          document.getElementById("coffee-updated").innerHTML = (coffee_info.updated);
        });
        //Message
        $.get(message_url, function(data, textStatus, jqXHR) {
          console.log(data);
          var message = data;
          document.getElementById("message").innerHTML = (message.message);
        });
    }
    // Wrapper function for updateMessage(), (right below it) which
    // submits the function to the online message JSON
    // NOTE: THIS IS A  CRITICAL SECTION AND I HAVEN'T FIXED
    // READER-WRITER PROBLEM YET.
    function sendMessage(){
        updateMessage(document.getElementById('message-form').value);
    }
    function updateMessage(message){

        $.get(message_url, function(data, textStatus, jqXHR) {
          data['message'] = message;
          data["messageBacklog"].push(message);
          $.ajax({
              url:message_url,
              type:"PUT",
              data: JSON.stringify(data),
              contentType:"application/json; charset=utf-8",
              dataType:"json",
              success: function(data, textStatus, jqXHR){
                  console.log(data);
                  refresh()
              }
          });
        });
    }
    function update(machine, attr, val){

        $.get("https://api.myjson.com/bins/14sjn1", function(data, textStatus, jqXHR) {
          data[machine][attr] = val;
          $.ajax({
              url:"https://api.myjson.com/bins/14sjn1",
              type:"PUT",
              data: JSON.stringify(data),
              contentType:"application/json; charset=utf-8",
              dataType:"json",
              success: function(data, textStatus, jqXHR){
                  console.log(data);
                  refresh()

              }
          });
        });
    }
