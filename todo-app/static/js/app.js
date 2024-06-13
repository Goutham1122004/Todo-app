// static/js/app.js
document.getElementById('add-todo').addEventListener('submit', function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    fetch('/graphql', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            query: `
                mutation {
                    createTodo(
                        title: "${formData.get('title')}",
                        description: "${formData.get('description')}",
                        time: "${formData.get('time')}"
                    ) {
                        todo {
                            id
                            title
                            description
                            time
                        }
                    }
                }
            `
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle response and update the UI
    })
    .catch(error => console.error('Error:', error));
});
