import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class EvenOddNumberChecker extends Application {
    private TextField inputField;
    private Label resultLabel;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        // Create the input field
        inputField = new TextField();
        inputField.setPromptText("Enter an integer");

        // Create the button
        Button checkButton = new Button("Check");
        checkButton.setOnAction(e -> checkNumber());

        // Create the result label
        resultLabel = new Label();

        // Create a layout and add the components
        VBox root = new VBox(10);
        root.setPadding(new Insets(10));
        root.setAlignment(Pos.CENTER);
        root.getChildren().addAll(inputField, checkButton, resultLabel);

        // Create the scene and set it on the stage
        Scene scene = new Scene(root, 300, 200);
        primaryStage.setTitle("Even/Odd Number Checker");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void checkNumber() {
        try {
            // Get the user input from the text field
            int number = Integer.parseInt(inputField.getText());

            // Check if the number is even or odd
            if (number % 2 == 0) {
                resultLabel.setText(number + " is an even number.");
            } else {
                resultLabel.setText(number + " is an odd number.");
            }
        } catch (NumberFormatException e) {
            // Handle invalid input (non-integer value entered)
            resultLabel.setText("Invalid input. Please enter an integer.");
        }
    }
}
