function showContent(contentId) {
    // Hide all content divs
    var contentDivs = document.getElementsByClassName('main');
    for (var i = 0; i < contentDivs.length; i++) {
        contentDivs[i].style.display = 'none';
    }

    // Show the selected content div
    var selectedContent = document.getElementById(contentId);
    if (selectedContent) {
        selectedContent.style.display = 'block';
    }
};

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, {accordion: false});

    const menuThreat = document.getElementById('menu-threats');
    menuThreat.addEventListener('click', generateThreatList);

    const menuChat = document.getElementById('menu-chat');
    menuChat.addEventListener('click', generateChat);

    function generateChat() {
        const apiUrl = 'http://127.0.0.1:8000/api/new_chat/';

        // Using the Fetch API to make a GET request
        fetch(apiUrl)
            .then(response => {
                // Check if the response status is OK (200)
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                // Parse the JSON data in the response
                return response.json();
            })
            .then(data => {
                const chatBox = document.getElementById('chat-messages');
                chatBox.innerHTML = '';
                const sendButton = document.getElementsByClassName('send-button');
                sendButton[0].setAttribute('id', "send-"+ data.id );
            })
            .catch(error => {
                // Handle errors
                console.error('Error:', error);
            });
    }

    function generateThreatList() {
        const apiUrl = 'http://127.0.0.1:8000/api/incident/';

        // Using the Fetch API to make a GET request
        fetch(apiUrl)
            .then(response => {
                // Check if the response status is OK (200)
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                // Parse the JSON data in the response
                return response.json();
            })
            .then(data => {
                generateThreatElements(data);
            })
            .catch(error => {
                // Handle errors
                console.error('Error:', error);
            });
    }

    function generateThreatElements(data) {
        const ulElement = document.getElementById('threat-list');
        ulElement.innerHTML = '';
        // Loop through the JSON data and create <li> elements
        data.forEach(item => {
            // Create elements with the specified structure
            const liElement = document.createElement('li');
            liElement.innerHTML = `
                <div class="collapsible-header threat-entry" id="incident-${item.id}">
                    <i class="material-icons">error_outline</i>
                    ${item.id}: ${item.type}
                    <span class="badge">${item.time_stamp}</span>
                </div>
                <div class="collapsible-body">
                </div>
            `;

            ulElement.appendChild(liElement);
        });
    }

    function retrieveChat(id) {
        const apiUrl = "http://127.0.0.1:8000/api/get_chat/" + id;

        // Using the Fetch API to make a GET request
        fetch(apiUrl)
            .then(response => {
                // Check if the response status is OK (200)
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                // Parse the JSON data in the response
                return response.json();
            })
            .then(data => {
                var messageContainer = document.getElementById('chat-messages');
                messageContainer.innerHTML = '';
                data.msg.forEach(message => {

                    if (message.role == "user") {
                        var userMessageDiv = document.createElement('div');
                        userMessageDiv.className = 'message user-message';
                        userMessageDiv.textContent = message.content;
                        messageContainer.insertBefore(userMessageDiv, messageContainer.firstChild);
                    }
                    else if (message.role == "assistant") {
                        var responseMessageDiv = document.createElement('div');
                        responseMessageDiv.className = 'message';
                        responseMessageDiv.textContent = message.content;

                        messageContainer.appendChild(responseMessageDiv);
                        messageContainer.insertBefore(responseMessageDiv, messageContainer.firstChild);
                    }
                });
                

                var contentDivs = document.getElementsByClassName('main');
                for (var i = 0; i < contentDivs.length; i++) {
                    contentDivs[i].style.display = 'none';
                }

                // Show the selected content div
                var selectedContent = document.getElementById('chat');
                if (selectedContent) {
                    selectedContent.style.display = 'block';
                }
                // Scroll to the bottom to show the latest message
                chatContainer = document.getElementById('chat-container');
                chatContainer.scrollTop = messageContainer.scrollHeight;
                const sendButton = document.getElementsByClassName('send-button');
                sendButton[0].setAttribute('id', "send-"+ data.id );
            })
            .catch(error => {
                // Handle errors
                console.error('Error:', error);
            });
    }
    document.addEventListener('click', function (event) {
        // Check if the clicked element has the class
        if (event.target.classList.contains('threat-entry')) {
            // Get the clicked div and its sibling within the same li
            const clickedDiv = event.target;
            const clickedDivId = clickedDiv.id;
            const parts = clickedDivId.split('-');
            const siblingContentDiv = clickedDiv.nextElementSibling;

            // Call a function to generate content in the sibling content div
            generateThreatContent(siblingContentDiv, parts[1]);
        }

        if (event.target.classList.contains('threat-action')) {
            // Get the clicked div and its sibling within the same li
            const clickedDiv = event.target;
            const clickedDivId = clickedDiv.id;
            const parts = clickedDivId.split('-');
            var actionType = parts[0];
            var incidentId = parts[1];
            var stage = parts[2];
            var new_stage = stage;
            
            if (actionType=="chat"){
                retrieveChat(incidentId);
            }
            else {
                if (actionType=="next"){
                    var tmp_stage = Number(stage) + 1;
                    new_stage = tmp_stage.toString();
                }
                else if (actionType == "back"){
                    var tmp_stage = Number(stage) - 2;
                    new_stage = tmp_stage.toString();
                }

                const url = 'http://127.0.0.1:8000/api/update_incident/';

                // Data to be sent in the POST request (replace with your actual data)
                const postData = {
                    id: incidentId,
                    stage: new_stage
                };

                // Options for the fetch request
                const options = {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json', // Specify the content type if sending JSON data
                        // Include any other headers if needed
                    },
                    body: JSON.stringify(postData), // Convert the data to JSON format
                };
                fetch(url, options)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`HTTP error! Status: ${response.status}`);
                        }
                        return response.json(); // Assuming the response is in JSON format
                    })
                    .then(data => {
                        
                        const focusDiv = clickedDiv.closest(".collapsible-body");

                        // Call a function to re-generate content in the div
                        generateThreatContent(focusDiv, incidentId);
                    })
                    .catch(error => {
                        // Handle errors during the fetch
                        console.error('Error:', error);
                    });
            }
            
        }

        if (event.target.classList.contains('send-button')) {
            // Get the clicked div and its sibling within the same li
            const button = event.target;
            const buttonId = button.id;
            const parts = buttonId.split('-');
            var userInput = document.getElementById('user-input');
            var messageContainer = document.getElementById('chat-messages');

            // Get user input
            var userMessage = userInput.value.trim();
            if (userMessage !== '') {
                // Display user message
                var userMessageDiv = document.createElement('div');
                userMessageDiv.className = 'message user-message';
                userMessageDiv.textContent = userMessage;
                messageContainer.insertBefore(userMessageDiv, messageContainer.firstChild);
                chatContainer = document.getElementById('chat-container');
                chatContainer.scrollTop = messageContainer.scrollHeight;
                const url = 'http://127.0.0.1:8000/api/chat_msg/';

                // Data to be sent in the POST request (replace with your actual data)
                const postData = {
                    uid: parts[1],
                    msg: userMessage
                };

                // Options for the fetch request
                const options = {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json', // Specify the content type if sending JSON data
                        // Include any other headers if needed
                    },
                    body: JSON.stringify(postData), // Convert the data to JSON format
                };
                fetch(url, options)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`HTTP error! Status: ${response.status}`);
                        }
                        return response.json(); // Assuming the response is in JSON format
                    })
                    .then(data => {
                        // Handle the response data
                        var responseMessageDiv = document.createElement('div');
                        responseMessageDiv.className = 'message';
                        responseMessageDiv.textContent = data.msg;
                        if (data.link !== ""){
                            responseMessageDiv.innerHTML += data.link;
                        }
                        messageContainer.appendChild(responseMessageDiv);
                        messageContainer.insertBefore(responseMessageDiv, messageContainer.firstChild);

                        // Scroll to the bottom to show the latest message
                        chatContainer = document.getElementById('chat-container');
                        chatContainer.scrollTop = messageContainer.scrollHeight;
                    })
                    .catch(error => {
                        // Handle errors during the fetch
                        console.error('Error:', error);
                    });
                // Clear the input field
                userInput.value = '';
            }
        }

        if (event.target.classList.contains('create-incident')) {
            // Get the clicked div and its sibling within the same li
            const clickedDiv = event.target;
            const incidentId = clickedDiv.getAttribute('incident');
            const type = clickedDiv.getAttribute('type');

            const url = 'http://127.0.0.1:8000/api/create_incident/';

            // Data to be sent in the POST request (replace with your actual data)
            const postData = {
                id: incidentId,
                type: type
            };

            // Options for the fetch request
            const options = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json', // Specify the content type if sending JSON data
                    // Include any other headers if needed
                },
                body: JSON.stringify(postData), // Convert the data to JSON format
            };
            fetch(url, options)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json(); // Assuming the response is in JSON format
                })
                .then(data => {
                    // Hide all content divs
                    var contentDivs = document.getElementsByClassName('main');
                    for (var i = 0; i < contentDivs.length; i++) {
                        contentDivs[i].style.display = 'none';
                    }

                    // Show the selected content div
                    var selectedContent = document.getElementById('threats');
                    if (selectedContent) {
                        selectedContent.style.display = 'block';
                    }
                    generateThreatList();
                })
                .catch(error => {
                    // Handle errors during the fetch
                    console.error('Error:', error);
                });
        }

    });

    function generateThreatContent(contentDiv, id) {
        // Fetch data from the API (replace with your actual API endpoint)
        fetch('http://127.0.0.1:8000/api/incident/'+id)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                var stages = ``;
                data.finished.forEach(item => {
                    stages += `
                        <li class="collapsible-header green" style="color:white"><i class="material-icons">done</i>${item}</li>
                    `;
                });
                stages += `<li class="collapsible-header"><i class="material-icons">error_outline</i>${data.stage_name}</li>`;

                var actions = ``;
                data.action.forEach(action => {
                    actions = actions + `<a href="#" class="threat-action" id="${action}-${data.id}-${data.stage}">${action}</a>`
                });

                // Set the content in the content div
                contentDiv.innerHTML = `
                <div style="display:flex">
                    <div class="left-body">
                        <ul class="collapsible">${stages}</ul>
                    </div>
                    <div class="right-body card">
                        <div class="card-content">
                        ${data.playbook}
                        </div>
                        <div class="card-action">
                        ${actions}
                        </div>
                    </div>
                </div>`;
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
});