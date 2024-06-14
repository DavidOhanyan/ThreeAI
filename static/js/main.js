const btn = document.getElementById("sendButton")
const quest_filed = document.querySelector('.question-display')
const gpt_field = document.querySelector('#gpt')
const claude_field = document.querySelector('#claude')
const gemini_field = document.querySelector('#gemini')

function handleKeyDown(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        btn.click();
    }
}

function autoGrow(element) {
    element.style.height = '5px';
    element.style.height = (element.scrollHeight) + 'px';
}

btn.addEventListener('click', function(event) {
    event.preventDefault();
    const msg = document.getElementById('inp').value;

    quest_filed.textContent = msg;
    document.getElementById('inp').value = '';

    fetch('/gpt', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({'message':msg})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Write a question');
        }
        return response.json();
    })

    .then(data => {
        gpt_field.innerHTML = `<p>${data.answer}</p>`
    })
    .catch((error) => {
        quest_filed.textContent = `Error happend:${error}`;
    });

///////////////////////////////////////////

    fetch('/gemini', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({'message':msg})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Write a question');
        }
        return response.json();
    })
    .then(data => {
        gemini_field.innerHTML = `<p>${data.answer}</p>`
    })
    .catch((error) => {
        quest_filed.textContent = `Error happend:${error}`;
    });

///////////////////////////////////////////

    fetch('/claude', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({'message':msg})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Write a question');
        }
        return response.json();
    })
    .then(data => {
        claude_field.innerHTML = `<p>${data.answer}</p>`
    })
    .catch((error) => {
        quest_filed.textContent = `Error happend:${error}`;
    });
    
    
});