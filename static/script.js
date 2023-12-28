let currentQuestionIndex = 0;
let questions = [];

image_links = {"wrist watch" : "https://i.pinimg.com/736x/11/13/0a/11130ac9de99eae78af686a9742a15e3.jpg",
                "airplane": 'https://thumbs.dreamstime.com/b/airplane-18327587.jpg',
                "car": 'https://vehicle-images.dealerinspire.com/stock-images/chrome/d51929e056d69529c5bf44c4ceaddf7e.png',
}

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
        group5()
    });
}

function group5() {
    // choose a random image from image_links
    let keys = Object.keys(image_links);
    let random_key = keys[Math.floor(Math.random() * keys.length)];
    let random_image = image_links[random_key];

}