$(document).bind('ready', function() {
      var portletlinks = $('a.portletlink')
      $(portletlinks).click(function(event, data) {
          var myurl = event.currentTarget;
              window.open(myurl, 'Continue_to_Application', 'width=800, height=800, scrollbars=yes, resizable=1');
              event.preventDefault();
        });
});      
