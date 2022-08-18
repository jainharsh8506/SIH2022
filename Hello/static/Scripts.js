(function(d, m){
    var kommunicateSettings = 
        {"appId":"f0863bfee755704c0e0bcb0cefdc75e8","popupWidget":true,"automaticChatOpenOnNavigation":true};
    var s = document.createElement("script"); s.type = "text/javascript"; s.async = true;
    s.src = "https://www.kommunicate.io/livechat-demo?appId=f0863bfee755704c0e0bcb0cefdc75e8&botIds=nwns-6z4pl&assignee=nwns-6z4pl";
    var h = document.getElementsByTagName("head")[0]; h.appendChild(s);
    window.kommunicate = m; m._globals = kommunicateSettings;
})(document, window.kommunicate || {});