let currentQuestionIndex = 0;
let questions = [];
const simpleImg = document.getElementById("simple-img");

// Clock!

const hourHand = document.getElementById("hourHand");
const minuteHand = document.getElementById("minuteHand");
const hourAngleInput = document.getElementById("hourAngle");
const minuteAngleInput = document.getElementById("minuteAngle");
const hourValue = document.getElementById("hourValue");
const minuteValue = document.getElementById("minuteValue");

function updateClockHands() {
    const hourAngle = parseInt(hourAngleInput.value);
    const minuteAngle = parseInt(minuteAngleInput.value);

    hourHand.style.transform = `translateX(-2px) translateY(-50px) rotate(${hourAngle}deg)`;
    minuteHand.style.transform = `translateX(-1px)
    translateY(-75px) rotate(${minuteAngle}deg)`;

    hourValue.textContent = hourAngle;
    minuteValue.textContent = minuteAngle;
}

hourAngleInput.addEventListener("input", updateClockHands);
minuteAngleInput.addEventListener("input", updateClockHands);

// Initial update
updateClockHands();

// End of clock

document.getElementById("start-btn").onclick = () => {
    fetch("/start")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        // wait for 2 seconds before calling group2()
        setTimeout(group2, 2000);
    });
};

function group2() {
    fetch("/group2")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        group3()
    });
}

function group3() {
    fetch("/group3")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        group4()
    });
}

function group4() {
    fetch("/group4")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        group5_1()
    });
}

function group5_1() {
    fetch("/group5_1")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        // remove class called no-display from simple-img
        simpleImg.classList.remove("no-display");
        simpleImg.getElementsByTagName("img")[0].src = data[1];
        group5_2()
    });
}

function group5_2() {
    fetch("/group5_2")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        group5_1_repeat()
    });
}

function group5_1_repeat() {
    fetch("/group5_1_repeat")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        // remove class called no-display from simple-img
        simpleImg.getElementsByTagName("img")[0].src = data[1];
        group5_2_repeat()
    });
}

function group5_2_repeat() {
    fetch("/group5_2_repeat")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        simpleImg.classList.add("no-display");
        group6()
    });
}

function group6() {
    fetch("/group6")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        group7_1()
    });
}

function group7_1() {
    fetch("/group7_1")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        document.querySelector('#choose-words').classList.remove('no-display')
        document.querySelector('#choose-words-inst').innerHTML = `Click the button with the word "${data[1]}"`
        // create two buttons inside #click-btn div woth the array from data[0]
        let btns = ''
        for (let i = 0; i < data[0].length; i++) {
            btns += `<button id="btn${i}" class="btn btn-primary btn-lg m-2">${data[0][i]}</button>`
        }
        document.querySelector('#click-btn').innerHTML = btns
        // group7_2()
    });
}

document.addEventListener('click', function(e) {
    if (e.target && e.target.classList.contains('btn-lg')) {
        target = e.target.innerHTML
        fetch("/group7_2", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({target: target})
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            document.querySelector('#choose-words').classList.add('no-display')
            group8_1()
        });
    }
})

function group8_1() {
    fetch("/group8_1")
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        document.querySelector('#clock-inst').innerHTML = `Set the clock to ${data['hour']}:${data['minute']}`
        document.querySelector('#clock-container').classList.remove('no-display')
    });
}

document.addEventListener('click', function(e) {
    if (e.target && e.target.id == 'clock-btn') {
        // hourAngle and minuteAngle id input fields values
        hourAngle = document.querySelector('#hourAngle').value
        minuteAngle = document.querySelector('#minuteAngle').value
        fetch("/group8_2", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({hour: hourAngle, minute: minuteAngle})
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            document.querySelector('#clock-container').classList.add('no-display')
            // group9()
        });
    }
})
