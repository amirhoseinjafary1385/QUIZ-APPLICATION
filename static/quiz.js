
$(document).ready(function() {
    $.getJSON("quiz.json", function(data) {
        var quiz = data;
        var currentQuestion = 0;
        var score = 0;

        function showQuestion() {
            var question = quiz[currentQuestion];
            var options = "";
            for (var i = 0; i < question.options.length; i++) {
                options += "<label><input type='radio' name='answer' value='" + question.options[i] + "'>" + question.options[i] + "</label>";
            }
            $("#quiz").html(question.question + "" + options);
        }

        function checkAnswer() {
            var selectedAnswer = $("input[name='answer']:checked").val();
            if (selectedAnswer === quiz[currentQuestion].answer) {
                score++;
        }
        currentQuestion++;

        if(currentQuestion < quiz.length) {
            showQuestion();
        }else{

            $("#quiz").html("Quiz completed!");
            $("#result").html("You got " + score + " out of " + quiz.length + " questions correct!");
        }
    }

    
        showQuestion();

        $("#submit").click(function() {
            checkAnswer();
        });X
    });
});