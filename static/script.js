let currentQuestionIndex = 0;
let questions = [];

document.getElementById("start-btn").onclick = () => {
    askQuestionOne();
};

function askQuestionOne() {
    fetch("/start")
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            // questions = data['questions'];
            // QuestionOne();
        });
}

// recursively ask questions
function QuestionOne() {
    if (currentQuestionIndex < questions.length) {
        const question = questions[currentQuestionIndex];
        console.log('Question asked:', question);
        fetch('/ask_and_listen', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                question: question
            })
        })
        .then((response) => response.json())
        .then((data) => {
            console.log('Response received:', data);
            document.querySelector('#text-box').value += data['spoken_text'] + '\n';
            currentQuestionIndex++;
            QuestionOne();
        })
        // .catch((error) => {
        //     console.error('Error:', error);
        //     // Optionally handle the error and continue with the next question
        //     currentQuestionIndex++;
        //     askQuestion();
        // });
    }
}
