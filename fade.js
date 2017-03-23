    // method that loads content into div
    var fnLoadPage = function(href) {
      $("#content").fadeOut("fast", function () {
        $this = $(this);
        var attr_href = "[href='" + href + "']";

        $this.load(href + ' #content > *', function() {
            $this.hide().fadeIn("slow");
        });
      });
    };

    // if back button is pressed, load previous content
    window.onpopstate = function(e) {
      fnLoadPage.call(undefined, document.location.pathname);
    };

    // update state link and call load function
    $(document).on('click', '.content_load', function(e) {
      e.preventDefault();
      e.stopImmediatePropagation();

      $this = $(this);
      var href = $this.attr('href');
      window.history.pushState({state: 'new'}, '', href);

      // load page
      fnLoadPage.call(undefined, href);
    });
