(function ($) {
  'use strict';
  
  /**
   * Spinner
   */

    const spinnerBox = document.getElementById("spinner-box");
    $.ajax({
      type: 'GET',
      url: '/admin-panel/main/',
      success: function(response){
        setTimeout( () => {
          spinnerBox.classList.add("not-visible");
        }, 500);
      },
      error: function(error){
        setTimeout( () => {
          spinnerBox.classList.add("not-visible");
          alert("Что-то пошло не так повторите попытку");
        }, 500);
      }
    });

    $("#suggestion").ticker();

    
   
    
  
})(jQuery);