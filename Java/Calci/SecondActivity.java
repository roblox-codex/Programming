Intent intent = getIntent();
int numberOne = intent.getIntExtra("NUMBER_ONE", 0);
int numberTwo = intent.getIntExtra("NUMBER_TWO", 0);
String operation = intent.getStringExtra("OPERATION");

int result;
switch (operation) {
    case "add":
        result = numberOne + numberTwo;
        break;
    case "subtract":
        result = numberOne - numberTwo;
        break;
    case "multiply":
        result = numberOne * numberTwo;
        break;
    case "divide":
        result = numberOne / numberTwo;
        break;
    default:
        result = 0;
}

TextView resultText = findViewById(R.id.resultText);
resultText.setText("The result is: " + result);
