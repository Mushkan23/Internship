/**$('.chat-button').on('click', function() {
    $('.chat-button').css({
        "display": "none"
    });
    $('.chat-box').css({
        "visibility": "visible"
    });
});
$('.chat-box .chat-box-header p').on('click', function() {
    $('.chat-button').css({
        "display": "block"
    });
    $('.chat-box').css({
        "visibility": "hidden"
    });
}) 
$("#addExtra").on("click", function() {
    $(".modal").toggleClass("show-modal");
}) 
$(".modal-close-button").on("click", function() {
    $(".modal").toggleClass("show-modal");
})
*/


var response = {
    "hi": "Hello!",
    "how are you": "I'm doing well",
    "What's your name": "My name is furry",
    "bye" : "Goodbye, have a nice day!"
};

function getResponse(message)
{
    message = message.toLowerCase();
    for(var key in reponses)
    {
        if (message.includes(key))
        {
            return reponse[key];
        }
    }
    return "I'm sorry."
}