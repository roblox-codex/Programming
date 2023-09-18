EditText editTextOne = findViewById(R.id.numberOne);
EditText editTextTwo = findViewById(R.id.numberTwo);
Button addButton = findViewById(R.id.additionButton);

addButton.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        int numberOne = Integer.parseInt(editTextOne.getText().toString());
        int numberTwo = Integer.parseInt(editTextTwo.getText().toString());

        Intent intent = new Intent(MainActivity.this, SecondActivity.class);
        intent.putExtra("NUMBER_ONE", numberOne);
        intent.putExtra("NUMBER_TWO", numberTwo);
        intent.putExtra("OPERATION", "add");
        startActivity(intent);
    }
});
