//trial 

/***function openChatWindow()
{
    var chatWindow = document.getElementById("chat-window");
    chatWindow.style.display = "block";
}

var chatLog = document.getAnimations("chat-log");
var chatInput = document.getElementById("chat-input");
chatInput.addEventListener("keypress", function(event){
    if (event.keyCode == 13){
        var userMessage = chatInput.value;
        chatLog.innerHTML += '<div class="user-message">' + userMessage + '</div>';
        chatInput.value ='';
        var botMessage = getResponse(userMessage);
        chatLog.innerHTML += '<div class="bot-message">' + botMessage + '</div>';
        chatLog.scrollTop = chatLog.scrollHeight;
    }
});
****/

async function loadIntents() {
    const response = await fetch('intents.json');
    const data = await response.json();
    return data.intents;
}

async function trainChatbot(){
    const intent = await loadIntents();
    

    const trainingData = intents.map(intent => ({
        input : intent.patterns,
        output : intent.name
    }));

    const net = new ImageBitmapRenderingContext.recurrent.LSTM();
    net.train(trainingData);
    return net;
}


async function getResponse(message, net){
    const intents = await loadIntents();

    const results = brain.likely(message, intents, net);
    const intent = intents.find(intent => intent.name === results);

    if (intent)
    {
        const response = intent.responses[Math.floor(Math.random() * intent.responses.length)];
        return response;
    }
    else
    {
        return "I'm sorry, I didn't understant what you said."
    }

}

function addMessageToChatWindow(message, isBot)
{
    const chatWindow = document.getElementById('chat-box');
    const chatMessage = document.getElement('div');
    if(isBot)
    {
        chatMessage.classList.add('chat-box-body-receive');  //bot-message
    }
    else
    {
        chatMessage.classList.add('chat-box-body-send');   //user-message
    }

    chatMessage.textContent = message;
    chatWindow.appendChild(chatMessage);

    chatWindow.scrollTop = chatWindow.scrollHeight;

}

async function handleUserMessage(message, net)
{
    addMessageToChatWindow(message, flase);

    const response = await getResponse(message, net);
    addMessageToChatWindow(response, true);
}

async function openChatbot()
{
    const net = await trainChatbot();
    const chatWindow = document.createElement('div');
    chatWindow.id = 'chat-box';                   //chat-window to chat-box
    document.body.appendChild(chatWindow);

    const inputField = document.createElement('input');
    inputField.type = 'text';
    inputField.placeholder = 'Type yout message here...'
    inputField.addEventListener('keydown', event => {
        if (event.key === 'Enter'){
            handleUserMessage(inputField.value, net);
            inputField.value = '';
        }
    });

    chatWindow.appendChild(inputField);

    const response = await getResponse('', net);
    addMessageToChatWindow(response, true);
}

const chatButton = document.getElementById('chat-button');
chatButton.addEventListener('click', openChatbot);