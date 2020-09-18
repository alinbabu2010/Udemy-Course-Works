var questions = [{
    question: "What is the baby of a Moth known as?",
    choices: ["baby","infant","kit","larva"],
    correctAnswer: 3
},{
    question: "What is the adult of kid called",
    choices: ["calf","doe","goat","chick"],
    correctAnswer: 2
}, {
    question: "What is the young of Buffalo called?",
    choices: ["calf","baby",'pup',"cow"],
    correctAnswer: 0
} , {
    question: "What a baby Aligator called?",
    choices: ["baby","gator","hatching","calf"],
    correctAnswer: 2
} , {
    question: "What is baby Whale called?",
    choices: ["whala","cub","grub","infant"],
    correctAnswer: 1
} , {
    question: "What is a baby Monkey called?",
    choices: ["infant","baby","calf","pup"],
    correctAnswer: 0
}];
var currentQuestion = 0;
var correctAnswers = 0;
var quizOver = false;

$(document).ready(function () {
    displayCurrentQuestion();
    $(this).find(".quizMessage").hide();
    $(this).find(".nextButton").on('click',function () {
        if (!quizOver) {
            value = $("input[type='radio']:checked").val();
            if (value == undefined) {
                $(document).find(".quizMessage").text("Please select an answer.");
                $(document).find(".quizMessage").show();
            }else {
                $(document).find(".quizMessage").hide();
                if(value == questions[currentQuestion].correctAnswer) {
                    correctAnswers++;
                }
                currentQuestion++;
                if (currentQuestion < questions.length) {
                    displayCurrentQuestion();
                } else {
                    displayScore();
                    $(document).find(".nextButton").text("Play Again!");
                    quizOver = true;
                }
            }
        } else {
            quizOver = false;
            $(document).find(".nextButton").text("Next Question");
            resetQuiz();
            displayCurrentQuestion();
            $(document).find(".result").hide();   //To hide Score from user
        }
    });
});

// Function to dispaly the current question to user
function displayCurrentQuestion(){
    console.log("In display current Question");
    var question = questions[currentQuestion].question;
    var questionClass = $(document).find(".quizContainer > .question");
    var choiceList = $(document).find(".quizContainer > .choiceList");
    var numChoices = questions[currentQuestion].choices.length;
    // Set the questionClass text to the current question
    $(questionClass).text(question);
    // Remove all current <li> elements if any
    $(choiceList).find("li").remove();
    var choice;
    for (let i = 0; i < numChoices; i++) {
        choice = questions[currentQuestion].choices[i];
        $('<li><input type="radio" value="'+i+'" name="dynradio" />'+choice+'</li>').appendTo(choiceList);     
    }
}

//Function to reset the quiz
function resetQuiz() {
    currentQuestion = 0;
    correctAnswers = 0;
    $(document).find(".result").hide();             //To hide Score from user
}

//Function to display quiz score
function displayScore() {
    $(document).find(".quizContainer > .result").text("You scored :"+correctAnswers);
    $(document).find(".quizContainer > .result").show();
}
