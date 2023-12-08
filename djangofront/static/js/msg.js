// function sendMessage( id ) {
//     var userInput = document.getElementById('user-input');
//     var messageContainer = document.getElementById('chat-messages');

//     // Get user input
//     var userMessage = userInput.value.trim();
//     console.log(userMessage);
//     if (userMessage !== '') {
//         // Display user message
//         var userMessageDiv = document.createElement('div');
//         userMessageDiv.className = 'message user-message';
//         userMessageDiv.textContent = userMessage;
//         messageContainer.insertBefore(userMessageDiv, messageContainer.firstChild);

//         const url = 'http://127.0.0.1:8000/api/chat_msg';

//         // Data to be sent in the POST request (replace with your actual data)
//         const postData = {
//             uid: id,
//             msg: userMessage
//         };

//         // Options for the fetch request
//         const options = {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json', // Specify the content type if sending JSON data
//                 // Include any other headers if needed
//             },
//             body: JSON.stringify(postData), // Convert the data to JSON format
//         };
//         console.log(options);
//         fetch(url, options)
//             .then(response => {
//                 if (!response.ok) {
//                     throw new Error(`HTTP error! Status: ${response.status}`);
//                 }
//                 return response.json(); // Assuming the response is in JSON format
//             })
//             .then(data => {
//                 // Handle the response data
//                 console.log('Response:', data);
//             })
//             .catch(error => {
//                 // Handle errors during the fetch
//                 console.error('Error:', error);
//             });
//         // Clear the input field
//         userInput.value = '';

//         // Simulate a simple response (you can replace this with actual server communication)
//         setTimeout(function() {
//             var responseMessageDiv = document.createElement('div');
//             responseMessageDiv.className = 'message';
//             responseMessageDiv.textContent = 'This is a simple response.';
//             messageContainer.appendChild(responseMessageDiv);
//             messageContainer.insertBefore(responseMessageDiv, messageContainer.firstChild);

//             // Scroll to the bottom to show the latest message
//             chatContainer = document.getElementById('chat-container');
//             chatContainer.scrollTop = messageContainer.scrollHeight;
//         }, 500);
//     }
// }