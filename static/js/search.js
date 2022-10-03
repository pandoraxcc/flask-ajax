$(document).ready(function(){

        $('.button').on('click', function(){

            if($(".data")) {

                $('.data').remove();

            }
            
            var query = $('.input-field').val();

            if (query) {

                console.log("sending query");

                $.ajax({

                    url: '/',
                    data: query,
                    type: 'POST',

                    success: function(response){

                        var search_result = response;
                        console.log("server replied");
                        $('.results').append(`<div class="data"><p class="success">Found a match(es)!</p><p>Array includes the following:</br> ${response}</p></div>`);

                    },
                    
                    error: function(error){

                        console.log(error);
                    }
                });

            }

        });

    });